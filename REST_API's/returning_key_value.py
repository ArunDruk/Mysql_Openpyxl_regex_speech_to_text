####################################################################################################
# employees_info={
#     'Smitha':{
#         'Job_title':'Linux_Admin',
#         'salary':'1000$',
#         'Place' : 'NewYork City'
#     },
#     'Priya':{
#         'Job_title':'Automation_Engineer',
#         'salary':'5000$',
#         'Place' : 'California City'
#     }
# }
#
# def get_employee_name(emp_name):
#     if emp_name in employees_info.keys():
#         return employees_info.get(emp_name)
#     return "Sorry, Not able to find"
#
# print(get_employee_name('Priya'))
####################################################################################################
string="CTM Payroll Payables Batch 4756213 5965321"

if (("Payroll" and "Payable") in string):
    if("CTM" in string):
        print("Present")
else:
    print("Not Present")