"""
Function:

A function is a self-contained, reusable block of code
that performs a specific task or set of tasks.

Steps for creating a function:

1. Function Definition: To create a function, you need to define it using the def keyword,
   followed by the function name and a set of parentheses. You can also include parameters inside
   the parentheses if the function requires inputs.

2. Function Call: To execute a function, you call it by using its name followed by parentheses. 
   If the function requires parameters, you provide them within the parentheses.

3. Parameters and Arguments: Parameters are placeholders for the values that a function needs
   to perform its task, while arguments are the actual values that are passed to the function
   when it's called. They allow you to customize the behavior of a function.

4. Return Statement: Functions can optionally return a value using the return statement.
   This allows you to obtain the result of a function's computation and use it in other 
   parts of your code.

"""


def sum_of_two_numbers(number1, number2):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    number1 (int or float): The first number.
    number2 (int or float): The second number.

    Returns:
    int or float: The sum of the two input numbers.
    """
    print(number1+number2)


def greet_person(name, message):
    print("Hello "+ name + "," + message)

def say_age(age):
    pass

# greet_person("Andres", "How are you doing today?")
# say_age(22)
# sum_of_two_numbers(2, 3)
