#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def generate_fibonacci(limit):
    fibonacci_nums = []
    a = 0
    b = 1
    
	# generating sequence
    while a < limit: 
        fibonacci_nums.append(a)
        a, b = b, a + b
    
    return fibonacci_nums

#generate_fibonacci(100)
if __name__ == "__main__":
    # setting up command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('limit', type=int, help="Upper limit for Fibonacci numbers")
    parser.add_argument('output_file', type=str, help="File to write to")
    
    args = parser.parse_args()
    
	# writing to file
    try:
        output_seq = generate_fibonacci(args.limit)
        
        with open(args.output_file, 'w') as file:
            file.write('\n'.join(str(i) for i in output_seq))
        print(f"Fibonacci sequence successfully written to {args.output_file}.")
            
    except IOError as e:
        print(f"Error occured while writing to {args.output_file}: {e}.")
    