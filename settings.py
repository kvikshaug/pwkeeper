import os

KEY_LENGTH = 256
BLOCK_LENGTH = 16

DEFAULT_PASSWORD_LENGTH = 25
KEY_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

DIR = os.path.dirname(__file__) + '/data/'
KEY_FILE =              DIR + 'key'
ENCRYPTED_FILE =        DIR + 'data'
ENCRYPTED_BACKUP_FILE = DIR + 'data-last'
DECRYPTED_FILE =        DIR + 'tmp'

EOT_CHAR = b'\x04'
CLIPBOARD_COMMAND = 'xclip -i'
