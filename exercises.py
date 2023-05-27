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

    print("OPERATIONS\n")

print("Python practice")
print("1.- List \n 2.- Tuple \n 3.- Dictionary \n 4.- Operation")
option=int(input("Select an option: "))

if option==1:
    functionList()
else:
    if option == 2:
        functionTuple()
    else:
        if option ==3:
            functionDictionary()
        else:
            if option==4:
                functionMath()
            else:
                print("ERROR")