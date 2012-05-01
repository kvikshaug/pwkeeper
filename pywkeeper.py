#!/usr/bin/env python
import json, os, optparse, random, shutil

from crypto import *
from file_io import *
from settings import *

options = None
arguments = None

def add():
    passwords = json.loads(decrypt().decode('utf-8'))
    usage = input("Usage: ")
    user = input("Username: ")
    rand = generate()
    password = input("Password [%s]: " % rand)
    password = rand if password == '' else password
    passwords.append({
        'usage': usage,
        'user': user,
        'passwords': [password]
    })
    encrypt_and_save(json.dumps(passwords).encode())
    print("Added new password to encrypted file.")

def search(phrases):
    def matches(password, phrase):
        return phrase.lower() in password['usage'].lower() or phrase.lower() in password['user'].lower()
    passwords = json.loads(decrypt().decode('utf-8'))
    hits = []
    for password in passwords:
        match = True
        for phrase in phrases:
            if not matches(password, phrase):
                match = False
                break
        if match:
            hits.append(password)
    for i in range(1, len(hits)+1):
        user = hits[i-1]['user']
        if user != '':
            user = "\n   Brukernavn: '%s'" % user
        print("%s. %s%s" % (i, hits[i-1]['usage'], user))
        if options.p:
            for password in hits[i-1]['passwords']:
                print("   '%s'" % password)
        elif len(hits[i-1]['passwords']) > 1:
            print("   (%s passwords)" % len(hits[i-1]['passwords']))
    p = os.popen('xsel', 'w')
    if len(hits) > 0:
        p.write(hits[0]['passwords'][0])
    else:
        print("No hits.")
    p.close()

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
        bytes = read_file(DECRYPTED_FILE, 'rt').encode()
    except IOError:
        print("There's no plaintext file to save!")
        print("Tried %s" % os.path.abspath(DECRYPTED_FILE))
        return
    encrypt_and_save(bytes)
    os.unlink(DECRYPTED_FILE)
    print("Removed plaintext, backed up and saved encrypted file.")

def encrypt_and_save(bytes):
    shutil.copyfile(ENCRYPTED_FILE, ENCRYPTED_BACKUP_FILE)
    iv, encrypted = encrypt(multiple_of(bytes, BLOCK_LENGTH))
    write_file(ENCRYPTED_FILE, 'wb', iv + encrypted)

def generate():
    length = options.n if options.n else DEFAULT_PASSWORD_LENGTH
    pw = ''
    for i in range(length):
        pw += random.choice(KEY_CHARS)
    return pw

def initialize():
    options.n = 32 # Pretend user set length to 32 for generate()
    print()
    print("Welcome! Looks like this is your first time using Pywkeeper.")
    print("===============================================================")
    print("You'll need to give a 16/24/32-character long key used to encrypt your passwords.")
    print("Here's a randomly generated one: %s" % generate())
    print()
    print("Note: Every time you save to the encrypted file, you can specify a new key.")
    print("Warning: If you lose this key, you lose all the passwords saved in the encrypted file.")
    print()
    iv, encrypted = encrypt(multiple_of('[]'.encode(), BLOCK_LENGTH))
    write_file(ENCRYPTED_FILE, 'wb', iv + encrypted)
    print()
    print("Passwords are now stored in '%s'." % ENCRYPTED_FILE)
    print("Check out the github wiki at https://github.com/murr4y/pywkeeper/wiki for usage help.")
    print()
    print("DON'T LOSE YOUR DECRYPTION KEY!")

if __name__ == '__main__':
    p = optparse.OptionParser(usage="usage: %prog [options] [add|edit|save|generate|<search>]")
    p.add_option("-n", type='int', help="With 'generate', the length of the generated password")
    p.add_option("-p", help="Show passwords when searching", action='store_true')
    options, arguments = p.parse_args()

    if not os.path.exists(DIR):
        os.makedirs(DIR)
        initialize()
        exit()

    if len(arguments) == 0:
        p.print_help()
        exit()

    if arguments[0] == 'add':        add()
    elif arguments[0] == 'edit':     edit()
    elif arguments[0] == 'save':     save()
    elif arguments[0] == 'generate': print(generate())
    else:                            search(arguments)
