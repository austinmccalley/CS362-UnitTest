def is_integer(s):
    negative = True if s[:1] == '-' else False
    if negative:
        if len(s) == 1:
            return False
        s = s[1:]
        for c in s:
            if not (c >= '0' and c <= '9'):
                return False
        return True
    else:
        for c in s:
            if not(c >= '0' and c <= '9'):
                return False
        return True


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return 0
    else:
        return a / b
