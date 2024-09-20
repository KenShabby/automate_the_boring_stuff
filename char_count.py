import pprint

message = 'It was a cold, dark night in April.  The clock had just struck thirteen'

count = {}

for c in message:
    count.setdefault(c, 0)
    count[c] = count[c] + 1

pprint.pprint(count)    
