import numpy as np
import time

a = np.zeros(4); print(f"a: {a}, type: {type(a)}, shape: {a.shape}, dtype: {a.dtype}")
a = np.zeros((4,)); print(f"a: {a}, type: {type(a)}, shape: {a.shape}, dtype: {a.dtype}")
a = np.random.random_sample(4); print(f"a: {a}, type: {type(a)}, shape: {a.shape}, dtype: {a.dtype}")


