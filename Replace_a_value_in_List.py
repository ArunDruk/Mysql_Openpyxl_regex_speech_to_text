
L1=['11', '90', '34', '06', '79', '37', '75', '30', '00', '06', '09']
print(L1)
for i in range(len(L1)):
    if L1[i]=='00':  # Here if the value is '00', am replacing with '23'
        L1[i]='23'

print(L1)