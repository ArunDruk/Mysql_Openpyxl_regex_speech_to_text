from datetime import date, datetime

# L1=[]
# a=date.today()
# L1=str(a).split('-')
# print(L1)
# S1=L1[1]+'/'+L1[2]+'/'+L1[0]
# print(S1)

b=date.today().strftime("%m/%d/%Y")
print(b)
c=datetime.now().strftime("%M%S")
print(c)