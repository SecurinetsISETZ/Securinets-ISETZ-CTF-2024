from Crypto.Util.number import getPrime
from random import randint
flag : Securinets{part1+part2} 
a = int(part1.encode().hex(), 16) 
b = int(part2.encode().hex(), 16) 

A = pow(g, a, p)
B = pow(g, b, p)

'''
p = 0xe4459d1445e9
g = 0x2
A = 0xdaa34310e4c3
B = 0x46ccdee8b8fe
'''