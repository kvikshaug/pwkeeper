#!/usr/bin/env python
import json
import os
import optparse
import random
import shutil

from crypto import *
from file_io import *
from settings import *

options = None
arguments = None

def edit():
    bytes = decrypt()
    try:
        bytes = json.dumps(json.loads(bytes.decode('utf-8')), indent=4, ensure_ascii=False)
    except ValueError:
        print("Warning: Couldn't parse the content as JSON. Skipping pretty-printing.")
    write_file(DECRYPTED_FILE, 'wt', bytes)
    print("Plaintext written to: %s" % os.path.abspath(DECRYPTED_FILE))

def save():
    try:
        bytes = multiple_of(read_file(DECRYPTED_FILE, 'rt').encode(), BLOCK_LENGTH)
    except IOError:
        print("There's no plaintext file to save!")
        print("Tried %s" % os.path.abspath(DECRYPTED_FILE))
        return
    shutil.copyfile(ENCRYPTED_FILE, ENCRYPTED_BACKUP_FILE)
    iv, encrypted = encrypt(bytes)
    write_file(ENCRYPTED_FILE, 'wb', iv + encrypted)
    os.unlink(DECRYPTED_FILE)
    print("Removed plaintext, backed up and saved encrypted file.")

def generate():
    length = options.n if options.n else DEFAULT_PASSWORD_LENGTH
    for i in range(length):
        print(random.choice(KEY_CHARS), end='')
    print()

if __name__ == '__main__':
    p = optparse.OptionParser(usage="usage: %prog [options] [edit|save|generate]")
    p.add_option("-n", type='int', help="With 'generate', the length of the generated password")
    options, arguments = p.parse_args()
    if len(arguments) == 0:
        arguments.append(DEFAULT_ARGUMENT)

    if arguments[0] == 'edit':       edit()
    elif arguments[0] == 'save':     save()
    elif arguments[0] == 'generate': generate()
