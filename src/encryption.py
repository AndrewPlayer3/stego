from cryptography.fernet import Fernet

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