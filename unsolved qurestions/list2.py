#Write a Python program to change the position of every n-th value with the (n+1)th in a listSet1.
from itertools import zip_longest, chain, tee
def a(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(a(n))
