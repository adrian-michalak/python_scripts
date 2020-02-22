import re
file = open("file.txt","r")
text = file.read()

findNumber = re.findall('\(?\+?\d+(?:[- \)]+\d+)+',text)
print('Lista numerow w tekscie: ')
for phone in findNumber:
    print(phone)
