# to find modular inverse of k under modulo m using Fermat's little theorem.
# This program works only if m is prime.
def __gcd(k, l):
    if(l == 0):
        return k
    else:
        return __gcd(l, k % l)
# To compute x^y under modulo m
def power(x, y, m):
    if (y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    return p if(y % 2 == 0) else (x * p) % m
# Function to find modular inverse of k under modulo m (Assumption: m is prime)
def modInverse(k, m):
    if (__gcd(k, m) != 1):
        print("Inverse does not exist")
    else:
        # If k and m are relatively prime, then modulo inverse is k^(m-2) mode m
        print("Modular multiplicative inverse is ",
            power(k, m - 2, m))
k = 3
m = 11
modInverse(k, m)
