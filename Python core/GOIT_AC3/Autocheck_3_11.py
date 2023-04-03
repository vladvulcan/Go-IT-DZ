def fibonacci(n):
    if n < 2:
        if n == 1:
           return 1
        else: return 0
    else: return fibonacci(n-1)+fibonacci(n-2)