# Ransom-Script

python encrypt.py /path/to/your/directory
python decrypt.py /path/to/your/directory

Replace "/path/to/your/directory" with the directory path you want to encrypt or decrypt. Make sure to run the encryption script before the decryption script, and both scripts should be run on the same directory.

The key is generated using the generate_key() function and is then saved to a file named 'key.bin' in the same directory where the encrypted files are located (directory_path). This file will contain the randomly generated AES key.

You can find the key in the file 'key.bin' located in the same directory where the encrypted files are stored. However, it's important to note that in a real-world scenario, you would want to securely manage and store this key to prevent unauthorized access. Additionally, you should avoid exposing the key to users or storing it in an insecure manner.
