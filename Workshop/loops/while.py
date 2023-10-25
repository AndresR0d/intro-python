"""
While:
A while loop in Python is used to repeatedly execute a block of code as long 
as a specified condition is evaluated as True. 
It continues executing the block of code until the condition becomes False.

1. Condition Evaluation: The loop begins by evaluating the specified condition.
   If the condition is True, the code block associated with the while loop is executed.
   If the condition is False from the start, the loop is skipped entirely.

2. Code Block Execution: The code block within the while loop is executed.
   This block of code can include any valid Python statements and can contain 
   any logic that you want to repeat.

3. Re-evaluation of the Condition: After executing the code block, the condition is re-evaluated.
   If the condition is still True, the loop will repeat, and the code block is executed again.
   This process continues until the condition becomes False.

4. Loop Termination: Once the condition becomes False, the loop terminates,
   and the program continues to execute the code following the while loop.

Explanation:

1. The count variable is initially set to 1.
2. The while loop checks if count is less than or equal to 5.
3. Inside the loop, it prints the value of count and increments it by 1.
4. The loop continues to execute as long as the condition count <= 5 remains True.
"""
# While loop
count = 1
while count <= 5:
    print(count)
    count += 1