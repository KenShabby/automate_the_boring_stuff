#! /usr/bin/local/python
# bullet_point-adder.py - adds bullet point markup to clipbord lists

import pyperclip as pc
text = pc.paste()

# separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all the lines in the list
    lines[i] = '* ' + lines[i] # add a star to the beginning of each line
text = '\n'.join(lines)

pc.copy(text)
