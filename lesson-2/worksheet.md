# Lesson 2 - Bubble Sort

The Bubble Sort algorithm sorts an unordered list by repeatedly stepping through the list and swapping elements if they are in the wrong order.

Give a small list such as:

`[4,3,6,5]`

The algorithm would begin by comparing the first two elements: `4` and `3`. As they are in thr wrong order, they would be swapped, to give:

`[3,4,6,5]`

Next `4` and `6` would be compared. These are in the correct order, so are left alone.
Next `6` and `5` would be compared and swapped to give:

`[3,4,5,6]`

In this example the list is now sorted. If it were not yet sorted the algorithm would start at the beginning again, and keep repeating until the list is completely sorted.
...

## Some useful functions

```python
import matplotlib.pyplot as plt
from random import shuffle

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
	return some_list

def display(some_list):
    plt.clf()
    plt.bar(range(len(some_list)),some_list)
    plt.draw()
    
```
- The first of these functions creates a list of random numbers.
- The second function displays the contents of a list as a barchart.
- Copy the code into a new file called **sorting.py**

## Swapping variables

- Integral to the Bubble Sort algorithm is the ability to swap elements in a list around.
Start by thinking about two variables each with different values. Type the following into a Python interpreter

	```python
	foo = 'first'
	bar = 'second'
	```

- How could these be easily swapped around so that `foo` is equal to `'second'` and `bar` is equal to `' first'`?

- The first way of achieving this is to use a *hold* variable. Try the following in the interpreter:

	```python
	hold = foo
	foo = bar
	bar = hold
	```

- Now type `foo` and `bar` into the interpreter, and you should see that their values have been swapped!

- In Python there is an easier way of swapping variable around. Start again by reassigning `foo` and `bar`

	```python
	foo = 'first'
	bar = 'second'
	```

- Now to swap them around, you only need a single line:

	```python
	foo, bar = bar, foo
	```

- Check the values of `foo` and `bar` in the interpreter now, and wyou should see that they have swapped.

## Swapping elements in a list

- The same process can be used to swap elements in a list.
- Type the following at the bottom of your new file.

	```python
	some_list=[3,2,1]
	```

- To get this list in order, you need to swap some elements around.

    ```python
	some_list = [3,2,1]
	some_list[0], some_list[1] = some_list[1], some_list[0]
	some_list[1], some_list[2] = some_list[2], some_list[1]
	some_list[0], some_list[1] = some_list[1], some_list[0]
	print(some_list)
	```

- You can visualise the whole process by using the display() function.

	```python
	some_list = [3,2,1]
	display(some_list)
	some_list[0], some_list[1] = some_list[1], some_list[0]
	display(some_list)
	some_list[1], some_list[2] = some_list[2], some_list[1]
	display(some_list)
	some_list[0], some_list[1] = some_list[1], some_list[0]
	display(some_list)
	```
	
- If it is a little too fast to see, try adding a `sleep(1)` between each swap (but you'll have to add `from time import sleep` to the top of your file.
	
- Using this method, try and sort the following list and visualise it happening:

  ```python
  [2,1,5,3,]
  ```
- Once you are done, you can delete or *comment* out the code.

## Swapping in a loop.

- You need to automate the comparison of the list elements and their swapping. To begin with you can implement a single pass through the list, swapping pairs of elements if they are in the wrong order.

- Comparing elements in a list is fairly easy. Try the following in the interpreter:

	```python
	i = 0
	some_list = [3,1,4]
	some_list[i] > some_list[i+1]
	```

- This should evaluate to `True` becuase the the 0th element of the list is larger than the first. We can reset `i` and try it again:

	```python
	i = 1
	some_list[i] > some_list[i+1]
	```

- This should evaluate to `False` as the 1st element of the list is not larger than the second.

- You can try this inside a `for` loop so that every pair of elements in the list is considered. Add the following lines to your **sorting.py** file. To start with you can just compare each element with next.

```python
some_list = [6,2,5,1,7,4,9,3]
for i in range(len(some_list)-1):
    if some_list[i] > some_list[i + 1]:
        print(some_list[i],'is greater than',some_list[i+1]
```

- Run your code to see what happens. Can you explain why you only use one less than the length of the list? What would happen if the for loop read `for i in range(len(some_list))`? Try it and see.

-At the moment the loop just compares the elements in the list and tells us if it's bigger. You need it to swap the elements. You can also have a look at what's going on by using the `display()` function

```python
some_list = [6,2,5,1,7,4,9,3]
for i in range(len(some_list)-1):
    if some_list[i] > some_list[i + 1]:
        some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
	    display(some_list)
```

- Run this code, to see the elements being swapped. If you need to slow it down, use a sleep() function again.

- You can try running this on an even longer list, by using the `create_random_list()` function.

```python
some_list = create_random_list(100)
for i in range(len(some_list)-1):
    if some_list[i] > some_list[i + 1]:
        some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
	    display(some_list)

```

- You should see a column moving left to right. If it meets a column that is larger, it stops and the larger column moves along.

## Sorting the list

- Obviously, your list isn't sorted yet. The whole process needs to be repeated multiple times. To do this, you can place the whole loop inside a `while` loop.

```python
some_list = create_random_list(10)
while True:
	for i in range(len(some_list)-1):
		if some_list[i] > some_list[i + 1]:
			some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
			display(some_list)
```

- This sorts the list, but the program never ends. The question is, how can you tell if the list is sorted? The key here is to see if an element in the list has been swapped. If in a single pass, no elements are swapped, then the list must be sorted.

    ```python
    some_list = create_random_list(10)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                display(some_list)
                swapped = True
```

- To finish off, you just need to wrap your sorting algorithm up in a function:

```python
def my_bubble_sort(some_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(some_list)-1):
            if some_list[i] > some_list[i + 1]:
                some_list[i],some_list[i+1] = some_list[i + 1],some_list[i]
                display(some_list)
                swapped = True
    return some_list
```

- You can call the function using the line:

```python
my_bubble_sort(create_random_list(20))
```
