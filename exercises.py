def functionList():

    listOne=[7,54,102,903,1]

    position=int( input("In which position do you want to save the entered number?: ") )

    number=( input("Enter the number to be added to the list: ") )

    listOne.insert(position,number)

    for i in listOne:
        print (i)

def functionTuple():

    tupleOne=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    
    i=int(0)
    while i<7:
        print(tupleOne[i])
        i=i+1

functionTuple()
functionList()