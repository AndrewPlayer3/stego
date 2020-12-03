import numpy as np
from PIL import Image
from cryptography.fernet import Fernet
import encryption as en
import io
import os

# Encoding using least significant bit method, where the message is encrypted
# before being entered into the image.
# Supports PNGs using RGB or RGBA
# Source Tutorial: https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2
def encode(key_path, img_path, message, channel):
    img = Image.open(img_path, 'r')
    width, height = img.size
    img_array = np.array(list(img.getdata()))

    channels = 3 if img.mode == 'RBG' else 4
    total_pixels = img_array.size//channels
    message = en.encrypt(key_path, message) + "$iM913"
    
    # Join all the ascii values into a string, formatted to binary.
    bits = ''.join([format(ord(char), "08b") for char in message])

    if len(bits) > total_pixels:
        return False
    else:
        index = 0
        for pxl in range(total_pixels):
            if index < len(bits):
                # Add the message bits at index to the last 8 bits of pixel pxl in the "channel" channel
                img_array[pxl][channel] = int(bin(img_array[pxl][channel])[2:9] + bits[index], 2)
                index += 1

        img_array = img_array.reshape(height, width, channels)
        enc_img = Image.fromarray(img_array.astype('uint8'), img.mode)
        enc_img.save(img_path)
        return True

# Decoding using least significant bit method, where the message is decrypted
# after being extracted from the image.
# Supports PNGs using RGB or RGBA
# Source Tutorial: https://medium.com/swlh/lsb-image-steganography-using-python-2bbbee2c69a2
def decode(key_path, img_path, channel):

    img = Image.open(img_path, 'r')
    img_array = np.array(list(img.getdata()))

    channels = 3 if img.mode == 'RBG' else 4
    total_pixels = img_array.size//channels

    bits = ""
    for pxl in range(total_pixels):
        bits += (bin(img_array[pxl][channel])[2:][-1])

    bits = [bits[i:i+8] for i in range(0, len(bits), 8)]

    message = ""
    for i in range(len(bits)):
        if message[-6:] == "$iM913":
            break
        else:
            message += chr(int(bits[i], 2))
    if "$iM913" in message:
        return "Message: \n"  + "--------------\n\n" + en.decrypt(key_path, message[:-6])
    else:
        return "No Message Found"