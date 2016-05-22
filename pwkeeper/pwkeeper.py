#!/usr/bin/env python
import argparse
import os

from .models import PWKeeper
from . import settings

def main():
    parser = argparse.ArgumentParser(description="Manage your passwords with pwkeeper.")
    parser.add_argument('-n', type=int, help="With 'generate', the length of the generated password")
    parser.add_argument('-p', action='store_true', help="Show passwords in cleartext when searching")
    parser.add_argument('command', nargs='*', help='[add|edit|save|generate|<search>]')
    args = parser.parse_args()

    if not os.path.exists(settings.DATA_DIR):
        print("Initializing new data directory in %s ..." % settings.DATA_DIR)
        key = PWKeeper.initialize()

        print()
        print("Generated AES key: %s" % key)
        print("AES key file:      %s" % settings.KEY_FILE)
        print("Password file:     %s" % settings.PASSWORD_FILE)
        exit()

    if not args.command:
        parser.print_help()
        exit()

    pw = PWKeeper()

    if args.command[0] == 'add':
        pw.add_password()
    elif args.command[0] == 'edit':
        pw.edit_plaintext()
    elif args.command[0] == 'save':
        pw.save_plaintext()
    elif args.command[0] == 'generate':
        print(PWKeeper.generate(args.n or settings.DEFAULT_PASSWORD_LENGTH))
    else:
        pw.search(args.command, args.p)

if __name__ == '__main__':
    main()
