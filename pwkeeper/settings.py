import os

KEY_LENGTH = 256
BLOCK_LENGTH = 16

DEFAULT_PASSWORD_LENGTH = 25
PASSWORD_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

DATA_DIR = os.path.join(os.path.expanduser('~'), '.pwkeeper')
KEY_FILE = os.path.join(DATA_DIR, 'key')
PASSWORD_FILE = os.path.join(DATA_DIR, 'data')
PASSWORD_FILE_BACKUP = os.path.join(DATA_DIR, 'data-last')
PASSWORD_FILE_PLAINTEXT = os.path.join(DATA_DIR, 'tmp')

PAD_BYTE = b'\x00'
CLIPBOARD_COMMAND = 'xsel'
