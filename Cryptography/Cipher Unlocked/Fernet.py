from cryptography.fernet import Fernet

# Hexadecimal key and encrypted flag (convert them to bytes)
key_hex = "74 77 68 73 79 62 67 65 6B 70 48 44 39 45 64 33 75 65 4B 45 6C 31 75 63 47 4F 37 46 6F 66 69 6B 46 78 58 67 34 61 6B 55 51 6C 59 3D"
encflag_hex = "67 41 41 41 41 41 42 6E 63 48 66 47 58 70 79 67 68 75 61 73 50 57 5A 46 77 34 59 35 34 71 62 79 71 4F 31 76 62 4F 61 51 4D 43 52 65 33 44 74 70 6D 5A 54 6D 49 55 6E 48 69 2D 31 30 78 56 62 30 6E 42 2D 44 57 6B 71 63 49 75 52 41 36 79 5F 79 4E 69 46 45 4E 38 6C 70 68 5A 36 63 73 75 72 4F 6F 4A 55 39 76 41 6A 74 78 50 56 4C 70 70 37 52 31 54 6A 77 52 71 6F 3D"

# Convert the hexadecimal strings to bytes
key = bytes.fromhex(key_hex)
encflag = bytes.fromhex(encflag_hex)

# Create the Fernet object with the key
fernet = Fernet(key)

# Decrypt the flag
flag = fernet.decrypt(encflag)

# Convert the decrypted flag to a string and print it
print(flag.decode())
