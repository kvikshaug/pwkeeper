from Crypto.Cipher import AES
import os

from settings import *

def get_cipher(iv, text):
    try:
        key = open(KEY_FILE, 'rb').read().strip()
    except IOError:
        key = input(text)
    return AES.new(key, AES.MODE_CBC, iv)

def encrypt(bytes):
    iv = os.urandom(16)
    c = get_cipher(iv, "Please enter an encryption key: ")
    return (iv, c.encrypt(bytes))

def decrypt():
    bytes = open(ENCRYPTED_FILE, 'rb').read()
    c = get_cipher(bytes[:16], "Please enter the decryption key: ")
    return c.decrypt(bytes[16:]).strip(b'\x04')

def multiple_of(bytes, length):
    if len(bytes) % length == 0:
        return bytes
    else:
        return bytes + (EOT_CHAR * (length - (len(bytes) % length)))
