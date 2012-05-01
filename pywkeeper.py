#!/usr/bin/env python
import json
import os
import optparse
import random

from crypto import *
from file_io import *
from settings import *

options = None
arguments = None

def main():
    if arguments[0] == 'generate':
        generate()
    elif arguments[0] == 'save':
        save()
    elif arguments[0] == 'edit':
        edit()

def save():
    try:
        bytes = multiple_of(read_file(DECRYPTED_FILE), BLOCK_LENGTH)
    except IOError:
        print("There's no plaintext file to save!")
        print("Tried %s" % os.path.abspath(DECRYPTED_FILE))
        return
    iv, encrypted = encrypt(bytes)
    write_file(ENCRYPTED_FILE, iv + encrypted)
    os.unlink(DECRYPTED_FILE)
    print("Removed plaintext and saved encrypted file.")

def edit():
    bytes = decrypt()
    write_file(DECRYPTED_FILE, bytes)
    print("Plaintext written to: %s" % os.path.abspath(DECRYPTED_FILE))

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
