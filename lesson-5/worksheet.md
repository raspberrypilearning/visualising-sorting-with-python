# Lesson 5 - Recursion

Before you learn the final sorting algorithm you're going to have to learn about a powerful concept in Computer Science called **Recursion**

## Finding Factorials

You can start with a very simple algorithm. Imagine you wanted to *Find the factorial of the number 10*. That is the result of multiplying 10*9*8*7*6*5*4*3*2*1 = 3628800

You could solve this by using a simple loop. With *recursion* you break the problem down into smaller problems of the same type. Another way of rephrasing the problem *Find the factorial of 10* is to say, *Find the factorial of the number 9, and multiply it by 10.* Or even, *Find the factorial of the number (10-1) and multiply it by 10*

Of course, we now have a new problem of *Find the factorial of (10-1)*, but we can solve this in the same way. We can just *Find the factorial of ((10-1)-1)*

We can keep going in this manner until we end up with trying to find the factorial of 1. At this point, we'd want our algorithm stop. This is called the **base case**

You can write this in code as follows.

```python
def factorial(n):			### Find the factorial of a number n
    if n == 1:				### Base case - if the number is 1    
        return 1                        ### Factorial of 1 is one, so return it
    else:                               ### If the number is greater than 1
        return n * factorial(n-1)       ### Multiply the number by the factorial of the next number down

print(factorial(10))                    ### Find and print the factorial of 10
```

Run the code and you should see the answer displayed.

To see what is going on with the algorithm, a few print statements might help.

```python
def factorial(n):
    print("Finding the factorial of",n)
    if n == 1:
        print(n)
        return 1
    else:
        answer = n * factorial(n-1)
        print("The answer is",answer)
        return answer

print(factorial(10))
```

When you run this you should notice that no actual answer is provided until the *base case* has been reached. All the other function calls are saved in something called the *call stack*. Once the base case has been found, the answer trickles back up the *call stack* until the final answer is reached.

## Finding the largest common divisor

Another algorithm that uses recursion is one to find the *Greatest Common Divisor*. This algorithm was actuall invented around 300BC by a greek mathematician called Euclid.

Imagine you have two numbers, and you want to find a the largest number that can divide into them exactly, say 100 and 46.

If the smaller number divides exactly into the larger number, then the small number is the Greatest Common Divisor. This is your *base case*. If it doesn't then you can find the remainder of the division.

This remainder 
100 % 46 == 8
46 % 8 == 6
8 % 6 == 2
6 % 2 == 0
