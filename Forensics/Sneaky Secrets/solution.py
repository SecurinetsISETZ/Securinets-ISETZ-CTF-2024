repeated_line = "I WILL NOT BE SNEAKY"
flag = ""
with open('I WILL NOT BE SNEAKY.txt', 'r') as file:
    for line in file:
        line = line.strip()
        for i in range(min(len(repeated_line), len(line))):
            if line[i] != repeated_line[i]:
                print(f"found: {line[i]} at line {line} ")
                flag += line[i]
print(flag)
