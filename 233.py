# This problem was asked by Apple.
# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, 
# using only O(1) space.
####
def fib(n):
    a = 1
    b = 1
    while n:
        a, b = b, a + b
        n -= 1
    return b
####
print(fib(6))