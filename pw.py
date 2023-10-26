#!/usr/bin/env python3
# password locker

PASSWORDS = {"email": "Kidiavayi1317"}

import sys, pyperclip

if len(sys.argv) < 2:
    print(f"Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard")
else:
    print(f"There is no account named {account}")
