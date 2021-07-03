# a="Arun Kumar"
# print(len(a))
# print("a[5:10]=",a[5:10])
# print("a[:5] or a[0:5]=",a[:5])
# print("a[:-3]=",a[:-3])
# print("a[::-1]=",a[::-1]) # -1 will start from the reverse way
# print("a[::2]=",a[::2]) # This will take index alternate positions

s="thank you for choosing the Olympus dictation management system the Olympus dictation management system gives you the power to manage your dictations transcriptions and document seamlessly and to improve the productivity of your daily work for example you can automatically sent to the equation files or transcribed documents your assistant officer by email"
# s="""thank you for choosing the Olympus dictation management system the Olympus dictation management system gives you
#    the power to manage your dictations transcriptions and document seamlessly and to improve the productivity of your daily work for example you can automatically
#   sent to the equation files or transcribed documents your assistant officer by email"""
i=1
with open("text_file_with_limit.txt",'w') as fw:
    for char in s:
        i+=1
        fw.write(char)
        if (i%100==0):
            fw.seek(i)
            fw.write('\n')


# word_count=s.split(' ')
# line_count=s.split('\n`')
#
# print(len(word_count))
# print(len(line_count))
