from datetime import date
from datetime import datetime
import re

s="MAN GLB US|Payroll|MAN:Payroll|06/10/2020|USD|||2310.60| ||||||||||||||||JAN-2020|00403|612030|1003|000|156|00000|0000||||FLX 0120||||||Rebill 06/10/2020"
#
# matches=re.finditer(r'[A-Z]{3}-\d{4}',s)
# # print(matches)
# for match in matches:
#     print(match.group())

# month_year=date.today().strftime("%b-%y")
# month_year=str(month_year).upper()
# print(month_year)

month_year=datetime.now().strftime("%b-%Y")
month_year=str(month_year).upper()
new_str=re.sub(r'[A-Z]{3}-\d{4}',month_year,s)
#
print(new_str)
print(month_year)
