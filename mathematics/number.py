from typing import List

def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    
    i = 2
    
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    
    return True

def factorize(x: int) -> List[int]:
    factors = []
    i = 2

    while i * i <= x:
        while x % i == 0:
            factors.append(i)
            x //= i
        i += 1

    if x != 1:
        factors.append(x)

    return factors

def find_dividers(x: int) -> List[int]:
    dividers = []
    i = 1

    while i * i <= x:
        if x % i == 0:
            dividers.append(i)

            if i * i != x:
                dividers.append(x / i)

    return dividers

def list_primes(left: int, right: int) -> List[int]:
    sieve = [True] * (right + 1)
    primes = []

    for i in range(2, right + 1):
        if sieve[i]:
            for j in range(i * i, right + 1, i):
                sieve[j] = False
    
    for i in range(left, right + 1):
        if sieve[i]:
            primes.append(i)
    
    return primes
