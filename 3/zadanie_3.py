

string = "Python is awesome, isn't it ?"
print(string)
CounterList = {}
for i in string:
    s = str(i)
    if s == " ":
        continue
    count = string.count(s)

    if count > 1:
        CounterList[s] = count


#print(CounterList)
print(sorted(CounterList.items(), reverse=True, key=lambda kv: (kv[1], kv[0])))