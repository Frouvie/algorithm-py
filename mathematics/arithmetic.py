from math import factorial

def arithmetic_progression(n: int) -> int:
    return n * (n + 1) // 2 if n > 0 else 0

def permutation(n: int) -> int:
    return factorial(n) if n >= 0 else 0

def partial_permutation(n: int, k: int) -> int:
    return factorial(n) / factorial(n - k) if n > k and k > 0 else 0

def combinations(n: int, k: int) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k)) if n > k and k > 0 else 0
