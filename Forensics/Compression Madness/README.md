# Task: Compression Madness

## Description
> My colleague sent me this ridiculously compressed file and said, 'Good luck!'  
> It’s layer after layer of decompression.  
> Can you endure the madness and uncover the hidden message?

> Author: ADX2K

The challenge provides a file (`200.zip`) that is compressed multiple times. Your mission is to handle each layer of compression, retrieve the final file, and uncover the hidden flag.

---

## Solution

### Step 1: Understand the Problem
The initial file (`200.zip`) contains multiple layers of compression, and manually decompressing each layer would be a **terrible idea**. Here’s why:

- **Time-Consuming**: Each decompression step takes time, especially when there are multiple layers.
- **Frustrating**: Manually decompressing files layer-by-layer is tedious and inefficient.

Instead, **automation** is the best way to handle this challenge. Let’s automate the process step by step.

---

### Step 2: Automate the `.zip` File Extraction
The first layer is a `.zip` file. Automatically, you would extract all the **.zip** layers using this python code:
```python
import zipfile
import os

def decompress_nested_zips(start_zip, output_folder):
    current_zip = start_zip
    
    while current_zip.endswith(".zip"):
        try:
            with zipfile.ZipFile(current_zip, 'r') as zip_ref:
                zip_ref.extractall(output_folder)
            os.remove(current_zip)
            
            next_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith(".zip")]
            if not next_files:
                break
            current_zip = next_files[0]
        except zipfile.BadZipFile:
            print(f"Bad ZIP file: {current_zip}")
            break

starting_zip = "200.zip"
output_dir = "extracted"
os.makedirs(output_dir, exist_ok=True)
decompress_nested_zips(starting_zip, output_dir)
```
After the decompression we got 2 files : 
- **200.tar** this is another file that contains multiple layers of compression.
- **password.txt** this file contains a password but we don't know it's case of use
  ```Password : HalfWay400```
### Step 3: Automate the `.tar` File Extraction
The second layer is a `.tar` file. Automatically, you would extract all the **.tar** layers using this python code:
```python
import tarfile
import os

def decompress_nested_tars(start_tar, output_folder):
    current_tar = start_tar

    while current_tar.endswith(".tar"):
        try:
            with tarfile.open(current_tar, 'r') as tar_ref:
                tar_ref.extractall(output_folder)
            os.remove(current_tar)
            
            next_files = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith(".tar")]
            if not next_files:
                break
            current_tar = next_files[0]
        except tarfile.TarError:
            print(f"Bad TAR file: {current_tar}")
            break

starting_tar = "extracted/200.tar" 
output_dir = "extracted"
os.makedirs(output_dir, exist_ok=True)
decompress_nested_tars(starting_tar, output_dir)
```
After the decompression we got a pdf file. 
trying to open the pdf file it demands to use a password.

### Step 4: Open the pdf file
So now the only step left is to open the pdf file with the password ``HalfWay400`` and here we go we got the flag.


Flag : ``Securinets{Pyth0n_L
00p5_4r3_H3lpfull}``
