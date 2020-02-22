

GenerateNumbers=[]
DigitsList = []
Temp=[]
SumNum=[]
PrimeSum=[]
sum = 0
print("Podaj zakres generowania liczb ")
x = input ("Podaj x: ")
xx = int(x)
y = input("Podaj y: ")
yy = int(y)


def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
            break
    else:
        return True


print("GENEROWANE LICZBY: ")
for i in range(xx, yy+1):
    GenerateNumbers.append(i)
print(GenerateNumbers)
print(len(GenerateNumbers))


print("PODZIAL LICZB NA CYFRY: ")
for i in GenerateNumbers:
    var = list(str(i))
    DigitsList.append(var)
print(DigitsList)

for i in DigitsList:
    Temp = list(i)
    sum = 0
    for j in Temp:
        sum += int(j)
    SumNum.append(sum)

print("sumy:", SumNum)
print("Rozmiar: ", len(SumNum))
Temp = []
print(GenerateNumbers, " ==== ", SumNum)










        

        



        


        
        
        
        

