import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

y = [i for i in range(100)]
shuffle(data)
x = range(len(y))
plt.ion()

for i in range(50):
    plt.clf()
    plt.plot(x,y, '-o')
    plt.draw()
    sleep(0.05)
    shuffle(y)


