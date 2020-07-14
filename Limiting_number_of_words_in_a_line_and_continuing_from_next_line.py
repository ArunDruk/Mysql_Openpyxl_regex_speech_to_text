
s="thank you for choosing the Olympus dictation management system the Olympus dictation management system gives you the power to manage your dictations transcriptions and document seamlessly and to improve the productivity of your daily work for example you can automatically sent to the equation files or transcribed documents your assistant officer by email"

L1=s.split()

word_limit=25

with open("word_limit_in_line.txt",'w') as fw:
    for i in range(0,len(L1),word_limit):
        print(i)
        s1=" ".join(L1[i:i+word_limit])
        fw.write(s1+'\n')
