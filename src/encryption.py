from cryptography.fernet import Fernet

# Fernet is symmetric encryption which guarantees that no one can read the 
# message without the private key. Therefore, anyone who may read the stego
# message must also have the key.

def gen_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt(key_path, message):
    key = open(key_path,"rb").read()
    message = message.encode('ascii')
    f = Fernet(key)
    message = f.encrypt(message)
    return str(message)

def decrypt(key_path, encrypted_message):
    key = open(key_path,"rb").read()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message[2:len(encrypted_message)-1].encode('ascii'))
    return decrypted_message.decode('ascii')