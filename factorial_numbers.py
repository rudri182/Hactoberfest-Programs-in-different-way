def factorial_numbers(n):
    assert n>=0 # Only non-negatives allowed
    assert type(n) == int # We only consider integer numbers
    total = 1
    while n>0:
        total *= n
        n-=1
    return total