'''
Write Python code that asks a user how many pizza slices they want.
The pizzeria charges Rs 123.00 a slice.
 if user order even number of slices, price per slice is Rs 120.00.
  Print the total price depending on how many slices user orders.
'''
n=int(input("no of pizza silice:"))
if(n%2==0):
    c=n*120
    print("total prize of pizza:",c)
else:
    d=n*123
    print("total prize of pizza:",d)