def say_hello(name):
    """Print Hello"""
    print("Congratulations " + name + " wish you the best!")

def summa(x, y):
    return x+y


def factorial(x):
    """Calculate factorial of number X"""
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet * i
    return otvet
#------------------------
print("------------------")
for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))
