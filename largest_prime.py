#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from fibonnaci import generate_fibonacci

### function to check if a number is prime ###
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


### function to find largest prime Fibonacci number less than specified limit ###
def largest_prime_fibonacci(limit):
    fibonacci_nums = generate_fibonacci(limit)
    
    prime_fibonacci_nums = [num for num in fibonacci_nums if is_prime(num)]
    
    if prime_fibonacci_nums:
        return max(prime_fibonacci_nums)
    else:
        return None


if __name__ == "__main__":
    # setting up command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('limit', type=int, help="Upper limit for Fibonacci numbers")
    
    args = parser.parse_args()
    
    output_num = largest_prime_fibonacci(args.limit)
    
    print(output_num)

# largest prime fibonacci number less than 50000 is 28657