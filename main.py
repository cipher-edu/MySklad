import re 
str = ' 3 tavar za 200.99'
pat= r'\d+.\d'
match = re.search(pat, str)

print(match.group)