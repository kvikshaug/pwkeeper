import os

KEY_LENGTH = 256
BLOCK_LENGTH = 16

DEFAULT_PASSWORD_LENGTH = 25
KEY_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

KEY_FILE = os.path.dirname(__file__) + '/data/key'
ENCRYPTED_FILE = os.path.dirname(__file__) + '/data/data'
ENCRYPTED_BACKUP_FILE = os.path.dirname(__file__) + '/data/data-last'
DECRYPTED_FILE = os.path.dirname(__file__) + '/data/tmp'

EOT_CHAR = b'\x04'

DEFAULT_ARGUMENT = 'search'
