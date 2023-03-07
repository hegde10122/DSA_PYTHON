import time

start_time = time.time()


def recursive_fib(n):
    if n < 0:
        print('Negative numbers are not allowed in fibonacci sequence')
        return

    if n == 0 or n == 1:
        value = n
    else:
        value = recursive_fib(n - 1) + recursive_fib(n - 2)  # recursive call with previous two numbers in sequence
    return value


val = recursive_fib(66)
elapsed_time = time.time() - start_time
print('elapsed time is ', elapsed_time)
print(val)

'''
Uncomment the lines below to see the working of the functions
val = recursive_fib(45)
elapsed_time = time.time() - start_time
print(elapsed_time)
print(val)

Explanation:
the recursive fibonacci involves a lot of wasteful computation wherein the factorial of already calculated
intermediate subproblems are recalculated as the fibonacci calculations resemble a tree

recursive_fib(35) takes around 7.5 secs (approx) to return the value 9227465
Complexity : O(2^n)
'''


def iter_fib(n):
    if n < 0:
        print('Negative numbers are not allowed in fibonacci sequence')
        return

    if n == 0 or n == 1:
        return n
    else:
        x1 = 0
        x2 = 1
        for i in range(2, n + 1):  # range function begins at k and ends at j-1 for range(k,j)
            x3 = x1 + x2  # calculate by adding the previous two numbers
            x1 = x2  # reassign second as first for new calculation
            x2 = x3  # reassign newly calculated value as the second value for next iterative calculation
    return x2


'''
Uncomment the lines below to see the working of the functions
val = iter_fib(35)
elapsed_time = time.time() - start_time
print(elapsed_time)
print(val)

Explanation:
the iterative fibonacci requires O(n) space and time Big-Omega(n^n)

recursive_fib(35) returns the value 9227465 instantaneously
Complexity : O(n)
'''

# better way than the iterative version
_lookup = {0: 0, 1: 1}  # lookup table or a dictionary of already calculated values pre-defined with the two base cases


def memoized_fib(n):
    if n < 0:
        print('Negative numbers are not allowed in fibonacci sequence')
        return

    if n in _lookup:
        return _lookup[n]
    else:
        value = memoized_fib(n - 1) + memoized_fib(n - 2)
    _lookup[n] = value
    return value


'''
Uncomment the lines below to see the working of the functions
val = memoized_fib(95)
elapsed_time = time.time() - start_time
print(elapsed_time)
print(val)

Explanation:
the memoized fibonacci uses the lookup table or dictionary to store the values of subproblems
This requires O(n) time

memoized_fib(35) returns the value 9227465 instantaneously
Complexity : O(n)
'''
