"""
Level 35: Shor's Factoring Algorithm

Physical meaning:
Factors composite integers N = p × q in polynomial time.
Classical complexity: sub-exponential (infeasible for large N)
Quantum complexity: O((log N)³) - exponential speedup

Key technique: Order finding via phase estimation
"""

import numpy as np
from math import gcd

def classical_order_finding(a, N):
    """Find order r where a^r ≡ 1 (mod N) classically.
    
    Args:
        a: int - base
        N: int - modulus
    
    Returns:
        int: order r, or None if not found
    """
    r = 1
    power = a % N
    while power != 1:
        power = (power * a) % N
        r += 1
        if r > N:  # Safety check
            return None
    return r

def shor_factor(N, a=None):
    """Factor N using Shor's algorithm (hybrid classical-quantum).
    
    Args:
        N: int - composite number to factor
        a: int - random base (optional, chosen randomly if None)
    
    Returns:
        tuple: (p, q) factors of N, or None if failed
    """
    if a is None:
        # Choose random a coprime to N
        while True:
            a = np.random.randint(2, N)
            if gcd(a, N) == 1:
                break
    
    # Check if a already divides N
    if N % a == 0:
        return (a, N // a)
    
    # Find order r (in real quantum computer, use phase estimation)
    r = classical_order_finding(a, N)
    if r is None or r % 2 == 1:
        return None  # Failed, try different a
    
    # Check a^{r/2} ≢ -1 (mod N)
    if pow(a, r // 2, N) == N - 1:
        return None  # Failed, try different a
    
    # Extract factors
    p = gcd(pow(a, r // 2) - 1, N)
    q = gcd(pow(a, r // 2) + 1, N)
    
    if p > 1 and q > 1 and p * q == N:
        return (p, q)
    else:
        return None

# Test Shor's algorithm
if __name__ == "__main__":
    print("=== Shor's Factoring Algorithm ===\n")
    
    # Test 1: Factor 15
    N = 15
    print(f"Test 1 - Factoring N = {N}:")
    for a in [2, 7, 11, 13]:  # Try different bases
        result = shor_factor(N, a)
        if result:
            print(f"Using a = {a}: factors are {result}")
            break
    print()
    
    # Test 2: Factor 21
    N = 21
    print(f"Test 2 - Factoring N = {N}:")
    result = shor_factor(N)
    if result:
        print(f"Factors are {result}")
    else:
        print("Failed, trying again...")
        result = shor_factor(N)
        if result:
            print(f"Factors are {result}")
    print()
    
    # Test 3: Factor 35
    N = 35
    print(f"Test 3 - Factoring N = {N}:")
    result = shor_factor(N)
    if result:
        print(f"Factors are {result}")
    print()
    
    # Test 4: Demonstrate order finding
    print("Test 4 - Order finding for N=15, a=7:")
    print("Computing powers of 7 mod 15:")
    power = 1
    for r in range(1, 6):
        power = (power * 7) % 15
        print(f"7^{r} ≡ {power} (mod 15)")
    print(f"Order r = {classical_order_finding(7, 15)}")
