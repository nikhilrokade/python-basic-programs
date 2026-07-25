import math

def user_input(op_type):
    if op_type == 1:
        number_1 = int(input("Enter the eg: 10 and not 10.0 value: "))
        return number_1  
    elif op_type == 2:
        number_1 = int(input("Enter the eg: 10 and not 10.0 value: "))
        number_2 = int(input("Enter the eg: 10 and not 10.0 value: "))
        return (number_1, number_2) 

def addItion():
    number_1, number_2 = user_input(2)
    return number_1 + number_2

def subStraction():
    number_1, number_2 = user_input(2)
    return (number_1 - number_2)

def multiPlication():
    number_1, number_2 = user_input(2)
    return (number_1 * number_2)

def divIsion():
    number_1, number_2 = user_input(2)
    return (number_1 / number_2)

def sqUare():
    number_1 = user_input(1)
    return (number_1 ** 2)

def squareRoot():
    number_1 = user_input(1)
    res = math.sqrt(number_1)
    return res

def cuBe():
    number_1= user_input(1)
    return (number_1 * number_1 * number_1)

def cubeRoot():
    number_1 = user_input(1)
    res = math.pow(number_1, (1/3))
    return res

def multipleCal():
    number_1 = int(input("Enter the first value: "))
    number_2 = int(input("enter the second value: "))

    print("Addition: ", number_1 + number_2)
    print("Substraction: ", number_1 - number_2)
    print("Multiplication: ", number_1 * number_2)
    print("Division: ", number_1 / number_2)
    print("Square: ", number_1 * number_1)
    print("Square Root: ", math.sqrt(number_1))
    print("Cube: ", number_1 * number_1 * number_1)
    print("Cube Root: ", math.pow(number_1, (1/3)))


def main():    
    while True:
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Square")
        print("6) Square Root")
        print("7) Cube")
        print("8) Cube Root")
        print("9) Multiple Caluclation")
        print("10) Exit")
        exit

        cal = input("Select number: ")
        if cal == "1":
            result = addItion()
            print("Result:", result)
            break
        elif cal == "2":
            result = subStraction()
            print("Result:", result)
            break 
        elif cal == "3":
            result = multiPlication()
            print("Result:", result)
            break
        elif cal == "4":
            result = divIsion()
            print("Result:", result)
            break
        elif cal == "5":
            result = sqUare()
            print("Result:", result)
            break
        elif cal == "6":
            result = squareRoot()
            print("Result:", result)
            break
        elif cal == "7":
            result = cuBe()
            print("Result:", result)
            break
        elif cal == "8":
            result = cubeRoot()
            print("Result:", result)
            break  
        elif cal == "9":
            multipleCal()
            break 
        elif cal == "10":
            break
        else:
            print("End")   
            break   

if __name__ == "__main__":
    main()