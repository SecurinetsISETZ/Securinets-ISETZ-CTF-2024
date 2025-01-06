# Task: Securing the Message

## Description
> My friend sent me this encrypted message along with the code they used, claiming it’s to avoid a man-in-the-middle attack.  
> Can you help me decode it and reveal the secret?  

**Author:** ADX2K  
**Hint:** `p + q`

---

## Solution

The problem involves RSA encryption using large prime numbers. We are given the ciphertext (`c`), modulus (`n`), public exponent (`e`), and a hint (`p + q`). The challenge is to decrypt the ciphertext and retrieve the flag.

### Step 1: Analyze the Encryption Code

```python
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
```

### Key Observations
1. The encryption uses RSA with large primes (`p` and `q`).
2. The provided hint (`p + q`) helps recover the values of `p` and `q`.
3. The private key can be derived once `p` and `q` are known.

### Step 2: Solve the Challenge
We use the **hint** and **n** to find `p` and `q` using the quadratic equation approach.

#### Python Solution:

```python
from sympy import sqrt
from Crypto.Util.number import long_to_bytes

c = 9472843078943706279499150492829502456745516159688150776276268995092861294491065849516733944955920820340298784537866811561877711685545925879453223898930667739987213875511401796223739617894740102832354639859002015809414344986695369870236287032226655470680398462011136742541510778355961172151664178683520781198945188421935022830902247891806595523201858166230958280314644917453167704479831840512120469181480479309436232944655325878204137622158462181951969473600462083220135819361378122096964430682932675572946843848263426185406307014393575350954561353062581740534204480271946796957159712006462887775903178477068606465854
hint = 248417732203978289135857067169388159850784793013662385278479478453695812571946727234572103686193252514704382819280243087359587132990182639545651718178035042433592920794140779546477976186958430701322872749929541979279321251286077939770802035288235885431553243078222609812538724565670277246515971454786631359978
n = 15362604478401671251570932628927492902470741966153185297461397274825377741706183252927039212611408618238303867157879256137558685845413559307496035225412242688509180487414473454019315082694143204021130300768645608281094240457906531224373352184867299181670702434099714431676780976517495641865098975582401061478438311369641077330843382712400156962524274729850894166668974738204467448018839066783824983964509833894005860105857306997972350264907975218777688994336244051367209632761161493759100031801345314814113889164202240361906616984428765060065006844041909895921035385211399734172159840209701262110032138884221910946537
e = 65537

p_plus_q = hint
discriminant = sqrt(p_plus_q**2 - 4 * n)
p_val = (p_plus_q + discriminant) // 2
q_val = (p_plus_q - discriminant) // 2

assert p_val * q_val == n

phi_n = int((p_val - 1) * (q_val - 1))

d = pow(e, -1, phi_n)

m = pow(c, d, n)
flag = long_to_bytes(m)

print(f"Decrypted flag: {flag.decode()}")
```

### Step 3: Getting The Flag
1. The hint (`p + q`) allows us to solve for `p` and `q` using the quadratic formula.
2. Once `p` and `q` are found, the private key (`d`) is calculated using modular inverse.
3. Finally, we decrypt the ciphertext using the private key and retrieve the flag.

Flag: `Securinets{W3_C@n_U5e_5UM_1n_RSA}`


