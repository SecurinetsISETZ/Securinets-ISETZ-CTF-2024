from sympy.ntheory import discrete_log
from Crypto.Util.number import long_to_bytes

# Convert hexadecimal values to integers
p = int("e4459d1445e9", 16)
g = int("2", 16)
A = int("daa34310e4c3", 16)
B = int("46ccdee8b8fe", 16)

# Calculate private keys
a = discrete_log(p, A, g)  # Find a such that g^a ≡ A (mod p)
b = discrete_log(p, B, g)  # Find b such that g^b ≡ B (mod p)
print(f"a = {a}")
print(f"b = {b}")

# Convert private keys to bytes
fa = long_to_bytes(a)
fb = long_to_bytes(b)

# Format the flag
flag = f"Securinets{{{fa.decode()}_{fb.decode()}}}"
print(flag)
