def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) #Process of defining something in terms of itself
print(factorial(3))
print(factorial(4))
print(factorial(5))
# Fibonacci sequence
def fiborec(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        fiborec(n-1)+fiborec(n-2)


