def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def abc(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(4)
print abc(-4)