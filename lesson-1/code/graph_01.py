import matplotlib.pyplot as plt

y = [i for i in range(-100,100,20)]
x = [i for i in range(len(y))]


plt.plot(x,y)
plt.scatter(x,y)
plt.draw()
