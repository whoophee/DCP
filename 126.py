# This problem was asked by Facebook.
# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
# Try solving this without creating a copy of the list. How many swap or moveoperations do you need?
####
# This is a pretty straightforward problem imo. Just swap out elements to the right position until the array is complete.

# Function to rotate list in-place.
def rotate_list(input_list, k):

    input_len = len(l)
    temp_val = None

    # input_len + 1 is the number of swaps required to rotate the list.
    for i in range(input_len + 1):
        # New index
        new_index = (k + i) % input_len
        # Swap most recently swapped out element to required position
        temp_val, input_list[new_index] = input_list[new_index], temp_val
