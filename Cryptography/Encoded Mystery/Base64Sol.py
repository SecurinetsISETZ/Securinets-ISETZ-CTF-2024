import base64

def decode_until_flag(file_path):
    with open(file_path, 'r') as file:
        encoded_data = file.read().strip()

    while True:
        # Decode the Base64 data
        decoded_data = base64.b64decode(encoded_data).decode('utf-8', errors='ignore')
        
        # Check if the decoded content matches a flag format
        if '{' in decoded_data and '}' in decoded_data and '_' in decoded_data :
            print("Flag found:", decoded_data)
            break
        elif len(decoded_data) % 4 !=0:
            print("Flag not found:", decoded_data)
            break
        else:
            encoded_data = decoded_data  # Update for next round of decoding

# Example usage
file_path = "flag.txt"  # Replace with your file's path
decode_until_flag(file_path)
