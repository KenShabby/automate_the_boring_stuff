import re

def my_strip(string):
    strip_regex = re.compile(r'^\s+|\s+$')
    print(strip_regex.sub('', string))
    
test_strings = ['  foo', 'bar   ', '   both   ']

for s in range(len(test_strings)):
    my_strip(test_strings[s])
