# Task: Lost Transmission

## Description
> I intercepted this unusual message, but its meaning is completely obscure.  
> Can you decode it?  
> **Flag format**: Securinets{}
 
> **Author**: ADX2K

---

## Solution

The challenge provides a sequence of characters that resembles Morse code. The goal is to decode the message and uncover the hidden flag.

### Step 1: Analyze the Provided Code
The given code:

```
-- ----- .-. ... . ..--.- -.-. ----- -.. ...-- ..--.- .-- ----- .-. -.- ... ..--.- .-- .---- - .... ..--.- -.. ----- - ... ..--.- .--.-. -. -.. ..--.- -.. .--.-. ... .... ...-- ...
```

Clearly follows the structure of Morse code with dots (`.`) and dashes (`-`), separated by spaces.

### Step 2: Decode Morse Code
We use online tools, such as **[dCode's Morse Code Decoder](https://www.dcode.fr/morse-code)**, to simplify decoding. Alternatively, manual decoding can be performed using a Morse code reference table.

### Step 3: Getting the Flag
Reassemble the decoded text, ensuring it matches the specified flag format: `Securinets{}`.

Flag:
```
Securinets{M0RSE_C0D3_W0RKS_W1TH_D0TS_@ND_D@SH3S}
```


