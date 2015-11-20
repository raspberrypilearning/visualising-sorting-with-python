# Lesson 5 - Recursion

Before you learn the final sorting algorithm you're going to have to learn about a powerful concept in Computer Science called **Recursion**.

## Finding Factorials

You can start with a very simple algorithm. Imagine you wanted to *Find the factorial of the number 10*. That is the result of multiplying 10*9*8*7*6*5*4*3*2*1 = 3628800

You could solve this by using a simple loop, but with *recursion* you break the problem down into smaller problems of the same type and then apply your general solution.

Another way of rephrasing the problem *Find the factorial of 10* is to say, *Find the factorial of the 9, and multiply it by 10.* Or even, *Find the factorial of the number (10-1) and multiply it by 10*

Of course, we now have a new problem of *Find the factorial of (10-1)*, but we can solve this in the same way. We can just *Find the factorial of 8 multiply 9 and then multiply it by 10*

We can keep going in this manner until we end up with trying to find the factorial of 1. At this point, we'd want our algorithm stop. This is called the **base case**

You can write this in code as follows.

```python
def factorial(n):			            ### Find the factorial of a number n
    if n == 1:				            ### Base case - if the number is 1    
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

Another algorithm that uses recursion is one to find the *Greatest Common Divisor*. This algorithm was actually invented around 300BC by a Greek mathematician called Euclid.

Imagine you have two numbers, and you want to find a the largest number that can divide into them exactly, say 100 and 46.

If the smaller number divides exactly into the larger number, then the small number is the Greatest Common Divisor. This is your *base case*. If it doesn't then you can find the remainder of the division. In Python you can use the modulo operator (`%`) to find the remainder of a division.

```python
100 % 46
```

Type this into your interpreter, and you should see the answer is `8`. You can now find the remainder of dividing `46` by `8`

```python
46 % 8
```

This gives the answer `6`. Once again you can find a remainder.

```python
8 % 6
```

Now you have the answer `2`

```python
6 % 2
```

This gives the answer `0`, so `2` must divide into `6` exactly. The *base case* has been reached and you can state that `2` is the *Greatest Common Divisor* of `100` and `46`.

Hopefully you can see that the same calculation has been performed multiple times, using the result of the previous calculation. This problem is therefore a perfect candidate to be solved with recursion.

```python
def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
```

This algorithm is extremely important in cryptography, where it is often necessary to find two numbers that are *co-prime*. That is, two numbers whose *Greatest Common Divisor* is 1.

```python
gcd(1022,2011)
```

Can you use you `gcd()` function to create an algorithm that will count the number of co-primes any number has? How many co-primes does the number `63` have? 

## Is it a palindrome?

A Palindrome is a word that reads the same forwards as it does backwards. The word `hannah` is therefore a palindrome.

Checking if a word is a palindrome or not is a simple enough process. You check if the first and last letters are the same, and if they are you can remove them and then check the first and last letters again, and so on. If the word has 1 or fewer characters, then it is a palindrome. Can you see an opportunity for recursion here?

See if you can write a recursive algorithm to tell if a string is a palindrome or not.

Here's some structured English to try and help you along:

```
function find_palindrome(word)
if the length of the word is 1 or 0, then it's a palindrome
if the first and last letters are the same, then find_palindrome(word with first and last letters removed)
otherwise the word is not a palindrome
```

And here's some helpful code that you might need:

```python
'my string'[0] ## the first character of the string
'my string'[-1] ## the last character of the string
'my string'[1:-1] ## the string with the first and last characters sliced off 
```

## The Fibonnaci sequence.

The Fibonnaci sequence is found by starting with `1, 1` and then adding the last number to the number preceding it in the sequence.

```
1, 1, 2, 3, 5, 8, 13, 21...
```

Imagine you wanted to find the `n`th fibonnaci number. How could this be done?

Hopefully you are beginning to see that there is a recursive solution to this. ALl you need to do is find the `n-1`th Fibonnaci number and add it to the `n-2`th Fibonnaci number, and that will give you the `n`th.

Have a go at writing a recursive algorithm to find the `n`th Fibonnaci number. You can test your algorithm using the values provided below.

```
The 10th Fibonnaci number is 55
The 2nd Fibonnaci number is 1
The 20th Fibonnaci number is 6765
```

Bewarned - recursive solutions aren't always the best solutions. Trying too large a number with this algorithm may well take a significant amount of time.

