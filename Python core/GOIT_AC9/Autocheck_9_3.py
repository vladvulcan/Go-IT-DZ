def caching_fibonacci():
    cache = {
        0: 0,
        1: 1
    }
    def fibonacci(n):
        if n in cache:   
            return cache[n]
        else:
            x = fibonacci(n-1)+fibonacci(n-2)
            cache[n] = x
            return x

    return fibonacci