#!/usr/bin/env python
from Crypto.Cipher import AES
import json
import os
import optparse
import random

KEY_LENGTH = 256
BLOCK_LENGTH = 16

DEFAULT_PASSWORD_LENGTH = 25
KEY_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

KEY_FILE = os.path.dirname(__file__) + '/key'
ENCRYPTED_FILE = os.path.dirname(__file__) + '/data'
DECRYPTED_FILE = os.path.dirname(__file__) + '/tmp'

EOT_CHAR = b'\x04'

options = None
arguments = None
DEFAULT_ARGUMENT = 'search'

def main():
    if arguments[0] == 'generate':
        generate()
    elif arguments[0] == 'save':
        save()
    elif arguments[0] == 'edit':
        edit()

def save():
    bytes = multiple_of(read_file(DECRYPTED_FILE), BLOCK_LENGTH)
    iv, encrypted = encrypt(bytes)
    write_file(ENCRYPTED_FILE, iv + encrypted)
    os.unlink(DECRYPTED_FILE)
    print("Removed %s" % os.path.abspath(DECRYPTED_FILE))
    print("Wrote encrypted data to %s" % os.path.abspath(ENCRYPTED_FILE))

def edit():
    bytes = decrypt()
    write_file(DECRYPTED_FILE, bytes)
    print("Plaintext written to: %s" % os.path.abspath(DECRYPTED_FILE))

def read_file(file):
    f = open(file, 'rb')
    b = f.read()
    f.close()
    return b

def write_file(file, bytes):
    f = open(file, 'wb')
    f.write(bytes)
    f.close()

def get_cipher(iv, text):
    try:
        key = open(KEY_FILE, 'rb').read()
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

def generate():
    if len(arguments) == 2:
        length = int(arguments[1])
    else:
        length = DEFAULT_PASSWORD_LENGTH
    for i in range(length):
        print(random.choice(KEY_CHARS), end='')
    print()

if __name__ == '__main__':
    p = optparse.OptionParser()
    options, arguments = p.parse_args()
    if len(arguments) == 0:
        arguments.append(DEFAULT_ARGUMENT)
    main()
