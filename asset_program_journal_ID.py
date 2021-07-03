
fo=open("Journal_program_asset.txt","r")
lines=fo.readlines()
print(type(lines))
print(lines[17][8:40])
print((lines[17][8:40]).strip())

# Assets A 459052 29690686 (CAI)
# Assets A 4544513 156643831 (MAN)