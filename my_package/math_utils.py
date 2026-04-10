def factorail(n: int) -> int:
    """A factorial function using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorail(n - 1)


def gcd(a: int, b: int) -> int:
    """A GCD function using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a