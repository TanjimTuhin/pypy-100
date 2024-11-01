import array

# Creating an array of integers
#my_array = array.array('i', [1, 2, 3, 4])
my_array = array.array(int(input()))

# Accessing elements
print(my_array[1])  # Output: 2

# Modifying the array
my_array.append(5)
print(my_array)  # Output: array('i', [1, 2, 3, 4, 5])
