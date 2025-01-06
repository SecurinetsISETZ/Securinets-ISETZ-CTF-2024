from Crypto.Util.number import getPrime, bytes_to_long
import os
from random import getrandbits

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 0x10001
hint = p + q
c = pow(bytes_to_long(flag.encode()), e, n)  # Fix: Encode flag to bytes
with open("output.txt", 'w') as f:
    f.write(f"{c =}\n")
    f.write(f"{hint =}\n")
    f.write(f"{n =}\n")
    f.write(f"{e =}\n")