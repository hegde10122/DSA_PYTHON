import time

def selection_sort(the_list):
    n = len(the_list)

    if n <= 1:
        return

    start_time = time.time()
    for i in range(n - 1):
        min_position = i  # assume that the ith element is the smallest

        # determine from the next index of current i and scan till the end if we can find smaller value
        for j in range(i+1, n):
            if the_list[j] < the_list[min_position]:  # current minimum is now larger than the element at j index
                min_position = j # new minimum index
        # swap the two elements after the inner for loop exits --- swapping using the pair notation
        (the_list[i], the_list[min_position]) = (the_list[min_position], the_list[i])

    end_time = time.time() - start_time
    print(end_time)
    return the_list

print(selection_sort(list(range(50000, 0, -1))))
'''
Analysis of selection sort

Finding minimum in a list of size n elements requires one entire scan of steps n, to begin with.
In each iteration the length of the segment to be scanned reduces by 1

T(n) = n + (n - 1) + (n - 2) + (n - 3) + ...+ 2 + 1 = n (n + 1)/2 = O(n^2)

We are considering 3 cases :
The first one is the range of numbers from 500 to 1 in descending order
print(selection_sort(list(range(500, 0, -1))))
The time taken is around 18ms.

The second case is the range of numbers from 5000 to 1 in descending order
print(selection_sort(list(range(5000, 0, -1))))
The time taken is around 1.79s

The 3rd case is the range of numbers from 50000 to 1 in descending order
print(selection_sort(list(range(50000, 0, -1))))
The time taken is around 207.2s

As the size of the list increases the performance of selection sort goes down drastically.
'''





