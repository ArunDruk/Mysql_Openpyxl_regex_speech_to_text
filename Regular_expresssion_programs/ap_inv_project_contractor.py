
import re
import random
filename="apinv_cai_zerochaos_AUTO.csv"

repl= "TestInv"+str(random.randint(1111,9999))

with open(filename,'r+') as fr:
    data=fr.read()
    new_data=re.sub(r'TestInv\d{4}',repl,data)
    fr.seek(0)
    fr.truncate()
    fr.write(new_data)
#     # print(type(new_data),new_data)
