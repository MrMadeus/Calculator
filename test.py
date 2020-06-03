import re

e = r'3254+155145*3462'

i = re.findall('\d+', e)

for s in i:
    print(s)

print(len(i))
