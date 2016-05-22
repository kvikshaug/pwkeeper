# pwkeeper

Terminal-based password manager.

* Store all your passwords in `~/.pwkeeper`
* Search for stored passwords and add matches to the clipboard
* Encrypt the file for safe distribution

## Install

    $ pip install pwkeeper

## Usage

First time: Initialize your password file with a randomly generated encryption key:

    $ pw

Create a new password:

    $ pw add
    Usage: github.com
    Username: ghuser
    Password [HFXuGJv95sjL5ZmfcEfdtBSi9]:
    Previous password file backed up at: /home/user/.pwkeeper/data-last
    New password saved in /home/user/.pwkeeper/data

Later, retrieve it to the clipboard:

    $ pw github
    1. github
       Username: 'ghuser'

Edit the password JSON in cleartext:

    $ pw edit
    Plaintext written to: /home/user/.pwkeeper/tmp
    $ vim /home/user/.pwkeeper/tmp
    $ pw save
    Previous password file backed up at: /home/user/.pwkeeper/data-last
    Removing: /home/user/.pwkeeper/tmp

## Dependencies

A command which writes input to the clipboard, like `xsel` or `xclip`.
