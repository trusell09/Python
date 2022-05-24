"""
is_fan = True

if is_fan:
    print("You are a Cubs fan!")
else:
    print("You are not a Cubs fan. Bummer!")
"""

"""
is_fan = False

if is_fan:
    print("You are a Cubs fan!")
else:
    print("You are not a Cubs fan. Bummer!")
"""

"""
is_fan = True
is_serious = False

if is_fan and is_serious:
    print("You are a die hard Cubs fan!")
elif is_fan and not(is_serious):
    print("You kind of like the Cubs")
elif not(is_fan) and is_serious:
    print("Not really a cubs fan but they are cool")
else:
    print("You are not a Cubs fan. Bummer!")
"""

"""
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(900,500,12000000000))
"""

"""
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))
if op == "+":
        print(num1 + num2)
elif op == "-":
        print(num1-num2)
elif op == ("/"):
        print(num1 / num2)
elif op == ("*"):
        print(num1 * num2)
else:
        print("Operator Invalid")
"""

""""
myFavorites ={
    "cubs": "Chicago Cubs",
    "real": "Real Madrid",
    "Avs": "Colorado Avalanche",
    "LBJ": "Lebron James",
    "DP": "Deadpool",
}
print(myFavorites.get("DP"))
print(myFavorites["real"])
"""

"""
i = 10 
while i <= 100:
    print(i)
    i += 1

print ("Done")
"""

"""
for index in range (3, 10):
    print(index)
"""

for index in range (6):
    if index == 0:
        print("Cubs are the best in the NL Central")
    else:
        print ("Go Cubs Go")
