def largest_factor(a, b):
    if b == 0:
        print(a)
    else:
        return largest_factor(b, a % b)
    
