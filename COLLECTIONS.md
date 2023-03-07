# COLLECTIONS in Python

# STRING
String is a sequence of characters which is used to store text values.

a_string = "The doctor is here."
b_string = "You eat apples today."

The variable a_string and b_string are both strings.

print(a_string+b_string)

The above print statement concatenates both the strings using the plus sign and produces a new string
"The doctor is here.You eat apples today."

We can access individual characters in a string using square brackets and an index. 

For example 
print(a_string[6]) produces the result "c". 

The start index for a string is 0.
Negative indices count backwards from the end of the string.

For example
print(a_string[-7]) produces the result "s". 

The name of the class for strings is str.

For example
print(type(b_string)) produces the result <class 'str'>

# LIST


A python list is an ordered sequence of objects (elements). The objects may not be of the
same type. 

For example

x_list = ['S', 'A', 'XYZ', 1, 4, 7.8]

This is a python list having the first three elements as strings. The next two objects are integers while the final object is a floating-point 
number.

Just like a string, we can access each object using the index.

For example
print(x_list[3]) produces the result 1. The starting index is 0 for a python list.

print(type(x_list)) produces the result <class 'list'>

We can append a new element at the end of the list using the keyword append.

For example
x_list.append('Q')
print(x_list)

Accessing the elements of list using indices.
For example

print("The first element is", x_list[0])
print("The second element is", x_list[1])
print("The last element is", x_list[-1])
print("The second to last item is", x_list[-2])

Negative indices count backwards from the end of the list just like a string.

We can also overwrite values in a list using assignment statements.

For example

x_list[2] = 'inflation'
x_list[3] = 'd'
x_list[4] = 82
x_list[-2] = "second"

print(x_list)

# TUPLE

Tuple is an ordered sequence of objects, but unlike lists, they are
immutable. We can access the items but can't change what elements are
in the tuple after it is created. For example, trying to append element to a tuple raises an
exception.

For example,

tups = (10, 2, "tuples country", 99.77, 'inflation')

print(type(tups))  produces the result <class 'tuple'>
print(tups) 
print(tups[-3]) produces the result "tuples country"

tups.append("truth") produces the exception
AttributeError: 'tuple' object has no attribute 'append'

tups[3] = "hatred"

If we try to replace an element in a tuple then it produces the exception below
TypeError: 'tuple' object does not support item assignment

Note: Strings like tuples are also immutable

So append and replace operations do not work and produce exceptions.

