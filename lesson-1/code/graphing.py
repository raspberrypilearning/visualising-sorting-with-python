import matplotlib.pyplot as plt
from time import sleep
from random import shuffle


plt.ion()

y = [i for i in range(100)]
x = [i for i in range(len(y))]

for i in range(50):       ## Do the following 50 times
    plt.clf()             ## Clear the plot
    plt.bar(x,y)          ## Plot a bar chart
    plt.draw()            ## Draw the bar chart
    sleep(0.5)            ## Pause for 1/2 a second
    shuffle(y)            ## Shuffle the data
    plt.savefig('foo%s.png' %i)
