# -*- coding: utf-8 -*-
import os
import re

directory = input("Podaj sciezke do katalogu ")
path = os.path.dirname(directory)
enteredWord = input("Podaj slowo do wyszukania ")

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))
print("Lista plikow do przeszukania ")
for f in files:
    print(f)
print("Pokaz w ktorych plikach znajde:  ", enteredWord)
for f in files:
    openFile = open(f, 'r')
    content = openFile.read()
    findWord = re.findall(enteredWord, content)
    if len(findWord) != 0:
        print(f)





