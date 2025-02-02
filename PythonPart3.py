# Creating set 
# use {}  but just store with one item (not key- value pair like dictionary)
# Cannot access with mutable value 
# cannot duplicate data (not the same) 
# unordered data structure
my_set = {'Ki', 'Lu', 'Min', 2, 5}  
print(type(my_set))
print(my_set)      # useful when you want to know types of data

empty_set = {} # cannot write like this (change to dict)
print(type(empty_set))

# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}


# adding
empty_set1 = set()
empty_set1.add(1)
empty_set1.add(2)
empty_set1.add(13)
empty_set1.add(4)
empty_set1.add(5)
print(empty_set1)

# removing 
set_1 = {1,3,2,5,6,7}
print(set_1)
set_1.remove(1)
print(set_1)
set_1.discard(2)
print(set_1)

# union
set_a = {1,2,3,4,5,6,7}
set_b = {1,3,5,7,8,9,}
union_set = set_a.union(set_b)
print(union_set)

# intersection
intersect_set = set_a.intersection(set_b)
print(intersect_set)

# difference
difference_set = set_a.difference(set_b)
print(difference_set)

# Operator precedence
# () , **,  * / , + -



# Input Function
user_input = input("Enter your name : ") 
print(f"Welcome {user_input}")
print(type(user_input))


# Type Conversion
int_value = 45
float_value = float(int_value)   # int to float
print(float_value)

string_value = '124'
float_value1 = float(string_value)  # string to float
print(float_value1)
