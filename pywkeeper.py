from Crypto.Cipher import AES
import json
import os

KEY_LENGTH = 256
BLOCK_LENGTH = 16

KEY_FILE = 'key'
ENCRYPTED_FILE = 'data'
DECRYPTED_FILE = 'tmp'

EOT_CHAR = '\x04'

def get_cipher(iv):
    try:
        key = open(KEY_FILE, 'rb').read()
    except IOError:
        key = input("Please enter the decryption key: ")
    return AES.new(key, AES.MODE_CBC, iv)

def encrypt():
    bytes = multiple_of(open(DECRYPTED_FILE, 'rt').read().encode(), BLOCK_LENGTH)
    iv = os.urandom(16)
    c = get_cipher(iv)
    return (iv, c.encrypt(bytes))

def decrypt():
    bytes = open(ENCRYPTED_FILE, 'rb').read()
    c = get_cipher(bytes[:16])
    return c.decrypt(bytes).decode('utf-8')

def multiple_of(bytes, length):
    if len(bytes) % length == 0:
        return bytes
    else:
        return bytes + (EOT_CHAR * (length - (len(bytes) % length))).encode()
