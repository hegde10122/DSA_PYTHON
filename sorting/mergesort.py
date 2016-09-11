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

Analysis of merge sort

T(n): time taken by merge sort on input of size n
Assume that n = 2^k for simplicity

T(n) = 2T(n/2) + n (the initial list of size n is broken into 2 parts of size n/2 each while n is the merge component added)
Two subproblems of size n/2
merging solutions requires time O(n/2 + n/2) = O(n)

Solve the recurrence by unwinding
T(1) = 1
T(n) = 2T(n/2) + n
     = 2[2(T(n/4) + n/2)] + n
     = 2^2T(n/2^2) + 2n
     = 2^2[2T(n/2^3) + n/2^2] + 2n
     = 2^3T(n/2^3) + 3n
     = 2^iT(n/2^i) + in  where i = log n (to the base 2)

     When i = log n, n/2^i = 1, T(n/2^i) = 1
So, T(n) = 2^log n + n.log n = n + nlog n = O(n.log n)
'''
