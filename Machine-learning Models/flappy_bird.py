import gymnasium
import flappy_bird_gymnasium
import pygame
import numpy as np
import pickle
import os
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# --- Q-LEARNING PARAMETERS ---
GAMMA = 0.99              # Discount factor (future rewards importance)
ALPHA = 0.1               # Learning rate
EPSILON_START = 1.0       # Initial exploration rate
EPSILON_END = 0.01        # Minimum exploration rate
EPSILON_DECAY = 0.99995   # Decay rate per episode
TOTAL_EPISODES = 50000    # Total training episodes

# Save file for Q-table
Q_TABLE_FILE = "q_table.pkl"

# --- STATE DISCRETIZATION ---
def get_state(obs):
    """
    Discretizes the continuous state observation.
    
    Flappy Bird observation (12 values):
    - obs[0]: horizontal distance to next pipe
    - obs[1]: difference between player y and next upper pipe y
    - obs[2]: difference between player y and next lower pipe y
    - obs[3-11]: other values (velocity, etc.)
    """
    
    if obs is None or len(obs) < 3:
        return (0, 0)
    
    # Horizontal distance to next pipe (normalized)
    horizontal_dist = int(obs[0] / 20)  # Divide by 20 to reduce state space
    horizontal_dist = max(0, min(20, horizontal_dist))  # Clamp between 0-20
    
    # Vertical distance to pipe gap center
    vertical_dist = int(obs[1] / 10)  # Use upper pipe distance
    vertical_dist = max(-50, min(50, vertical_dist))  # Clamp between -50 to 50
    
    return (horizontal_dist, vertical_dist)


# --- Q-TABLE AGENT CLASS ---
class QAgent:
    def __init__(self, actions=[0, 1]):
        """
        Initialize Q-Learning Agent
        Actions: 0 = do nothing, 1 = flap
        """
        self.q_table = {}
        self.actions = actions
        self.epsilon = EPSILON_START
        self.episode = 0
        
        # Load existing Q-table if available
        if os.path.exists(Q_TABLE_FILE):
            try:
                with open(Q_TABLE_FILE, "rb") as f:
                    self.q_table = pickle.load(f)
                print(f"✅ Loaded existing Q-table with {len(self.q_table)} states.")
            except Exception as e:
                print(f"⚠️ Error loading Q-table: {e}. Starting fresh.")
                self.q_table = {}
        else:
            print("📝 No existing Q-table found. Starting fresh.")
    
    def get_q_value(self, state, action):
        """Get Q-value for state-action pair, default to 0 if not found."""
        return self.q_table.get((state, action), 0.0)
    
    def choose_action(self, state, train=True):
        """
        Epsilon-greedy action selection.
        During training: explore with probability epsilon
        During evaluation: always exploit (choose best action)
        """
        if train and np.random.uniform(0, 1) < self.epsilon:
            # Explore: random action
            return np.random.choice(self.actions)
        else:
            # Exploit: choose best action
            q_values = [self.get_q_value(state, action) for action in self.actions]
            max_q = max(q_values)
            
            # If multiple actions have same Q-value, choose randomly among them
            best_actions = [action for action, q in zip(self.actions, q_values) if q == max_q]
            return np.random.choice(best_actions)
    
    def update_q_table(self, state, action, reward, next_state, terminated):
        """
        Update Q-table using Q-learning formula:
        Q(s,a) = Q(s,a) + α[r + γ·max(Q(s',a')) - Q(s,a)]
        """
        current_q = self.get_q_value(state, action)
        
        if terminated:
            # No future rewards if episode ended
            max_future_q = 0
        else:
            # Maximum Q-value for next state
            max_future_q = max([self.get_q_value(next_state, a) for a in self.actions])
        
        # Q-learning update formula
        new_q = current_q + ALPHA * (reward + GAMMA * max_future_q - current_q)
        self.q_table[(state, action)] = new_q
    
    def decay_epsilon(self):
        """Decay epsilon after each episode."""
        self.epsilon = max(EPSILON_END, self.epsilon * EPSILON_DECAY)
    
    def save_q_table(self):
        """Save Q-table to file."""
        try:
            with open(Q_TABLE_FILE, "wb") as f:
                pickle.dump(self.q_table, f)
            print(f"💾 Q-table saved ({len(self.q_table)} states)")
        except Exception as e:
            print(f"⚠️ Error saving Q-table: {e}")


