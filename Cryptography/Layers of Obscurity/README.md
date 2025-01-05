# Task: Layers of Obscurity

## Description

> I came across this strange sequence of data.\
> Can you figure out what it really means?

> **Author:** ADX2K

The challenge provides a string of encoded data that has been transformed through multiple layers of encoding. Your task is to decode it step-by-step to uncover the hidden flag.

---

## Solution

### Step 1: Understand the Problem

The encoded data in this task has gone through multiple transformations. Manually decoding each layer can be tedious, so we'll use an online tool called **CyberChef** to streamline the process.

### Step 2: The Decoding Process

The data will be decoded using multiple layers in the following sequence:

1. **Base64** encoding
2. **URL encoding**
3. **Binary** encoding
4. **Hexadecimal** encoding
5. **Base64** encoding (again)

### Step 3: Use CyberChef

Navigate to **CyberChef** at the following link:
[CyberChef](https://gchq.github.io/CyberChef/)

#### Decode the flag using the decoding layers

### Step 5: Retrieve the Flag

After decoding through all the layers, the final output reveals the flag.

**Flag:** `Securinets{B64_H3x_B1n@ry_URL_B64}`

---

