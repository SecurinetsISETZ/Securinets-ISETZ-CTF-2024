# Task: Sneaky Secrets

## Description
> I received this mysterious file, but its purpose remains unknown.  
> Can you uncover its hidden truth?

> Author: ADX2K

The challenge provides a text file containing repeated lines of text. However, some characters in these lines differ, hinting at a hidden flag. Your mission is to uncover the flag.

---

## Solution

### Step 1: Analyze the File
The provided file contains repeated lines but the flag caracters are hidden between the repeated line caracters :<br>
Exemple : 
```
I WILL NOT BE SNEAKY
I WILL NOT BE SNEAKY
I WILL NOT BE SNEAKY
I WILL NOT SE SNEAKY    # We have the first caracter of the flag hidden here "S"
I WILL NOT BE SNEAKY
I WILL NOT BE SNEAKY
I WILL NOT BE SNEAKY
```
So we need automate this with python to extract the full flag: 
```bash
repeated_line = "I WILL NOT BE SNEAKY"
flag = ""
with open('I WILL NOT BE SNEAKY.txt', 'r') as file:
    for line in file:
        line = line.strip()
        for i in range(min(len(repeated_line), len(line))):
            if line[i] != repeated_line[i]:
                print(f"found: {line[i]} at line {line}")
                flag += line[i]
print(flag)
```
Output:
```
found: S at line I WILL NOT SE SNEAKY
found: e at line I WILL NOT BE SNEAeY
found: c at line I WILL NOc BE SNEAKY
found: u at line I WILL NuT BE SNEAKY
found: r at line I WILL NOT BE SNrAKY
found: i at line I WILL NOT BE SNEiKY
found: n at line I WILL NOT BE SnEAKY
found: e at line I WILL NOe BE SNEAKY
found: t at line I WILL NOT tE SNEAKY
found: s at line I WILL NOs BE SNEAKY
found: { at line I WILL NOT {E SNEAKY
found: S at line I WILL NOT BE SNEAKS
found: 0 at line I WILL NOT BE S0EAKY
found: r at line I WILL NOr BE SNEAKY
found: r at line I WILL NOT rE SNEAKY
found: y at line I WIyL NOT BE SNEAKY
found: _ at line I WILL _OT BE SNEAKY
found: B at line I WILL NOT BE SBEAKY
found: u at line I WILL NuT BE SNEAKY
found: t at line I WILL NOT BE SNEtKY
found: _ at line I _ILL NOT BE SNEAKY
found: 1 at line I 1ILL NOT BE SNEAKY
found: _ at line I WILL NO_ BE SNEAKY
found: 5 at line I WILL NOT BE SNEA5Y
found: n at line I nILL NOT BE SNEAKY
found: 3 at line I W3LL NOT BE SNEAKY
found: @ at line @ WILL NOT BE SNEAKY
found: k at line I WkLL NOT BE SNEAKY
found: 3 at line I WILL NOT BE S3EAKY
found: d at line I WILL NOT BE SNEAKd
found: } at line I WIL} NOT BE SNEAKY
```
Flag: ```Securinets{S0rry_But_1_5n3@k3d}```
