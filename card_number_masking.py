s="6531 1341 5172 5592"
L=[0,1,16,17,18]
new_s=""

for i in range(len(s)):
    if i in L:
        new_s=new_s+s[i]
    elif s[i] == " ":
        new_s=new_s+' '
    else:
        new_s=new_s+ 'X'

print("Entered card number: "+s)

print("The card number you have entered is: "+new_s)