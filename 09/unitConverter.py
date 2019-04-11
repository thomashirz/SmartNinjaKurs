print("Welcome this tiny toll helps you to convert kilometer (km) into miles (mi)")


numberKm = int(input("Enter the km here: "))

numMi = numberKm * 0.621371

while numberKm >=0:
    print(str(numMi) + " miles")
    break

while True:
    quest = input("Do you want to make another conversion? Please answer YES or NO: ")
    if quest == "YES":
        numberKm = int(input("Enter the km here: "))

    while numberKm >= 0:
        print(str(numMi) + " miles")
        break

    if quest == "NO":
        print(Bye)
