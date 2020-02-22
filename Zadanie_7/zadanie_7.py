import re

finput = open("main.cpp", "r")
foutput = open("main_without_comments.cpp", "w")
text = finput.read()
pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE)
result = re.sub(pattern, " ", text)
foutput.write(result)
foutput.close()
