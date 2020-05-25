# L1=["k1","k2","k3"]
# L2=["v1","v2","v3"]
# D1=dict(zip(L1,L2))
#
# print(D1)
# print(type(D1))


# Lines=[1,2,3,4]
# L2=["v1","v2","v3","v4"]
# D2=dict(zip(L2,line)) for line in Lines
#
# print(D2,type(D2))

# conf_msg= "Request id is: 162009256"
#
# req_id= "".join(i for i in conf_msg if i.isdigit())
#
# print(req_id)

from datetime import datetime,timedelta

a=datetime.now()
# d = datetime.strptime('18-05-2020', '%d-%m-%Y') #'%Y-%m-%d'
# t = timedelta((12 - d.weekday()) % 7)
#
# print(d + t)
# print((d + t).strftime('%d-%m-%Y'))
# print(sat_date)
today_date=datetime.strftime('%d-%m-%Y')
# today_date=a.strftime('%d-%m-%Y')
print("Today's date is: ",today_date)
