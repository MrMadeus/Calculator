import re

e = '3254+155145*3462'

i = re.findall(r'\d*', e)

for s in i:
    print(s)

print(len(i))
