# Docstrings are literals that apper right after the definition of a function,method,class or module
def sqaure(n): # docstring is added right below the function name and it is not a comment and python gives special attibutes to it
    '''Takes a number n and return the square of number n'''
    print(n**2)
sqaure(5)
print(sqaure.__doc__)
# pep 8 is python enhancment proposal describes new features , documents, design and style for community