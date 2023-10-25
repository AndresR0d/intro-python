"""
Dictionaries:
A dictionary in Python is a versatile and powerful data structure
that allows you to store and organize data in key-value pairs.
It is also known as an associative array or a hash map in 
other programming languages.

Characteristics:

Unordered: Dictionaries are unordered collections of key-value pairs.
This means that the elements in a dictionary are not stored in any specific order,
and you access them by their keys, not by their position.

Mutable: Dictionaries are mutable, which means you can add, modify,
or remove key-value pairs as needed.

Heterogeneous: Dictionaries can store key-value pairs where keys and values
can be of different data types. You can mix integers, strings, floats,
and other data types as keys and values.

Key-Based Access: To access a value in a dictionary, you use the associated key as the index.
Keys are unique within a dictionary.

Dynamic: Dictionaries can grow or shrink in size as you add or remove key-value pairs.

"""

# Creating a Dictionary
pokemon = {
    "name": "Pikachu",
    "type": "Electric",
    "region": "Kanto"
}

print(pokemon)
print(pokemon["type"])

# Change value given a key
pokemon["name"] = "Jigglypuff"
print(pokemon)

print(pokemon.get("name"))
