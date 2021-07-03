
############################################ Switch case Statement printing the Name of the weekday for the number mapped to it ########################################################
# def days(num):
#     days_name={
#                 1:'Monday',
#                 2:'Tuesday',
#                 3:'Wednesday',
#                 4:'Thursday',
#                 5:'Friday',
#                 6:'Saturday',
#                 7:'Sunday'
#     }
#     return days_name.get(num,"Invalid Number: Try between 1-7")
#
# print(days(4))
########################################################################################################################################################################################################
############################################ Switch case Statement for a Simple Calculator ############################################
# def math_operations(sym):
#     a=int(input("Enter the first num: "))
#     b=int(input("Enter the second num: "))
#     math_signs={
#             '+':a+b,
#             '-':a-b,
#             '*':a*b
#     }
#     return math_signs.get(sym,"Invalid Symbol: Try only '+ - *' ")
#
# user_sym=input("Enter the Math Operation: + - * :  ")
# print(math_operations(user_sym))
########################################################################################################################################################################################################
############################################ Switch case Statement to return person name for the Birthday date ############################################
def func1(i):
    switch_statement={
        "30-aug":"Kiran's Birthday",
        "30-sep":"Arun's Birthday",
        "24-jun":"Daddy's Birthday"
    }
    return switch_statement.get(i,"No data found")


print(func1("30-may"))
####################################################################################################################################
