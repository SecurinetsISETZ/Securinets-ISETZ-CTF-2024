# Task: The Hidden Trace

## Description
> Some things are best left unspoken, they said, yet left behind this file.  
> What’s inside may not be what it seems.

> Author: ADX2K

The challenge provides a `.wav` file that appears normal but may contain something hidden. Your goal is to uncover its secrets.

---

## Solution

### Step 1: Analyze the File
The provided `.wav` file seems ordinary, but its description hints at hidden content. To investigate, we can use tools called ``Binwalk`` or ``Foremost``, which can analyze and extract embedded data from files.

### Step 2: Extract Hidden Data
Running ``Binwalk`` on the `.wav` file reveals that it contains a hidden **JPEG** file.
<br><div align="center">
  <img src="Binwalk.png" alt="binwalk Mystery.wav">
</div>
To extract all embedded files, we use the `--dd` option.

Run the following command:
```binwalk --dd=".*" Mystery.wav```
<div align="center">
  <img src="ExtractData.png" alt="binwalk --dd=".*" Mystery.wav">
</div>

Then now the data is extracted and we got the **JPEG** file with the name **2D2D**. And this is our flag : 
<div align="center">
  <img src="Flag.png" alt="Flag.png">
</div>

Flag : ```Securinets{Alw@y5_L00k_F0r_H3x}```
