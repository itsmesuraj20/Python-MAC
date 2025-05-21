#TYPES OF COMMENTS IN PYTHON
# 1. Single-line comments
# 2. Multi-line comments
# 3. Docstrings

# 1. Single-line comments
# This is a single-line comment
print("Hello, World!")  # This is an inline comment

# 2. Multi-line comments
'''
This is a multi-line comment
It can span multiple lines
'''
print("Hello, World!")  # This is an inline comment

# 3. Docstrings
"""
This is a docstring
It is used to document functions, classes, and modules
"""
def my_function():
    """
    This is a docstring for my_function
    It describes what the function does
    """
    print("Hello, World!")
my_function()  # Call the function
# Docstrings can also be used to document classes
class MyClass:
    """
    This is a docstring for MyClass
    It describes what the class does
    """
    def __init__(self):
        """
        This is a docstring for the __init__ method
        It describes what the method does
        """
        print("Hello, World!")
my_class = MyClass()  # Create an instance of MyClass
# Docstrings can also be used to document modules
"""