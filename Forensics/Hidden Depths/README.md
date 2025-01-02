
# Task: Hidden Depths

## Description
> This image seems ordinary, but my source insists it holds more than meets the eye.  
> Can you uncover its secrets?

> Author: ADX2K

The challenge provides an image file that appears normal at first glance but contains hidden data. Your mission is to analyze the image, uncover the hidden layers, and retrieve the flag.

---

## Solution

The solution involves multiple steps using steganographic techniques to uncover the hidden flag.

### Step 1: Examine the Image
Start by inspecting the provided image for any embedded files. Use **binwalk**, a tool for analyzing and extracting data hidden within files.

Run the following command:  
```
binwalk --dd=".*" Gabes.jpg
```

This command extracts any embedded files from the image. After running it, a second image file is discovered in the extracted directory.



### Step 2: Analyze the Second Image
The second image may contain additional hidden data. Use **ExifTool** to inspect its metadata for clues. Run the following command:  
```
exiftool hidden.jpg
```

Inspecting the metadata reveals a password hint:  
Password Format: ``jR*S*_4*0wM``

This indicates the password for the next layer follows the format `jR*S*_4*0wM`, where the `*` symbols need to be replaced with characters.



### Step 3: Generate a Wordlist
To proceed, generate a wordlist of possible passwords based on the given format. You can use the following Python script:

from itertools import product  
import string  

# Define the password format  
prefix = "jR"  
suffix = "_4"  
middle = "0wM"  
possible_chars = string.ascii_letters + string.digits  

# Generate the wordlist  
with open("passwords.txt", "w") as f:  
    for combo in product(possible_chars, repeat=3):  # 3 '*' symbols  
        password = f"{prefix}{combo[0]}{combo[1]}{combo[2]}{suffix}{middle}"  
        f.write(password + "\n")  
print("Wordlist generated: passwords.txt")

This script generates all possible combinations for the password format and saves them to a file named `passwords.txt`.

---

### Step 4: Use StegSeek to Extract Hidden Data
Next, use **StegSeek** to brute-force the password and extract the hidden data from the second image.

Run the following command:  
stegseek extracted_image.jpg passwords.txt

StegSeek will attempt each password in the wordlist until it successfully extracts the hidden data. After the process completes, the flag is revealed.

---

## Flag
Securinets{Unc0ver_Th3_Lay3rs}

---

## Tools Used
1. **Binwalk**: For analyzing and extracting embedded files.  
   Command: binwalk --dd=".*" hidden_image.jpg  
2. **ExifTool**: For inspecting image metadata.  
   Command: exiftool extracted_image.jpg  
3. **StegSeek**: For brute-forcing Steghide passphrases.  
   Command: stegseek extracted_image.jpg passwords.txt  
4. **Python**: For generating the password wordlist.

---

## Summary
1. Use **binwalk** to extract files from the provided image.  
2. Analyze the metadata of the extracted image using **ExifTool** to find a password format.  
3. Generate a wordlist based on the password format using Python.  
4. Use **StegSeek** with the wordlist to brute-force the password and extract the hidden flag.

---

Include the provided image (`hidden_image.jpg`) in your repository for players to test. Let me know if you need further refinements or adjustments!
