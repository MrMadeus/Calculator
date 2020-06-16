import re

e = r'3254+155145*3462'

i = re.findall('\d+', e)
s = re.findall('\D+', e)

j = 0
while j <= len(i):
    print(i[j], s[j])
    j = j + 1

print(len(i), len(s))
