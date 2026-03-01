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
    
def readfile(file):
    try:
        with open(file, encoding="utf=8") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError as fnf_err:
        print(f"Файл {fnf_err.filename} не знайдено")
