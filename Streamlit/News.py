import streamlit as st
import requests

# API KEY
API_Key = "734439f6531842388d83b65653e8f676"

def make_requests(query):
    url = "https://newsapi.org/v2/everything"
    
    # Parameters with API key and query
    params = {
        'q': query,
        'apiKey': API_Key,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 20  # Number of articles to fetch
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()["articles"]
        elif response.status_code == 401:
            st.error("⚠️ API Key is invalid or unauthorized!")
            return None
        else:
            st.error(f"Error fetching news: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {e}")
        return None

def filtered_news():
    st.title("📰 News App by Your Own Choice")
    
    # User input for the search query
    user_query = st.text_input("Enter a topic (e.g., 'Nepal', 'technology'):", "Nepal")

    if user_query:
        # Fetch news based on user's query
        with st.spinner(f"Searching for '{user_query}'..."):
            news_articles = make_requests(user_query)

        if news_articles:
            st.header(f"🔍 Search Results for '{user_query}'")
            st.write(f"Found {len(news_articles)} articles")
            
            # Display each article
            for article in news_articles:
                if article.get('title') and article.get('description'):
                    with st.expander(article['title']):
                        st.write(f"**Source:** {article['source']['name']}")
                        st.write(f"**Published:** {article['publishedAt']}")
                        st.write(article['description'])
                        if article.get('url'):
                            st.markdown(f"[Read full article]({article['url']})")
                        if article.get('urlToImage'):
                            st.image(article['urlToImage'], use_container_width=True)
        elif news_articles is not None:
            st.info("No news found for this query.")
        else:
            st.warning("Please check your API key or try again later.")

if __name__ == "__main__":
    filtered_news()