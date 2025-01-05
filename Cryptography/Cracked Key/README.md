# Task: Cracked Key

## Description
> I intercepted this encrypted message, but the key to unlocking it is missing.  
> Can you uncover the secret?  
> **Flag format**: Securinets{}
 
> **Author**: ADX2K  

The challenge provides the following RSA parameters:
- **Ciphertext (C):** 31763929159528552398701727519578458901
- **Modulus (n):** 133057759405410196713996577614776585137
- **Exponent (e):** 65537

Your goal is to decrypt the ciphertext and retrieve the flag.

---

## Solution

### Step 1: Observe the Given Values
Looking at the provided values, it is clear that **n** is relatively small. This indicates that the RSA key size is weak and can be factored quickly.

### Step 2: Use Online Tools
Since the values are small, we can easily solve this using the online tool **dcode.fr** (RSA Cipher):

1. Go to: [RSA Cipher Decrypter](https://www.dcode.fr/rsa-cipher)
2. Input the given values:
   - **Modulus (n):** 133057759405410196713996577614776585137
   - **Exponent (e):** 65537
   - **Ciphertext (C):** 31763929159528552398701727519578458901
3. Click **Decrypt** to obtain the plaintext.

### Step 3: Retrieve the Flag
The plaintext output reveals the flag, which follows the required format.

Flag: `Securinets{Th1s_1s_3@sy_RSA}`

