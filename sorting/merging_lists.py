# merging sorted lists

'''
combine two sorted lists A and B into C
If A is empty, copy B into C
If B is empty, copy A into C
Otherwise, compare first element of A and B and move the smaller of the two into C
Repeat until all the elements in A and B have been moved
'''


def merge_lists(A, B): # A[0:m] B[0:n]

    # initialise the new list C and get the lengths of the two lists into variables m and n
    (C, m, n) = (list(), len(A), len(B))

    # current positions of A and B
    (i, j) = (0, 0) # initialise the two indices to be used in the while loop below

    while i + j < m + n: # i+j is the number of elements so far merged
        if i == m:  # Case 1: A is exhausted or A is empty, Append B if size of B is greater than A
            C.append(B[j])
            j += 1
        elif j == n:  # Case 2: B is exhausted or B is empty, Append A if size of A is greater than B
            C.append(A[i])
            i += 1
        elif A[i] <= B[j]:  # Case 3: Element of A is smaller
            C.append(A[i])
            i += 1
        elif A[i] > B[j]:  # Case $: Element of A is larger (B is smaller)
            C.append(B[j])
            j += 1
    return C


'''
How much time does merge take?

merge A of size m, B of size n into C
In each iteration, we add one element to C
Size of C is m + n
m + n <= 2.max(m,n)
Hence O(max(m,n)) = O(n) if m == n
'''


