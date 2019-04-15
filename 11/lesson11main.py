some_number = 3
float_number = 4.56
string_text = "hallo"
boolean = True #variablen namen sollte lesbar

number_list = [2, 4, 1, 7, 8]

print(number_list[3])

#print(number_list[3:4] --> bei einer Range wird letzter Wert nicht ausgegeben

auto_list = ["Audi", "Tesla", "VW"]
print(auto_list[2])
auto_list.append("Honda") #es wird Honda in der Liste angefügt
print(auto_list)


for item in auto_list:
    item = "bla"
    print(item)

print(auto_list)


shopping_list = {"milk": 2,
                 "break": 5,
                 "eggs": 10,
                 "dict": {
                     "c++": 5,
                     "java": 3,
                     "python": 1,
                 },
                 "list": [1, 2, 3, 4, 5]
                 }

print(shopping_list["milk"])

print(shopping_list)