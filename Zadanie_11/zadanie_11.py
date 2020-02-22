
def windows(filename,openfile):
    for line in file:
        fields = line.split("/")
        print(" route add " + fields[0] + " netmask " + fields[1] + " " + fields[2])


def linux(filename, openfile):
    id = 0
    for line in file:
        fields = line.split("/")
        print(" ifconfig eth" + str(id) + " " + fields[0] + " netmask " + fields[1])
        print(" route add default gw " + fields[2])
        id += 1


def cisco(filename, openfile):
    for line in file:
        fields = line.split("/")
        print(" ip address " + fields[0] + " " + fields[1])
        print(" ip default-gateway " + fields[2])


def choose(choice):
    while choice != 5:
        if choice == 1:
            windows(name, file)
            break

        if choice == 2:
            linux(name, file)
            break

        if choice == 3:
            cisco(name, file)
            break

        if choice == 4:
            print("Koniec")
            break


name = "adresy.txt"
#name = input("Podaj nazwe pliku : ")
file = open(name, "r")
choice__ = input("1. Windows\n2. Linux\n3. Cisco\n")
choice_ = int(choice__)
choose(choice_)



