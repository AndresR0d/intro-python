"""
Tuples:
A tuple in Python is a data structure that is similar to a list but with a key difference:
tuples are immutable, which means their elements cannot be modified or changed after creation.
Tuples are often used to represent collections of items that should not be altered

Characteristics:

Ordered: Like lists, tuples maintain the order of their elements.
You can access elements by their position (index) in the tuple.

Immutable: Once you create a tuple, you cannot add, remove, or change its elements.
Tuples provide data integrity by ensuring that the elements remain constant.

Heterogeneous: Tuples can store elements of different data types, just like lists.

Hashable: Tuples are hashable, which means they can be used as keys in dictionaries, unlike lists.

"""
# Creatiing a tupleç

my_tuple = (1, 2, "Pikachu", 2.5)
print(my_tuple)

# Returns index of given value
print(my_tuple.index("Pikachu"))
