def factorial(n: int) -> int:
    if n < 0:
        res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
