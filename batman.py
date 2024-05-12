import os
import sys
import secrets
from jnius import autoclass

# Import required Java classes
File = autoclass('java.io.File')
FileInputStream = autoclass('java.io.FileInputStream')
FileOutputStream = autoclass('java.io.FileOutputStream')
Cipher = autoclass('javax.crypto.Cipher')
SecretKeySpec = autoclass('javax.crypto.spec.SecretKeySpec')

def generate_key():
    # Generate a random 128-bit AES key
    return secrets.token_bytes(16)

def save_key(key, key_file_path):
    # Save the key to a file
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

def encrypt_file(file_path, key):
    try:
        # Read data from file
        input_file = FileInputStream(file_path)
        data = bytearray(input_file.readAllBytes())
        input_file.close()

        # Encrypt data using AES algorithm
        cipher = Cipher.getInstance("AES")
        cipher.init(Cipher.ENCRYPT_MODE, SecretKeySpec(key, "AES"))
        encrypted_data = cipher.doFinal(data)

        # Write encrypted data back to file
        output_file = FileOutputStream(file_path + '.encrypted')
        output_file.write(encrypted_data)
        output_file.close()

        print(f"File {file_path} encrypted successfully.")
    except Exception as e:
        print("Error:", e)

def main():
    # Check if directory path is provided
    if len(sys.argv) != 2:
        print("Usage: python encrypt.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]

    # Generate a random AES key
    key = generate_key()
    # Save the key to a file
    key_file_path = os.path.join(directory_path, 'key.bin')
    save_key(key, key_file_path)

    # Encrypt files in the specified directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)

if __name__ == "__main__":
    main()
