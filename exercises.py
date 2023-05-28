def functionList():

    print("LIST\n")
    listOne=[7,54,102,903,1]

    position=int( input("In which position do you want to save the entered number?: ") )

    number=( input("Enter the number to be added to the list: ") )

    listOne.insert(position,number)

    for i in listOne:
        print (i)

def functionTuple():

    print("TUPLE\n")
    tupleOne=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

    i=int(0)
    while i<7:
        print(tupleOne[i])
        i=i+1

def functionDictionary():

    print("DICTIONARY\n")
    dictionary={"Name":"Messi","Number":10,"Team":"PSG"}
    print("The dictionary is: ",dictionary)
    dictionary["Team"]=input("What would you like Lionel Messi's new team to be?: ")
    print("Dictionary update: ",dictionary)

def functionMath():

    def operation(operand, firstNumber, secondNumber):
        if operand == '+':
            result = firstNumber + secondNumber
        else :
            if operand == '-':
                result = firstNumber - secondNumber
            else:
                if operand == '*':
                    result = firstNumber * secondNumber
                else:
                    if operand == '/':
                        if secondNumber == 0:
                            print("Error: Division by zero is not allowed.")
                            return None
                        result = firstNumber / secondNumber
                    else:
                        print("Error: Invalid operand.")
                        return None

        return result

    print("OPERATIONS\n")
    operand = input("Enter an operand (+, -, /, *): ")
    firstNumber = int(input("Enter the first number: "))
    secondNumber = int(input("Enter the second number: "))

    result = operation(operand, firstNumber, secondNumber)
    if result is not None:
        print("Result:", result)

print("Python practice")
print("\n1.- List\n2.- Tuple\n3.- Dictionary\n4.- Operation\n")
optionMenu=int(input("Select an option: "))

if optionMenu==1:
    functionList()
else:
    if optionMenu==2:
        functionTuple()
    else:
        if optionMenu==3:
            functionDictionary()
        else:
            if optionMenu==4:
                functionMath()
            else:
                print("ERROR")