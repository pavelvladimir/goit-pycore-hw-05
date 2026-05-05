def caching_fibonacci():
    """Return a Fibonacci function that caches previously computed values."""

    cache = {}

    def fibonacci(n):
        if not isinstance(n, int):
            raise TypeError("n must be an integer.")
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
