# pip install requests-html

from requests_html import HTML

with open("simple.html",'r+') as html_file:
    source=html_file.read()
    html=HTML(html=source)

print(html.text)
