from math import isqrt

# Parameters
p = 0xec9de9898c4f
g = 0x11
A = 0x68b907670156
B = 0xc37922ebe082
encrypted_flag_hex = [0x68, 0x5e, 0x58, 0x4e, 0x49, 0x52, 0x55, 0x5e, 0x4f, 0x48, 0x40, 0x7f, 0xa, 0x5d, 0x5d, 0xa, 0x8, 0x64, 0x73, 0x8, 0x57, 0x57, 0x56, 0xf, 0x55, 0x64, 0x8, 0x55, 0x58, 0x49, 0x42, 0x4b, 0x4f, 0xa, 0x54, 0x55, 0x46]

# Baby-Step Giant-Step to find discrete logarithm
def baby_step_giant_step(g, A, p):
    m = isqrt(p) + 1  # Step size
    value_table = {}

    # Baby step: Compute g^j % p for j in [0, m)
    current = 1
    for j in range(m):
        value_table[current] = j
        current = (current * g) % p

    # Giant step: Compute A * g^(-im) % p for i in [0, m)
    g_inv_m = pow(g, -m, p)
    giant_step = A

    for i in range(m):
        if giant_step in value_table:
            return i * m + value_table[giant_step]
        giant_step = (giant_step * g_inv_m) % p

    return None

# Recover private key a
a = baby_step_giant_step(g, A, p)

# If a is found, calculate the shared key and decrypt the flag
if a is not None:
    key = pow(B, a, p)
    decrypted_flag = ''.join(chr(byte ^ (key % 256)) for byte in encrypted_flag_hex)
else:
    decrypted_flag = "Failed to recover private key."

print("Decrypted Flag:", decrypted_flag)
