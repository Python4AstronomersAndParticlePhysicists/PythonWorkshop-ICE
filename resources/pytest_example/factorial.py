def factorial(n):
    """Does this function work? Hint: no."""
    n_fact = n
    while n > 1:
        n -= 1
        n_fact *= n
    return n_fact
    
