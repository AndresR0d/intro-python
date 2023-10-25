"""
For loop:
Is used to iterate over a sequence or an iterable object, executing a block of code
for each item in the sequence. For loops are particularly useful when you want to perform
an operation a specific number of times or when you need to work with each element in a 
collection like a list, tuple, string, or dictionary.

1. Iteration: The for loop begins by iterating over the elements of the iterable one by one.
The variable takes on the value of each element in the sequence during each iteration.

2. Code Block Execution: For each iteration, the code block associated with the for loop is executed.
   This block of code can include any valid Python statements and can contain any logic
   that you want to apply to each element of the iterable.

3. Iteration Completion: After the code block is executed for all elements in the iterable,
   the loop terminates, and the program continues executing the code after the for loop.

Loop Explanation:

1. The for loop iterates over the elements of the fruits list,
   with fruit taking on the value of each element (e.g., "apple," "banana," and "cherry").
2. Inside the loop, it prints a message for each fruit,
   incorporating the value of the fruit variable.
3. The loop terminates after all elements in the list have been processed.
"""
# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)


# For loop with string
text = "Hello everyone!"
for letter in text:
    print(letter)


# For loop with dictionary
vocals = {"a": 1, "e": 2, "i":3, "o": 4, "u": 5}
for k,v in vocals.items():
    print(k,v)
print("End")

# For loop with continue statement
list_of_strings = ["a", "b", "c"]
for elem in list_of_strings:
    if elem=="b":
        continue
    print(elem)
print("End")

