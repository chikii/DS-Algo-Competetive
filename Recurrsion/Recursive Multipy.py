def multiply(a, b):
    if a<b: a, b = b, a
    res = 0
    while b:
        if b&1:
            res = res+a
        b >>= 1
        a += a
    return res

a, b = 45, 52
print(multiply(a, b), a*b)