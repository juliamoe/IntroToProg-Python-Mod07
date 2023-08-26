# Title: Assignment 07
# Dev:JMoekkoenen
# Date: 8/25/2023
# Exploring error handling on a simple calculator
#-------------------------------------------------------------#
import pickle

class Processor:
    @staticmethod
    def WriteToFile(value):
        pass
        print()
        des2=input("Would you like to write the data into a file? [y/n]")
        if des2=='y':
            objFile =open("Calculations.dat","ab")
            pickle.dump(value,objFile)
            objFile.close()
            print("Value is saved into the file")
        if des2=='n':
            print()
        readFile = input("Would you like to read the data in file? [y/n]")
        if readFile=='y':
            objFile=open("Calculations.dat","rb")
            objFileData=pickle.load(objFile)
            objFileData += pickle.load(objFile)

            objFile.close()
            print(objFileData,type(objFileData)) #printing the


while(True):
    des1=str(input("Would you like to \n a) Add the values together? \n b) Substract the first value from the second value?"))
    try:
        val1=int(input("Please enter the first value: "))
    except Exception as e:
        print("The provide an integer.")
        break
    try:
        val2=int(input("Please enter the second value: "))
    except Exception as e:
        print("The provide an integer.")
        break

    if des1 == "a":
        add=val1+val2
        print("The addition value is: ",add)
        Processor.WriteToFile(add)
        break
    elif des1 == "b":
        subs = val2-val1
        print("The substraction value is:",subs)
        Processor.WriteToFile(subs)
        break
    else:
        print("Please provide a or b.")
        continue