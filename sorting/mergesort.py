import time
from merging_lists import *

# takes in a list or array of integers as the input parameter
# uses the divide and conquer strategy
# solve each part seperately
# combine the solutions efficiently

'''
To sort A[0:n] into B[0:n]
If n is 1, nothing to be done
Otherwise,
Sort A[0:n//2] into L(left)
Sort A[n//2:n] into R(right)
Merge L and R into B
'''


def mergesort(the_list,left,right):

    if right - left <= 1:  # base case
        return the_list[left:right]

    if right - left > 1:  # recursive call
        mid = (left + right) // 2

        L = mergesort(the_list,left,mid)
        R = mergesort(the_list,mid,right)

    return merge_lists(L,R)


def mergesort1(the_list): # wrapper function that get the list from the user
    # Sort the_list provided as the input parameter

    if len(the_list) <= 1:
       return the_list

    # call the main mergesort function with the leftmost and rightmost indices
    return mergesort(the_list, 0, len(the_list))

start_time = time.time()
print(mergesort1(list(range(5000000, 0, -1))))
print(time.time() - start_time)

'''
Case 1: print(mergesort1(list(range(500, 0, -1))))
500 numbers in descending order are now sorted in ascending order
time taken is 3ms

Case 2: print(mergesort1(list(range(5000, 0, -1))))
5000 numbers in descending order are now sorted in ascending order
time taken is 45ms

Case 3: print(mergesort1(list(range(50000, 0, -1))))
50000 numbers in descending order are now sorted in ascending order
time taken is 458ms

Case 4: print(mergesort1(list(range(500000, 0, -1))))
500000 numbers in descending order are now sorted in ascending order
time taken is 5.47s

The data handled is much more than insertion or selection sort.

We are making 19 recursive calls that equal log(500000) = 19

Case 5: print(mergesort1(list(range(5000000, 0, -1))))
5000000 numbers in descending order are now sorted in ascending order
time taken is 67.19s


'''
