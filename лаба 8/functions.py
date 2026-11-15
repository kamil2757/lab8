# functions.py

# --- Задание 1 ---
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Задание 2 ---
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_iter(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# --- Задание 3 ---
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

# --- Задание 4 ---
def sum_digits(n: int) -> int:
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

def reverse_string(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)