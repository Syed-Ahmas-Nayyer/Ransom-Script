import os
import sys
from jnius import autoclass

# Import required Java classes
File = autoclass('java.io.File')
FileInputStream = autoclass('java.io.FileInputStream')
FileOutputStream = autoclass('java.io.FileOutputStream')
Cipher = autoclass('javax.crypto.Cipher')
SecretKeySpec = autoclass('javax.crypto.spec.SecretKeySpec')

def load_key(key_file_path):
    # Load the key from the file
    with open(key_file_path, 'rb') as key_file:
        return key_file.read()

def decrypt_file(file_path, key):
    try:
        # Read encrypted data from file
        input_file = FileInputStream(file_path)
        encrypted_data = bytearray(input_file.readAllBytes())
        input_file.close()

        # Decrypt data using AES algorithm
        cipher = Cipher.getInstance("AES")
        cipher.init(Cipher.DECRYPT_MODE, SecretKeySpec(key, "AES"))
        decrypted_data = cipher.doFinal(encrypted_data)

        # Write decrypted data back to file
        output_file = FileOutputStream(file_path.replace('.encrypted', ''))
        output_file.write(decrypted_data)
        output_file.close()

        print(f"File {file_path} decrypted successfully.")
    except Exception as e:
        print("Error:", e)

def main():
    # Check if directory path is provided
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]

    # Load the key from the file
    key_file_path = os.path.join(directory_path, 'key.bin')
    key = load_key(key_file_path)

    # Decrypt files in the specified directory
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path) and file_path.endswith('.encrypted'):
            decrypt_file(file_path, key)

if __name__ == "__main__":
    main()
