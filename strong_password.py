#!/usr/local/bin/python
# strong_password.py
# a program that will detect if a password has at least eight characters,
# contains upper and lowercase, and has at least one digit.

import re

test_passwords = ['foo', 'abc123', 'dontpani42', 'DontPani42', 'HF2', 'HF2fffff']


good_password_regex = re.compile(r'''
                                (?=(.*[A-Z]){2,})
                                (?=.*[0-9]{1,})
                                (?=.*[a-zA-Z0-9]{8,})
                                 ''',re.VERBOSE)

def test_password_list(list):
    for password in range(len(list)):
        if good_password_regex.search(list[password]):
            print(list[password] + ' is a good password')
        else:
            print('Nah, ' + list[password] + ' is shitty')

test_password_list(test_passwords)
