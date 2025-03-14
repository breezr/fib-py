import argparse
from fib_py.fib_calcs.fib_number import recurring_fibonacci_number

def fib_number() -> None:
    parser = argparse.ArgumentParser(
        description='Calculate the nth Fibonacci number')
    parser.add_argument(
        '-n',
        '--number',
        type=int, 
        help='The nth Fibonacci number to calculate')
    args = parser.parse_args()
    print(f"The Fibonacci number is: {recurring_fibonacci_number(number=args.n)}")
