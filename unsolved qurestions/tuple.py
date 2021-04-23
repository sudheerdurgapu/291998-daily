#Write a Python program to find the repeated items of a tuple
tuple=(5,2,4,7,9,4,5,5,1)
for i in tuple:
    if(tuple.count(i)>1):
        print(i)