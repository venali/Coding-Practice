Encryption and decryption program: Create a program with the ability to decrypt and encrypt text and files. It can use an existing algorithm or you can create a basic one.
Below is an example Python program that can encrypt and decrypt both text and files using the popular `Fernet` encryption from the `cryptography` library. 
This ensures strong encryption and ease of use.

How It Works
1. Key Management:
   - The `generate_key()` function generates a secure key and saves it to a file (`secret.key` by default).
   - The `load_key()` function reads this key for encryption or decryption.  

2. Text Encryption/Decryption:
   - `encrypt_text()` encrypts a given plaintext using the loaded key.
   - `decrypt_text()` decrypts the encrypted text back into plaintext.  

3. File Encryption/Decryption:
   - `encrypt_file()` reads a file, encrypts its contents, and writes an `.enc` encrypted version.
   - `decrypt_file()` reads the `.enc` file and restores the original content.

4. Interactive CLI:
   - Users can choose from options to generate a key, encrypt or decrypt text, or handle file encryption/decryption.


Usage
1. Run the program:
   ```bash
   python encryption_decryption.py
   ```

2. Generate a key:
   ```
   Choose an option:
   1. Generate encryption key
   ...
   Enter your choice: 1
   Key saved to secret.key
   ```

3. Encrypt a text:
   ```
   Enter your choice: 2
   Enter the key file path (default: secret.key): 
   Enter text to encrypt: Hello, world!
   Encrypted text: b'gAAAA...'
   ```

4. Encrypt a file:
   ```
   Enter your choice: 4
   Enter the key file path (default: secret.key): 
   Enter the file path to encrypt: example.txt
   File encrypted to example.txt.enc
   ```