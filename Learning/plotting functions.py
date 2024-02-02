import numpy as np
import matplotlib.pyplot as plt
N = 1000
x = np.linspace(-1,100,N,endpoint=False)

# exponential
plt.xlim(-2,60)
plt.ylim(-5,20)
plt.plot(np.exp(x))
plt.ylabel('Y')
plt.xlabel("x")

# logarithm
plt.plot(np.log(x))
plt.ylabel('Y')
plt.xlabel("x")
plt.show()
N = 8
y = np.zeros(N)
