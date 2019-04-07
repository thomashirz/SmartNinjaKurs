print("Welcome to the world's most basic Calculator")


nummer1 = input("Enter Number One Here: ")

operator = input("What do you want to do? (+, -, *, /:)")

nummer2 = input("And Here Number Two: ")

if operator == '+':
    print(float(nummer1) + float(nummer2))

elif operator == '-':
    print(float(nummer1) - float(nummer2))

elif operator == '*':
    print(float(nummer1) * float(nummer2))

elif operator == '/':
    print(float(nummer1) / float(nummer2))


else:
    print("Error, wrong input.")


