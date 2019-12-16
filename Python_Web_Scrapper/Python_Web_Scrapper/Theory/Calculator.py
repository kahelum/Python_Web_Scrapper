def plus(a, b):
    return int(a) + int (b)

def sub(a, b):
    return int(a) - int (b)

def mul(a, b):
    return int(a) * int (b)

def div(a, b):
    return int(a) / int (b)

def negation(a):
    return -int(a)

def pow(a, b):
    return int(a) ** int (b)

def reminder(a, b):
    return int(a) % int (b)

print(plus(5, "5"))
print(sub(5, 2))
print(mul(5, 3))
print(div(6, 3))
print(negation(9))
print(pow(2, 5))
print(reminder(8, 5))