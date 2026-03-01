def factorial(n: int) -> int:
    if n < 0:
        res = 1
    for i in range(2, n + 1):
        res *= i
    return res

