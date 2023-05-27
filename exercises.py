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

    def addition(a,b):
        return a+b
    def substraction(a,b):
        return a-b
    def multiplication(a,b):
        return a*b
    def division(a,b):
        return a/b

    print("OPERATIONS\n")
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print("Select an operation")
    print("\n1.- Addition\n2.- Substraction \n3.- Multiplication\n4.-Division")

    option=input("Select an option: ")

    if option==1:
        print("The addition of {0} and {1} is: ".format(a,b), addition(a,b))
    else:
        if option == 2:
            print("The substraction of {0} and {1} is: ".format(a,b), substraction(a,b))
        else:
            if option ==3:
                print("The multiplication of {0} and {1} is: ".format(a,b), multiplication(a,b))
            else:
                if option==4:
                    print("The multiplication of {0} and {1} is: ".format(a,b), division(a,b))
                else:
                    print("ERROR")

print("Python practice")
print("\n1.- List\n2.- Tuple\n3.- Dictionary\n4.- Operation\n")
optionMenu=input("Select an option: ")

if optionMenu==1:
    functionList()
else:
    if optionMenu == 2:
        functionTuple()
    else:
        if optionMenu ==3:
            functionDictionary()
        else:
            if optionMenu==4:
                functionMath()
            else:
                print("ERROR")