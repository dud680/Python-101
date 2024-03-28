"""
Module to demonstrate primitive data types in Python.

This module provides examples of primitive data types
in Python, including:
- Booleans
- Integers
- Floats
- Strings

What is a primitive data type?

A primitive data type is a basic data type that is
provided by a programming language. These data types
are used to represent simple values, such as numbers
or text. In Python, there are several primitive data
types that are commonly used in programming.

Booleans:

A boolean is a data type that represents one of two
values: True or False. Booleans are used to represent
logical values in programming, such as whether a
condition is true or false.

Integers:

An integer is a data type that represents whole numbers,
both positive and negative. Integers can be used to
represent counts, quantities, or other numerical values
that do not have a fractional part.

Floats:

A float is a data type that represents real numbers,
including both whole numbers and numbers with a
fractional part. Floats are used to represent values
that require greater precision than integers.

Strings:

A string is a data type that represents a sequence of
characters. Strings are used to represent text in
programming, such as names, messages, or other
information.

"""


def example_boolean_usage() -> None:
    """
    Example function to demonstrate boolean usage.

    This function demonstrates how to use booleans
    in Python. Booleans are used to represent logical
    values, such as whether a condition is true or
    false.

    You can cast other data types to boolean using the bool() function.
    For example, bool(0) will return False, while bool(1) will return True.

    """

    print("Example function to demonstrate boolean usage.")

    # Define a boolean variable
    is_true = True
    is_false = False

    # Print the boolean values
    print("is_true:", is_true)
    print("is_false:", is_false)

    # Cast other data types to boolean
    print("bool(0):", bool(0))
    print("bool(1):", bool(1))
    print("bool(0.0):", bool(0.0))
    print("bool(1.0):", bool(1.0))
    print("bool(''): ", bool(""))
    print("bool('Hello'): ", bool("Hello"))


def example_integer_usage() -> None:
    """
    Example function to demonstrate integer usage.

    This function demonstrates how to use integers
    in Python. Integers are used to represent whole
    numbers, both positive and negative.

    You can perform mathematical operations with integers.
    For example, you can add, subtract, multiply, and divide
    integers using the standard arithmetic operators.

    You can also cast other data types to integers using the
    int() function. For example, int(3.14) will return 3.

    An important note about integer division in Python:
    When you divide two integers in Python, the result will
    always be a float, even if the result is a whole number.
    For example, 10 / 5 will return 2.0, not 2.

    Another important note about casting to integers:
    When you cast a float to an integer, Python will truncate
    the decimal part of the number. For example, int(3.14)
    will return 3, not 4.

    """

    print("Example function to demonstrate integer usage.")

    # Define some integer variables
    x = 10
    y = 5

    # Perform arithmetic operations with integers
    print("x + y:", x + y)
    print("x - y:", x - y)
    print("x * y:", x * y)
    print("x / y:", x / y)

    # Cast other data types to integers
    print("int(3.14):", int(3.14))
    print("int('10'):", int("10"))
    print("int(True):", int(True))
    print("int(False):", int(False))


def example_float_usage() -> None:
    """
    Example function to demonstrate float usage.

    This function demonstrates how to use floats
    in Python. Floats are used to represent real
    numbers, including both whole numbers and
    numbers with a fractional part.

    You can perform mathematical operations with floats.
    For example, you can add, subtract, multiply, and divide
    floats using the standard arithmetic operators.

    You can also cast other data types to floats using the
    float() function. For example, float(10) will return 10.0.

    An important note about casting to floats:
    When you cast an integer to a float, Python will add a
    decimal point and a zero to the number. For example,
    float(10) will return 10.0, not 10.

    """

    print("Example function to demonstrate float usage.")

    # Define some float variables
    x = 3.14
    y = 2.71

    # Perform arithmetic operations with floats
    print("x + y:", x + y)
    print("x - y:", x - y)
    print("x * y:", x * y)
    print("x / y:", x / y)

    # Cast other data types to floats
    print("float(10):", float(10))
    print("float('3.14'):", float("3.14"))
    print("float(True):", float(True))
    print("float(False):", float(False))


def example_string_usage() -> None:
    """
    Example function to demonstrate string usage.

    This function demonstrates how to use strings
    in Python. Strings are used to represent text
    in programming, such as names, messages, or
    other information.

    You can perform string operations with strings.
    For example, you can concatenate strings using the
    + operator, or repeat a string using the * operator.

    You can also cast other data types to strings using
    the str() function. For example, str(10) will return
    "10".

    """

    print("Example function to demonstrate string usage.")

    # Define some string variables
    hello = "Hello"
    world = "World"

    # Perform string operations with strings
    print("hello + world:", hello + world)
    print("hello * 3:", hello * 3)

    # Cast other data types to strings
    print("str(10):", str(10))
    print("str(3.14):", str(3.14))
    print("str(True):", str(True))
    print("str(False):", str(False))


def main() -> None:
    """
    Main function for the primitive data types module.

    This function provides examples of primitive data types
    in Python, including booleans, integers, floats, and strings.

    """

    # Print a welcome message
    print("Welcome to the primitive data types module!")

    # Call the example usage functions
    example_boolean_usage()
    example_integer_usage()
    example_float_usage()
    example_string_usage()


if __name__ == "__main__":
    main()
