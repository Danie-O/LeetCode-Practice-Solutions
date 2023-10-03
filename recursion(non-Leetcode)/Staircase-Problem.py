def number_of_paths(n):
    # base cases
    if n < 0:
        return 0 
    elif n == 1 or n == 0:
        return 1 

    else:
        return number_of_paths(n - 1) + number_of_paths(n - 2) + number_of_paths(n - 3)