# --- TRAINING FUNCTION ---
def train_agent():
    """Train the Q-Learning agent."""
    print("\n" + "="*60)
    print("🎮 FLAPPY BIRD Q-LEARNING TRAINING")
    print("="*60)
    
    # Create environment without rendering (faster training)
    env = gymnasium.make("FlappyBird-v0", render_mode=None)
    agent = QAgent()
    
    print(f"\n📊 Training for {TOTAL_EPISODES:,} episodes...")
    print(f"Initial epsilon: {EPSILON_START}")
    print(f"Final epsilon: {EPSILON_END}")
    print(f"Saving checkpoint every 1000 episodes...\n")
    
    best_score = 0
    scores = []
    
    try:
        for episode in range(1, TOTAL_EPISODES + 1):
            obs, info = env.reset()
            state = get_state(obs)
            terminated = False
            truncated = False
            total_reward = 0
            steps = 0
            
            while not (terminated or truncated):
                # Choose action
                action = agent.choose_action(state, train=True)
                
                # Take action in environment
                next_obs, reward, terminated, truncated, info = env.step(action)
                next_state = get_state(next_obs)
                
                # Update Q-table
                agent.update_q_table(state, action, reward, next_state, terminated or truncated)
                
                state = next_state
                total_reward += reward
                steps += 1
            
            # Decay epsilon
            agent.decay_epsilon()
            
            # Track score
            current_score = info.get('score', 0)
            scores.append(current_score)
            
            if current_score > best_score:
                best_score = current_score
            
            # Print progress
            if episode % 1000 == 0:
                avg_score = np.mean(scores[-1000:]) if len(scores) >= 1000 else np.mean(scores)
                print(f"Episode {episode:,}/{TOTAL_EPISODES:,} | "
                      f"Epsilon: {agent.epsilon:.4f} | "
                      f"Score: {current_score} | "
                      f"Avg Score (last 1000): {avg_score:.2f} | "
                      f"Best: {best_score} | "
                      f"Steps: {steps} | "
                      f"Q-States: {len(agent.q_table):,}")
                agent.save_q_table()
            
            # Quick progress updates every 100 episodes
            elif episode % 100 == 0:
                print(f"Episode {episode:,} - Score: {current_score}, Epsilon: {agent.epsilon:.4f}")
        
        print("\n" + "="*60)
        print("✅ TRAINING COMPLETE!")
        print(f"Final Best Score: {best_score}")
        print(f"Total Q-States Learned: {len(agent.q_table):,}")
        print("="*60)
        agent.save_q_table()
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Training interrupted by user.")
        print(f"Saving progress... (Episode {episode})")
        agent.save_q_table()
    
    finally:
        env.close()


