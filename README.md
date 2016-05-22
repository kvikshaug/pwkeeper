# Pywkeeper

Pywkeeper stores all your passwords in an encrypted file.

You must remember your **encryption key**, but no other passwords, as they are stored safely and can be retrieved at any time.

This is, in my opinion, the best way to manage personal passwords. It lets you have long and complicated passwords, and different passwords for different services, without having to remember them.

Pywkeeper is thoroughly documented at the [github wiki](https://github.com/murr4y/pywkeeper/wiki).

## Dependencies

By default, pywkeeper depends on `xclip` in order to set the clipboard. This can be changed in the settings, to any command that accepts a string on stdin and writes that to the clipboard.

As for python modules, it depends on [PyCrypto](https://www.dlitz.net/software/pycrypto/).

Pywkeeper is written for Python 3.

## Todo: Phone app

I plan to develop a phone app. This will require an additional synchronization feature, but otherwise it should work fairly similar to the terminal app.
