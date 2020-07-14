import re

mail_id="This is my Mail ID arundruk@gmail.com"

match=re.search(r'(\w+)@(\w+)\.(\w+)',mail_id,re.IGNORECASE)
print(match.group(2))
print(match.span()) # Start and End of the index position
print(match.start()) # Start position of the matched string
print(match.end()) # End position of the matched string