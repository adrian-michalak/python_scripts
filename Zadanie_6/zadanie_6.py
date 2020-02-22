from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2016, 7, 11)
delta = l_date - f_date
print(f_date, "-", l_date, " = ", delta.days, " dni")
