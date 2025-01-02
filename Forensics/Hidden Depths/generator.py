import itertools
base_string = "jR*S*_4*0wM"
wildcard_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_$*"
wildcard_positions = [i for i, char in enumerate(base_string) if char == '*']
combinations = itertools.product(wildcard_characters, repeat=len(wildcard_positions))
wordlist = []
for combo in combinations:
    chars = list(base_string)
    for pos, replacement in zip(wildcard_positions, combo):
        chars[pos] = replacement
    wordlist.append(''.join(chars))
with open("wordlist.txt", "w") as f:
    f.write("\n".join(wordlist))
print(f"Wordlist generated with {len(wordlist)} combinations and saved to 'wordlist.txt'.")
