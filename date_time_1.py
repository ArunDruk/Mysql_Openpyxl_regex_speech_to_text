###################################################################################################
# from datetime import datetime
#
# today_date=datetime.now().strftime("%d-%b-%Y")
# present_date=datetime.now().strftime("%Y%m%d%H%M%S%f")
# print(present_date)
#
# current_date=datetime.now()
#
# print("Current year =", current_date.year)
# print("Current Month =",  str(current_date.month)+","+current_date.strftime("%b"))
# print("Current Day = ", current_date.day)
# print("Current Hour = ", current_date.hour)
# print("Current Min = ", current_date.minute)
# print("Current Sec = ", current_date.second)
# print("Current Micro-Sec = ", current_date.microsecond)

###################################################################################################
from datetime import datetime

now1=datetime.now().strftime("%d(DD)-%m(MM)-%Y(yyyy) %H(hr):%M(min):%S(ss):%f(micro-sec) ")
print(now1)


