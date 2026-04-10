def factorail(n) -> float:
    """a factorial function"""
    if n == 0 or n == 1:
        return 1
    return n * factorail(n - 1)


def gcd(a, b) -> float:
    """a gcd function"""
    while b:
        a, b = b, a % b
    return a