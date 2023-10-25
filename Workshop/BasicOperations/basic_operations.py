"""
Arithmetic Operators:
+ (Addition): Adds two numbers.
- (Subtraction): Subtracts the right operand from the left operand.
* (Multiplication): Multiplies two numbers.
/ (Division): Divides the left operand by the right operand (result is a float)
// (Floor Division): Divides the left operand by the right operand
    and returns the largest integer not greater than the result.
% (Modulus): Returns the remainder of the division of the left operand
    by the right operand.
** (Exponentiation): Raises the left operand to the power of the right operand.
"""

# Addition
result_add = 5 + 3  # result_add is 8

# Subtraction
result_sub = 10 - 4  # result_sub is 6

# Multiplication
result_mul = 6 * 7  # result_mul is 42

# Division
result_div = 20 / 5  # result_div is 4.0 (floating-point division)

# Floor Division
result_floor_div = 20 // 3  # result_floor_div is 6 (integer division, rounded down)

# Modulus
result_mod = 17 % 5  # result_mod is 2 (remainder of the division)

# Exponentiation
result_exp = 2 ** 3  # result_exp is 8 (2 raised to the power of 3)

"""
Comperason Operators:
== (Equal): Tests if two values are equal.
!= (Not Equal): Tests if two values are not equal.
< (Less Than): Tests if the left value is less than the right value.
> (Greater Than): Tests if the left value is greater than the right value.
<= (Less Than or Equal To): Tests if the left value is less than or equal to
    the right value.
>= (Greater Than or Equal To): Tests if the left value is greater than or
    equal to the right value.

Note: Comperason Operators will always return a Boolean value (True or False)

"""

# Equal
is_equal = (5 == 5)  # is_equal is True

# Not Equal
is_not_equal = (10 != 5)  # is_not_equal is True

# Less Than
is_less_than = (3 < 5)  # is_less_than is True

# Greater Than
is_greater_than = (7 > 5)  # is_greater_than is True

# Less Than or Equal To
is_less_equal = (4 <= 4)  # is_less_equal is True

# Greater Than or Equal To
is_greater_equal = (8 >= 8)  # is_greater_equal is True

"""
Logical Operators:
and (Logical AND): Returns True if both operands are True.
or (Logical OR): Returns True if at least one operand is True.
not (Logical NOT): Returns the opposite of the operand's value.
"""

# Logical AND
result_and = True and False  # result_and is False

# Logical OR
result_or = True or False  # result_or is True

# Logical NOT
result_not = not True  # result_not is False

"""
Assignment Operators:

= (Assignment): Assigns the value on the right to the variable on the left.
+= (Add and Assign): Adds the value on the right to the variable 
    and assigns the result to the variable.
-= (Subtract and Assign): Subtracts the value on the right from the variable
   and assigns the result to the variable.
*= (Multiply and Assign): Multiplies the variable by the value on the right
    and assigns the result to the variable.
/= (Divide and Assign): Divides the variable by the value on the right
    and assigns the result to the variable.
//= (Floor Divide and Assign): Performs floor division on the variable
    and assigns the result.
%= (Modulus and Assign): Computes the modulus of the variable
    and assigns the result.
**= (Exponentiate and Assign): Raises the variable to the power of the value
    on the right and assigns the result.

"""
# Assignment
x = 10

# Add and Assign
x += 5  # x is now 15

# Subtract and Assign
x -= 3  # x is now 12

# Multiply and Assign
x *= 2  # x is now 24

# Divide and Assign
x /= 4  # x is now 6.0

# Floor Divide and Assign
x //= 2  # x is now 3 (rounded down)

# Modulus and Assign
x %= 2  # x is now 1

# Exponentiate and Assign
x **= 2  # x is now 1 (1 raised to the power of 2)
