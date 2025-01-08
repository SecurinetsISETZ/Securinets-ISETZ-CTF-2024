# Task: Diffie’s Puzzle

> ### Description:
> I intercepted these mysterious Diffie-Hellman values during a secret communication.  
> Can you reverse them and piece together the hidden message in the format **Securinets{}**?

> **Author:** ADX2K  

---

## Solution

### Step 1: Analyze the Encryption Scheme
The problem involves a Diffie-Hellman key exchange setup where the private keys are directly encoded as hexadecimal representations of parts of the flag.

Given data:
```
p = 0xe4459d1445e9
g = 0x2
A = 0xdaa34310e4c3
B = 0x46ccdee8b8fe
```

The public keys (A and B) are derived as:
- A = g^a mod p
- B = g^b mod p

We need to reverse this process to retrieve the private keys (**a** and **b**), which form the parts of the flag.

---

### Step 2: Solve for Private Keys
Python's `sympy` library provides the `discrete_log` function to reverse the modular exponentiation and extract the private keys.

```python
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

# Convert private keys to bytes
fa = long_to_bytes(a)
fb = long_to_bytes(b)

# Format the flag
flag = f"Securinets{{{fa.decode()}_{fb.decode()}}}"
print(flag)
```

### Step 3: Retrieve the Flag
Executing the script outputs the flag:

Flag: ```Securinets{D1ff_&_H3ll}```


