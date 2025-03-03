def rabbit_pairs(months, k):
    if months == 1 or months == 2:
        return 1
    
    previous = 1 # F(n-2)
    current = 1 # F(n-1)

    for _ in range(3, months + 1):
        next_value = current + k * previous
        previous, current = current, next_value
    
    return current

rabbit_pairs(33, 3)