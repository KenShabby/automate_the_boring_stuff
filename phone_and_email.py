#!/usr/local/bin/python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phone_regex = re.compile(r'''(
     (\d{3}|\(\d{3}\))?             # area code
     (\s|-|\.)                     # optional delimiter
     (\d{3})                        # prefix
     (\s|-|\.)                      # optional delimiter
     (\d{4})                        # last four digits
     (\s*(ext|x|ext.)\s*(\d{2,5}))? # optional extension
     )''', re.VERBOSE)              # verbose allows inline comments

# TODO: Create email regex.
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # Username portion
     @                  # at
    [a-zA-Z0-9.-]+      # domain name
     (\.[a-zA-z]{2,4})  # dot whatevs
     )''', re.VERBOSE)

# TODO: Find matches in clipboard text.
clipy_text = str(pyperclip.paste())

matches = []
for groups in phone_regex.findall(clipy_text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(clipy_text):       
    matches.append(groups[0])

# TODO: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
     print('No phone numbers or addresses found.')
