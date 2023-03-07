import time


# the function for insertion sort with the list of integer elements as a parameter in non-descending order
# initially the sorted portion of the list is element at index 0 and with every iteration the sorted portion
# expands by 1


def insertion_sort(the_list):
    n = len(the_list)

    if n <= 1:
        return

    start_time = time.time()  # start time of the algorithm

    # starts with the first element as the only sorted element.
    for index in range(1, n):
        # save this value to be positioned
        value = the_list[index]

        # find the position where value fits into the ordered portion of the list
        position = index
        while position > 0 and value < the_list[position - 1]:
            # shift the elements if the condition is true to the right or the unordered portion of the list
            # the while loop stops at index 1
            the_list[position] = the_list[position - 1]
            position -= 1
        # put the saved value into the "hole" created
        the_list[position] = value

    end_time = time.time() - start_time  # end time of the algorithm
    print(end_time)  # just to check the amount of time required
    return the_list


print(insertion_sort(list(range(50000, 0, -1))))

'''
In every scan we begin with an ordered portion of 1 which keeps increasing its size by one.
Hence in the first scan we have just one element in the sorted portion of the list and in the
nth step we have all the n sorted elements

T(n) = 1 + 2 + 3 + ... + (n - 1) = n(n - 1)/2 = O(n^2)

We again consider worst cases where the input list is in descending sorted order.

The first case of 500 elements in sorted descending order produces the ascending sort in 37ms
print(inserion_sort(list(range(500,0,-1))))

The second case of 5000 elements in sorted descending order produces the result in 3.91s
print(inserion_sort(list(range(5000,0,-1))))

The third case of 50000 elements in sorted descending order produces the result in 431.56s
print(inserion_sort(list(range(50000,0,-1))))

In insertion sort if the list is already in sorted non-descending order then the result is pretty much
instantaneous. This happens because the while loop fails as the value to the right is already larger
and hence insertion sort is much faster for already sorted lists than the selection sort.
In selection sort we have to scan for the minima till the end in every iteration.
'''
