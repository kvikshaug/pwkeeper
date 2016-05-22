#!/usr/bin/env python
import optparse
import os

from models import PWKeeper
import settings

if __name__ == '__main__':
    p = optparse.OptionParser(usage="usage: %prog [options] [add|edit|save|generate|<search>]")
    p.add_option("-n", type='int', help="With 'generate', the length of the generated password")
    p.add_option("-p", help="Show passwords when searching", action='store_true')
    options, arguments = p.parse_args()

    if not os.path.exists(settings.DIR):
        print("Initializing new data directory in %s ..." % settings.DIR)
        key = PWKeeper.initialize()

        print()
        print("Generated AES key: %s" % key)
        print("AES key file:      %s" % settings.KEY_FILE)
        print("Password file:     %s" % settings.PASSWORD_FILE)
        exit()

    if len(arguments) == 0:
        p.print_help()
        exit()

    pw = PWKeeper()

    if arguments[0] == 'add':
        pw.add_password()
    elif arguments[0] == 'edit':
        pw.edit_plaintext()
    elif arguments[0] == 'save':
        pw.save_plaintext()
    elif arguments[0] == 'generate':
        print(PWKeeper.generate(options.n or settings.DEFAULT_PASSWORD_LENGTH))
    else:
        pw.search(arguments, options.p)
