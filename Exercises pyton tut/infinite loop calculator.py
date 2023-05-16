def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b


def div(a, b):
    return a / b


choose = 0

while choose != 1:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    cho = int(input("choose 1 for add, 2 for subtraction, 3 for multiplication, 4  for division: "))
    if cho ==1:
        print("the sum of these digit is ", add(a,b))
        continue
    elif cho ==2:
        print("the subtraction of these digit is ", sub(a,b))
        continue
    elif choose==3:
        print("the multiply of these digit is ", multi(a,b))
        continue
    elif cho==4:
        print("the division of these digit is ", div(a,b))
        continue
    else:
        print("Wrong input")
        break

