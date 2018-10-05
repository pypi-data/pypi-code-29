import numpy as np
x=np.random.normal(size=25)
y=np.random.normal(size=25)
z = np.vstack((x, y))
c = np.cov(z)

print(z)
print(c)
