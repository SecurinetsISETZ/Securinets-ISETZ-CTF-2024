# Task: The Encrypted Mystery

## Description
> While digging through intercepted data, I came across a series of mysterious numbers and an encrypted flag.  
> They seem connected, but the true meaning is locked away.  
> Can you unravel the puzzle, find the missing keys, and uncover the hidden message?  

> **Author:** ADX2K

---

## Solution
This task is based on **Diffie-Hellman encryption**. We need to retrieve the shared key using the provided parameters and decrypt the flag. Since the numbers used are **large**, we use the **Baby-Step Giant-Step (BSGS)** method to solve discrete logarithms efficiently.

### Given Encryption Code
```python
from Crypto.Util.number import getPrime
import random


p = getPrime(48)
g = 17
a = random.randint(1, p - 1)
b = random.randint(1, p - 1)

flag = ""

A = pow(g, a, p) 
B = pow(g, b, p) 

key = pow(A, b, p)


encrypted_flag = []
for char in flag:
    encrypted_flag.append(ord(char) ^ (shared_secret % 256))

'''
p: 0xec9de9898c4f
g: 0x11
A: 0x68b907670156
B: 0xc37922ebe082
Encrypted Flag: ['0x68', '0x5e', '0x58', '0x4e', '0x49', '0x52', '0x55', '0x5e', '0x4f', '0x48', '0x40', '0x7f', '0xa', '0x5d', '0x5d', '0xa', '0x8', '0x64', '0x73', '0x8', '0x57', '0x57', '0x56', '0xf', '0x55', '0x64', '0x8', '0x55', '0x58', '0x49', '0x42', '0x4b', '0x4f', '0xa', '0x54', '0x55', '0x46']
'''
```
### Approach
We need to find the private keys (**a** and **b**) using the **Baby-Step Giant-Step** algorithm, as the numbers are too large for brute force approaches.

1. **Calculate private key (a):**  
   Use the BSGS method to compute the discrete logarithm of **A** with respect to **g mod p**.
2. **Compute shared key:**  
   Once **a** is found, calculate the shared key using:  
   `key = B^a % p`
3. **Decrypt the flag:**  
   XOR the encrypted flag bytes with the **key % 256**.

### Key Observations
- **Diffie-Hellman relies on discrete logarithms,** which are computationally hard to reverse for large numbers. However, with relatively smaller primes, the **BSGS algorithm** is efficient.
- The encrypted flag is XOR-encrypted using the shared key modulo 256, making it straightforward to reverse once the key is known.

### Decryption Code
```python
from math import isqrt
p = 0xec9de9898c4f
g = 0x11
A = 0x68b907670156
B = 0xc37922ebe082
encrypted_flag_hex = [0x68, 0x5e, 0x58, 0x4e, 0x49, 0x52, 0x55, 0x5e, 0x4f, 0x48, 0x40, 0x7f, 0xa, 0x5d, 0x5d, 0xa, 0x8, 0x64, 0x73, 0x8, 0x57, 0x57, 0x56, 0xf, 0x55, 0x64, 0x8, 0x55, 0x58, 0x49, 0x42, 0x4b, 0x4f, 0xa, 0x54, 0x55, 0x46]
def baby_step_giant_step(g, A, p):
    m = isqrt(p) + 1  # Step size
    value_table = {}
    current = 1
    for j in range(m):
        value_table[current] = j
        current = (current * g) % p
    g_inv_m = pow(g, -m, p)
    giant_step = A
    for i in range(m):
        if giant_step in value_table:
            return i * m + value_table[giant_step]
        giant_step = (giant_step * g_inv_m) % p

    return None
a = baby_step_giant_step(g, A, p)
if a is not None:
    key = pow(B, a, p)
    decrypted_flag = ''.join(chr(byte ^ (key % 256)) for byte in encrypted_flag_hex)
else:
    decrypted_flag = "Failed to recover private key."
print("Decrypted Flag:", decrypted_flag)

```

After running the BSGS algorithm and decrypting the flag using the derived key, we obtain:

**Flag:** `Securinets{D1ff13_H3llm4n_3ncrypt1on}`


