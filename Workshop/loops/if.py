"""
If statement:
he if statement in Python is a conditional statement that allows you to
execute a block of code if a specified condition is evaluated as True.
It provides a way to control the flow of your program by allowing you to perform
different actions based on whether a condition is met.

Statement explanation:

1. Condition Evaluation: The if statement begins by evaluating the specified condition.
   If the condition is True, the code block associated with the if statement is executed.
   If the condition is False, the code block is skipped.

2. Code Block Execution: If the condition is True, the code block within the if statement is executed.
   This block of code can include any valid Python statements and logic.

3. Optional elif and else Blocks: You can extend the if statement with optional
   elif (short for "else if") and else blocks to handle multiple conditions or
   provide an alternative action when the condition is False.
"""
# If statement
number = 10
if number > 0:
    print("Number is positive")
else:
    print("Number is negative")
