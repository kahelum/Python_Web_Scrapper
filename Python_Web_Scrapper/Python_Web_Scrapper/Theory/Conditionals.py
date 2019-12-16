def plus(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

print(plus(5,'a'))
print(plus(5,6.5))
