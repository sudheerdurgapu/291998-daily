def merge(squares1,squares2):
    c={**squares1,**squares2}
    return c
squares1={'1':1,'2':4,'3':9}
squares2={'4':16,'5':25,'6':36}
c=merge(squares1,squares2)
print(c)