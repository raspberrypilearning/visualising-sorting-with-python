def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# def coprimes(c):
#     values = [i for i in range(1,c) if gcd(c,i) == 1]
#     return values

def coprimes(c):
    values = []
    for i in range(1,c):
        if gcd(c,i) == 1:
            values.append(i)
    return values

results = coprimes(63)
