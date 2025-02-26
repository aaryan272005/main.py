'''Methods of tuple'''
# 1. count(value):
# Returns the number of occurrences of the specified value in the tuple.
# Example:
my_tuple = (1, 2, 3, 1, 4, 1)
print(my_tuple.count(1))  # Output: 3

# 2. index(value, start, end):

# Returns the index of the first occurrence of the specified value in the tuple. You can also specify a start and end index to limit the search.
# Example:

print(my_tuple.index(3))  # Output: 2


'''Orentation with tuple'''
#1. Concatenation: You can combine tuples using the + operator.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # Output: (1, 2, 3, 4, 5, 6)

#2. Repetition: You can repeat a tuple by using the * operator.

my_tuple = (1, 2)
repeated = my_tuple * 3
print(repeated)  # Output: (1, 2, 1, 2, 1, 2)

#3. Membership Test: You can check if a value is present in a tuple using the in operator.

my_tuple = (1, 2, 3, 4)
print(2 in my_tuple)  # Output: True

#4. Indexing and Slicing: You can access individual elements or slices of the tuple.

my_tuple = (10, 20, 30, 40)
print(my_tuple[1])  # Output: 20
print(my_tuple[1:3])  # Output: (20, 30)

