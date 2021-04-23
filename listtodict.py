#Write a Python program to convert a list into a nested dictionary of keys
list=[1,2,3,4,5,6]
dict=a={}
for i in list:
    a[i]={}
    a=a[i]
print(dict)