# --- EVALUATION FUNCTION ---
def evaluate_agent(num_games=5):
    """Evaluate the trained agent with visualization."""
    print("\n" + "="*60)
    print("🎮 FLAPPY BIRD Q-LEARNING EVALUATION")
    print("="*60)
    
    if not os.path.exists(Q_TABLE_FILE):
        print("❌ No trained Q-table found! Please train the agent first (choose 'T').")
        return
    
    # Initialize pygame
    pygame.init()
    
    # Create environment with rendering
    env = gymnasium.make("FlappyBird-v0", render_mode="human")
    agent = QAgent()
    agent.epsilon = 0  # No exploration during evaluation
    
    print(f"\n🤖 AI will play {num_games} games using trained Q-table...")
    print(f"Q-table size: {len(agent.q_table):,} states")
    print("\nClose the game window to stop evaluation.\n")
    
    scores = []
    
    try:
        for game in range(1, num_games + 1):
            print(f"\n--- Game {game}/{num_games} ---")
            
            obs, info = env.reset()
            state = get_state(obs)
            terminated = False
            truncated = False
            total_reward = 0
            steps = 0
            
            while not (terminated or truncated):
                # Handle pygame events (window close, etc.)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("\n👋 Evaluation stopped by user.")
                        env.close()
                        pygame.quit()
                        return
                
                # Agent chooses best action (no exploration)
                action = agent.choose_action(state, train=False)
                
                # Take action
                next_obs, reward, terminated, truncated, info = env.step(action)
                next_state = get_state(next_obs)
                
                state = next_state
                total_reward += reward
                steps += 1
            
            # Game ended
            final_score = info.get('score', 0)
            scores.append(final_score)
            print(f"Game {game} finished!")
            print(f"  Score: {final_score}")
            print(f"  Steps survived: {steps}")
            print(f"  Total reward: {total_reward:.2f}")
        
        # Summary
        print("\n" + "="*60)
        print("📊 EVALUATION SUMMARY")
        print("="*60)
        print(f"Games played: {len(scores)}")
        print(f"Average score: {np.mean(scores):.2f}")
        print(f"Best score: {max(scores)}")
        print(f"Worst score: {min(scores)}")
        print(f"Total pipes passed: {sum(scores)}")
        print("="*60)
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Evaluation interrupted.")
    
    finally:
        env.close()
        pygame.quit()
        print("\n✅ Evaluation complete!")


# --- WATCH SINGLE GAME ---
def watch_agent():
    """Watch the agent play continuously until you close the window."""
    print("\n" + "="*60)
    print("👀 WATCH MODE - Press ESC or close window to exit")
    print("="*60)
    
    if not os.path.exists(Q_TABLE_FILE):
        print("❌ No trained Q-table found! Please train the agent first.")
        return
    
    pygame.init()
    env = gymnasium.make("FlappyBird-v0", render_mode="human")
    agent = QAgent()
    agent.epsilon = 0
    
    game_count = 0
    
    try:
        while True:
            game_count += 1
            print(f"\n🎮 Starting game #{game_count}...")
            
            obs, info = env.reset()
            state = get_state(obs)
            terminated = False
            truncated = False
            
            while not (terminated or truncated):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        raise KeyboardInterrupt
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        raise KeyboardInterrupt
                
                action = agent.choose_action(state, train=False)
                next_obs, reward, terminated, truncated, info = env.step(action)
                next_state = get_state(next_obs)
                state = next_state
            
            print(f"Game #{game_count} - Score: {info.get('score', 0)}")
    
    except KeyboardInterrupt:
        print(f"\n\n👋 Watched {game_count} games. Goodbye!")
    
    finally:
        env.close()
        pygame.quit()


# --- MAIN MENU ---
def main():
    print("\n" + "="*60)
    print("🐦 FLAPPY BIRD Q-LEARNING AI")
    print("="*60)
    print("\nOptions:")
    print("  [T] Train the agent (50,000 episodes)")
    print("  [E] Evaluate trained agent (5 games)")
    print("  [W] Watch agent play continuously")
    print("  [Q] Quit")
    print("="*60)
    
    choice = input("\nYour choice (T/E/W/Q): ").upper().strip()
    
    if choice == 'T':
        confirm = input("\n⚠️ Training will take a long time. Continue? (y/n): ").lower()
        if confirm == 'y':
            train_agent()
        else:
            print("Training cancelled.")
    
    elif choice == 'E':
        num_games = input("How many games to evaluate? (default 5): ").strip()
        try:
            num_games = int(num_games) if num_games else 5
        except:
            num_games = 5
        evaluate_agent(num_games)
    
    elif choice == 'W':
        watch_agent()
    
    elif choice == 'Q':
        print("👋 Goodbye!")
    
    else:
        print("❌ Invalid choice. Please run again and choose T, E, W, or Q.")


if __name__ == "__main__":
    main()