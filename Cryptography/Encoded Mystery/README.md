
# Task: Encoded Mystery  

## Description  
> My friend handed me this strange text and insisted it holds something crucial.  
> Can you figure out what’s hidden inside?  
 
> **Author:** ADX2K  

The challenge provides a file (`flag.txt`) containing a string that looks encoded. Your mission is to decode it and reveal the hidden flag.  

---

## Solution  

### Step 1: Analyze the File  
Open the provided file (`flag.txt`) and examine its contents.  

The string appears to be **Base64 encoded**, which is a common encoding format used to obfuscate text.  

### Step 2: Automate the Decoding Process  
Since the file might be **encoded multiple times**, manually decoding it step-by-step would be inefficient. Instead, we’ll write a Python script to automate the decoding process until the flag is found.  

### Python Script:  
```python
import base64
def decode_until_flag(file_path):
    with open(file_path, 'r') as file:
        encoded_data = file.read().strip()
    while True:
        decoded_data = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
        if '{' in decoded_data and '}' in decoded_data and '_' in decoded_data :
            print("Flag found:", decoded_data)
            break
        elif len(decoded_data) % 4 !=0:
            print("Flag not found:", decoded_data)
            break
        else:
            encoded_data = decoded_data
file_path = "flag.txt"
decode_until_flag(file_path)

```
### Step 3: Run the Script  
Save the script as `Base64Sol.py` and execute it with Python:  

```
python3 Base64Sol.py
```

### Step 4: Retrieve the Flag  
The script will keep decoding until it outputs the flag:  

Flag: ```Securinets{Base64_1s_4lw4ys_4_g00d_1d34}```
