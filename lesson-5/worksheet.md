# Visualising Sorting With Python 5 - Recursion

Before you learn the final sorting algorithm, you should learn about a powerful concept in computer science called **recursion**.

## Finding factorials

You can start with a very simple algorithm. Imagine you wanted to find the **factorial** of the number 10, which is the result of multiplying 10*9*8*7*6*5*4*3*2*1 = 3628800. You could solve this by using a simple loop, but with recursion you break the problem down into smaller problems of the same type, and then apply your general solution.

Another way of rephrasing the problem 'find the factorial of 10' is to say 'find the factorial of 9 and multiply it by 10, or even 'find the factorial of the number (10-1) and multiply it by 10'. Of course, we now have a new problem of 'find the factorial of (10-1)', but we can solve this in the same way. We can just find the factorial of 8 multiplied by 9, and then multiply it by 10. We can keep going in this manner until we end up trying to find the factorial of 1. At this point, we'd want our algorithm to stop. This is called the **base case**.

You can write this in code as follows:

	```python
	def factorial(n):			            # Find the factorial of a number n
		if n == 1:				            # Base case - if the number is 1    
			return 1                        # Factorial of 1 is one, so return it
		else:                               # If the number is greater than 1
			return n * factorial(n-1)       # Multiply the number by the factorial of the next number down

	print(factorial(10))                    # Find and print the factorial of 10
	```

Run the code and you should see the answer displayed.

To see what's going on with the algorithm, a few `print` statements might help:

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

Another algorithm that uses recursion is one to find the *greatest common divisor*. This algorithm was actually invented around 300BC by a Greek mathematician called Euclid.

Imagine you have two numbers, and you want to find a the largest number that can divide into them exactly, such as 100 and 46. If the smaller number divides exactly into the larger number, then the small number is the greatest common divisor. This is your *base case*. If it doesn't, then you can find the remainder of the division. In Python you can use the modulo operator (`%`) to find the remainder of a division:

	```python
	100 % 46
	```

Type this into your interpreter, and you should see the answer is `8`. You can now find the remainder of dividing `46` by `8`:

	```python
	46 % 8
	```

This gives the answer `6`. Once again, you can find a remainder:

	```python
	8 % 6
	```

Now you have the answer `2`:

	```python
	6 % 2
	```

This gives the answer `0`, so `2` must divide into `6` exactly. The *base case* has been reached and you can state that `2` is the *greatest common divisor* of `100` and `46`.

You can see that the same calculation has been performed multiple times, using the result of the previous calculation. This problem is therefore a perfect candidate to be solved with recursion:

	```python
	def gcd(a,b):
		if a % b == 0:
			return b
		else:
			return gcd(b, a % b)
	```

This algorithm is extremely important in cryptography, where it is often necessary to find two numbers that are *co-prime*, two numbers whose *greatest common divisor* is 1:

	```python
	gcd(1022,2011)
	```

Can you use your `gcd()` function to create an algorithm that will count the number of co-primes any number has? How many co-primes does the number `63` have? 

## Is it a palindrome?

A palindrome is a word that reads the same forwards as it does backwards. For example, the word `hannah` is a palindrome.

Checking if a word is a palindrome or not is a simple enough process. You check if the first and last letters are the same, and if they are you can remove them and then check the first and last letters again, and so on. If the word has 1 or fewer characters, then it is a palindrome. Can you see an opportunity for recursion here?

See if you can write a recursive algorithm to tell if a string is a palindrome or not.

Here's some pseudocode to try and help you along:

	```
	function find_palindrome(word)
	if the length of the word is 1 or 0, then it's a palindrome
	if the first and last letters are the same, then find_palindrome(word with first and last letters removed)
	otherwise the word is not a palindrome
	```

And here's some helpful code that you might need:

	```python
	'my string'[0] # the first character of the string
	'my string'[-1] # the last character of the string
	'my string'[1:-1] # the string with the first and last characters removed 
	```

## The Fibonacci sequence

The Fibonacci sequence is found by starting with `1, 1` and then adding the last number to the number preceding it in the sequence:

	```
	1, 1, 2, 3, 5, 8, 13, 21...
	```

Imagine you wanted to find the `n`th Fibonacci number. How could this be done?

Hopefully, you are beginning to see that there is a recursive solution to this. All you need to do is find the `n-1`th Fibonacci number and add it to the `n-2`th Fibonacci number, and that will give you the `n`th.

Have a go at writing a recursive algorithm to find the `n`th Fibonacci number. You can test your algorithm using the values provided below:

	```
	The 10th Fibonacci number is 55
	The 2nd Fibonacci number is 1
	The 20th Fibonacci number is 6765
	```

Be warned: recursive solutions aren't always the best solutions. Trying too large a number with this algorithm may well take a significant amount of time.

