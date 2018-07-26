# The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.
# All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom and
# the smallest one at the top.
# The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:
# •	You can only move one disk at a time.
# •	A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
# •	You cannot place a larger disk on top of a smaller disk.
# Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the rods are
# numbered, with the first rod being 1, the second (auxiliary) rod being 2, and the last (goal) rod being 3.
# For example, with n = 3, we can do this in 7 moves:
# Move 1 to 3
# Move 1 to 2
# Move 3 to 2
# Move 1 to 3
# Move 2 to 1
# Move 2 to 3
# Move 1 to 3

####
# Time tested recursion problem.
# Moving a disc from A to C would require moving all of the discs above it
# from A to B, moving the disc to C and replacing all the discs from B to C.
####
def hanoi(n, A = 0, B = 2):
    C = 3-(A+B)
    ret = []
    if n == 0:
        return ret
    ret.extend(hanoi(n-1, A, C))
    ret.append((n, A, B))
    ret.extend(hanoi(n-1, C, B))
    return ret
####
def format_hanoi(steps):
    for step in steps:
        print("Move {} to {}".format(step[1]+1, step[2]+1))
print(format_hanoi(hanoi(3)))
