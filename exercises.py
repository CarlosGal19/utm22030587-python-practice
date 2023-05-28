def functionList():                                                                         # Funcion lista (1)

    print("LIST\n")
    listOne=[7,54,102,903,1]                                                                # Lista declarada

    position=int( input("In which position do you want to save the entered number?: ") )    # Variable para conocer la posición donde será almacenado un nuevo número

    number=( input("Enter the number to be added to the list: ") )                          # Variable para conocer el valor que se almacenerá en la lista

    listOne.insert(position,number)                                                         # Inserta variable en la lista

    for i in listOne:                                                                       # Imprime la nueva lista
        print (i)

def functionTuple():                                                                        # Función tupla (2)

    print("TUPLE\n")
    tupleOne=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")       # Tupla declarada

    i=int(0)
    while i<7:                                                                              # While que imprime la tupla
        print(tupleOne[i])
        i=i+1

def functionDictionary():                                                                   # Función diccionario (3)

    print("DICTIONARY\n")
    dictionary={"Name":"Messi","Number":10,"Team":"PSG"}                                    # Diccionario declarado
    print("The dictionary is: ",dictionary)
    dictionary["Team"]=input("What would you like Lionel Messi's new team to be?: ")        # El valor ingresado se cambiará en la llave 'Team' del diccionario
    print("Dictionary update: ",dictionary)                                                 # Diccionario declarado

def functionMath():                                                                         # Funcion math (4)

    def operation(operand, firstNumber, secondNumber):                                      # Función que hará la operación (recibe los parámetros)

        if operand == '+':                                                                  # If anidados que evaluan el signo y números ingresados, para después hacer la operación
            result = firstNumber + secondNumber
        else :
            if operand == '-':
                result = firstNumber - secondNumber
            else:
                if operand == '*':
                    result = firstNumber * secondNumber
                else:
                    if operand == '/':
                        if secondNumber == 0:                                               # Si es una división, y el segundo número es 0 no se ejecutará, retornando un valor nulo
                            print("Error: Division by zero is not allowed.")
                            return None 
                        result = firstNumber / secondNumber
                    else:
                        print("Error: Invalid operand.")                                    # Si el operando no es válido, lo dirá, y retornará un valor nulo
                        return None

        return result

    print("OPERATIONS\n")

    operand = input("Enter an operand (+, -, /, *): ")                                      # Variable operando (caracter que hará la operación)
    firstNumber = int(input("Enter the first number: "))                                    # Primer número de la operación
    secondNumber = int(input("Enter the second number: "))                                  # Segundo número de la operación

    result = operation(operand, firstNumber, secondNumber)                                  # Función que hará la operación con los parámetros enviados
    if result is not None:                                                                  # Si hay un valor (no nulo) se imprimirá, de lo contrario no pasará nada
        print("Result:", result)

print("Python practice")                                            # Menu principal
print("\n1.- List\n2.- Tuple\n3.- Dictionary\n4.- Operation\n")
optionMenu=int(input("Select an option: "))

if optionMenu==1:                                                   # If anidados para llamar a la función que sea elegida
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