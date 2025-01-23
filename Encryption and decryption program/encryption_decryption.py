from cryptography.fernet import Fernet

# Generate and save a key
def generate_key(file_name="secret.key"):
    key = Fernet.generate_key()
    with open(file_name, "wb") as key_file:
        key_file.write(key)
    print(f"Key saved to {file_name}")

# Load the encryption key
def load_key(file_name="secret.key"):
    with open(file_name, "rb") as key_file:
        return key_file.read()

# Encrypt a text message
def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text

# Decrypt a text message
def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

# Encrypt a file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File encrypted to {file_path}.enc")

# Decrypt a file
def decrypt_file(encrypted_file_path, key, output_file_path=None):
    fernet = Fernet(key)
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    output_file_path = output_file_path or encrypted_file_path.replace(".enc", "")
    with open(output_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f"File decrypted to {output_file_path}")

# Main function for user interaction
def main():
    print("Choose an option:")
    print("1. Generate encryption key")
    print("2. Encrypt text")
    print("3. Decrypt text")
    print("4. Encrypt file")
    print("5. Decrypt file")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        generate_key()
    elif choice in ["2", "3", "4", "5"]:
        key_file = input("Enter the key file path (default: secret.key): ") or "secret.key"
        key = load_key(key_file)

        if choice == "2":
            text = input("Enter text to encrypt: ")
            encrypted = encrypt_text(text, key)
            print(f"Encrypted text: {encrypted}")
        elif choice == "3":
            encrypted_text = input("Enter text to decrypt: ").encode()
            decrypted = decrypt_text(encrypted_text, key)
            print(f"Decrypted text: {decrypted}")
        elif choice == "4":
            file_path = input("Enter the file path to encrypt: ")
            encrypt_file(file_path, key)
        elif choice == "5":
            encrypted_file_path = input("Enter the encrypted file path to decrypt: ")
            output_file_path = input("Enter the output file path (optional): ") or None
            decrypt_file(encrypted_file_path, key, output_file_path)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()


