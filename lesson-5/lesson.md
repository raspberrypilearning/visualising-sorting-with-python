# Visualising Sorting With Python 5 - Recursion

In this lesson, students will look at some classical solutions to various mathematical problems that utilise recursion.

## Learning objectives

- To understand what is meant by the term 'recursion'
- To be able to implement some simple recursive algorithms in Python

## Learning outcomes

### All students are able to

- Describe what is meant by recursion

### Most students are able to

- Implement recursive solutions to finding factorials and gcd

### Some students are able to

- Implement recursive solutions to detecting palindromes and creating a Fibonacci sequence

## Lesson summary

- Students are provided with a gentle introduction to recursion, by using recursive algorithms to find factorials of a number and the gcd of two numbers.
- Students can attempt to independently create recursive functions in Python, to detect palindromes and create the Fibonacci sequence.

## Starter

- Either show your students this animation, or run the code below:

![tree](images/tree.gif)

```python
import turtle
t = turtle.Turtle()
win = turtle.Screen()

t.pu()
t.bk(300)
t.pd()

def tree(length,t):
	if length < 5:
		return None
	else:
		t.forward(length)
		t.right(60)
		tree(length-30,t)
		t.left(120)
		tree(length-30,t)
		t.right(60)
		t.backward(length)

tree(180,t)
```

- Have the students try and explain what the turtle is doing as it draws out the tree.
- Ask them how they might go about coding the turtle to draw the tree.
- Try to get them to recognise the smallest part of the algorithm.

## Main development

- Students can work through the worksheet on recursion.
- They should have no issues with the first few tasks, but may need support later on.

### Solutions

**Co-primes**

```python
def gcd(a,b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)

# Function using list comprehensions
def coprimes(c):
	values = [i for i in range(1,c) if gcd(c,i) == 1]
	return values

# Function without list comprehensions
def coprimes(c):
	values = []
	for i in range(1,c):
		if gcd(c,i) == 1:
			values.append(i)
	return values


results = coprimes(63)
```

**Palindrome**

```python
def find_palindrome(word):
	if len(word) <= 1:
		return True
	elif word[0] == word[-1]:
		return find_palindrome(word[1:-1])
	else:
		return False

if find_palindrome('abcdefedcba'):
	print('Yep')

```

**Fibonacci**

```python
def fib(n):
   if n == 1:
	  return 1
   elif n == 0:
	  return 0
   else:
	  return fib(n-1) + fib(n-2)

print(fib(20))
```

## Plenary

- Show the students the tree code from the starter:

```python
import turtle
t = turtle.Turtle()
win = turtle.Screen()

t.pu()
t.bk(300)
t.pd()

def tree(length,t):
	if length < 5:
		return None
	else:
		t.forward(length)
		t.right(60)
		tree(length-30,t)
		t.left(120)
		tree(length-30,t)
		t.right(60)
		t.backward(length)

tree(180,t)
```

Ask them to identify the recursive calls and the base case of the function.

## Extension

- Students can try to write their own recursive function to draw something with a turtle, such as a spiral.
