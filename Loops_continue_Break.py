
########################################################################################################################################################################################################
##################################################### # Illustration of Continue statement ###############################################
T1=("Rock","John","Ajith","Arun","Dhoni")

for i in T1:
    if len(i) == 4:
        print(i)
        continue
        print("Thanks")  #The continue statement skips the code that comes after it, and the control is passed back to the start for the next iteration.

########################################################################################################################################################################################################
##################################################### # Illustration of Break statement ###############################################


T1=("Rock","Ajith","Dhoni")
T2=("John","Cena","Brock")

for i in T1:
    for j in T2:
        if i != "Dhoni":
            print(i,"\t",j)
        break   # A break statement, when used inside the loop, will terminate the loop and exit. If used inside nested loops, it will break out from the current loop.

########################################################################################################################################################################################################
# A break statement, when used inside the loop, will terminate the loop and exit. If used inside nested loops, it will break out from the current loop.
# A continue statement will stop the current execution when used inside a loop, and the control will go back to the start of the loop.
# The main difference between break and continue statement is that when break keyword is encountered, it will exit the loop.
#
# In case of continue keyword, the current iteration that is running will be stopped, and it will proceed with the next iteration.