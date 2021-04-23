'''
Write a python program to check
if the input number is-real number
-float numner-
string-complex
number-Zero (0)
'''
num=input("enter the number :")

    if(isinstance(num,int)=="True"):
        print("number is integer")
    elif(isinstance(num,float)=="True"):
        print("number is float")
    else:
        print("complex num")