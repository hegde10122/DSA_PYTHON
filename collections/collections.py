a_string = "The doctor is here."
b_string = "You eat apples today."

print(a_string + b_string)
print(a_string[6])
print(a_string[-7])
print(type(b_string))

x_list = ['S', 'A', "XYZ", 1, 4, 7.8]
print(x_list)

print(type(x_list))

x_list.append('Q')  # adding a new element to the end of the list
print(x_list)

print("The first element is", x_list[0])
print("The second element is", x_list[1])
print("The last element is", x_list[-1])
print("The second to last item is", x_list[-2])

x_list[2] = 'inflation'
x_list[3] = 'd'
x_list[4] = 82
x_list[-2] = "second"

print(x_list)

tups = (10, 2, "tuples country", 99.77, 'inflation')

print(type(tups))
print(tups)
print(tups[-3])

# tups.append("truth")

a_string.append("funding")