import string
import random
import re
####################################### string module to print a-z, A-Z, 0-9 #############################################################
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
####################################################################################################
txt="""
    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Ha HaHa
    0123456789
    352-980-879    
    123.436.908
    675*576*894
    800-980-879 
    900-980-879
    cat
    mat
    pat
    bat
    1at
    +at
"""
sentence="Start a sentence and bring it to the End"
#print(r"\tTab") # r-> denotes raw string and no special operations will be done.
#pattern=re.compile(r'abc') # The pattern we are searching it is better to take it into a variable.
#pattern=re.compile(r'\d') # matches the digit [0-9]
#pattern=re.compile(r'\D') # matches not digit [0-9]
#pattern=re.compile(r'\w') # matches the word character [a-z],[A-Z],[0-9]
# pattern=re.compile(r'\W') # Not a word character
#pattern=re.compile(r'\s') # Matches the whitespaces space, tab, newline
#pattern=re.compile(r'\S') # Not whitespace Space, tab and newline
####################################################################################################
# Anchors which helps to search the pattern before or after : \b -> word boundary \B -> Not a word boundary
# ^ -> Beginning (start) of the string
# $ -> End of the string
# [] ->Matches character in brackets, [^] -> Matches character not in bracket
# pattern=re.compile(r'\bHa') # Matches the word boundary the first 'Ha' and the first 'Ha' in 'HaHa'
# pattern=re.compile(r'\BHa') # Matches the second 'Ha' in 'HaHa', Not a word boundary

# pattern=re.compile(r'^Start') # This matches as at the beginning of the string there is a 'Start'
# pattern=re.compile(r'^and') #This doesn't give any match as 'and' is not at the begining of the string.

pattern=re.compile(r'End$') ## This matches as at the End of the string there is a 'End'
matches=pattern.finditer(sentence)
#pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d')
# pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d') # This matches any character for the fourth position
# pattern=re.compile(r'\d\d\d[.-]\d\d\d[-.]\d\d\d') # This is a Character Set and it matches only the characters .- inside [.-]
# pattern=re.compile(r'[89]00[.-]\d\d\d[-.]\d\d\d') # Need to match the phone number starting with either 8 or 9.
#pattern=re.compile(r'[^a-zA-Z]') # It matches everything except the first character starting with a-z and A-Z
# pattern=re.compile(r'[^[b]at') # Matches three character word, ending with 'at' except the first character not starting with 'b'
########################################## Using finditer method ##########################################
# matches=pattern.finditer(txt)
print(matches)
for match in matches:
    print(match)
####################################################################################
##################################### Using findall Method #####################################
# List_of_findings=pattern.findall(txt)
# print(List_of_findings,type(List_of_findings))
##########################################################################


#print(txt[5:8]) # This prints exactly what the match "abc" we searched
# Finished the video till 15 min, Corey RE