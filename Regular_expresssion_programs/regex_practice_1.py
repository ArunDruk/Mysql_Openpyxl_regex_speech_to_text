import re
txt="""
    This is to bring cat
    to bringmat
    pat
    bat
    1at
    +at
    """
pattern=re.compile(r'(\w?\s?)*?[a-z]+at')
matches=pattern.finditer(txt)

for match in matches:
    print(match)
