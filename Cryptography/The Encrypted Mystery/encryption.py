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