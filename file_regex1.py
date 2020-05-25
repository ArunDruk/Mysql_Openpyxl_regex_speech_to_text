
import re

# This way of opening the file is called as Context Manager
filename="CoStar_INV_IS_US_2020.txt"
# with open(filename,"r+") as fo:
############################################################################################################################################
    #L1=fo.readlines() # Readlines reads all the lines of the file and save it in the List in a single line
    # L1=fo.readline() # Readline reads only one line
    # L1=fo.read() # Reads the complete file.
############################################################################################################################################
# Below code is to read the complete file line by line using for loop
############################################################################################################################################
    # for line in fo:
    #     print(line,end="")
############################################################################################################################################
    # L1=fo.read(100) # You can mention the number of characters that you want to read from the file.
############################################################################################################################################
# Since read() operation reads the complete file, if the file size is huge we'll end up in memory issues.
# So in the below code am reading the file for 100 characters and printing it and again reading 100 characters till the end of the file.
# once the end of the file is reached it will return the empty string.
############################################################################################################################################
#     while (len(L1) > 0):
#         print(L1)
#         L1=fo.read(100)
############################################################################################################################################
# with open("copied_file.txt","r+") as fw:
#     fw.write(L1)
############################################################################################################################################
#Some other useful file operations
############################################################################################################################################
#print(fo.name) # This prints the name of the file
############################################################################################################################################

# Some logic just to create the file
############################################################################################################################################
# with open("Create_file.txt",'w') as fw:
#     pass
############################################################################################################################################

######################################################################################################################################################
# To Open the file read all the contents in the file and write the Contents to some new file, just like copy file
# To read the image file open the file in read binary mode 'rb', similarly to write open the file in write binary mode 'wb'
with open(filename,'r') as rf:
    with open("Costar_copy.txt",'w') as wf:
        for line in rf:
            wf.write(line)



######################################################################################################################################################