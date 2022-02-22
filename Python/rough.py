'''def func(x=20,y=50,z=[]):
    return 5,10,20

a,b,c=func(x=205,y=2,z=30)
print(type(a),type(b),type(c))'''
x = "x"
#
# def abc(dh=0,end=0):
#     print(dh)
#     print(end)
#
# abc(1,12)
# x =111
# x%=12
# print(x)]
from operator import itemgetter
l=[('harry', 31), ('berry', 45), ('tina', 34), ('akriti', 29), ('jayu', 33)]

l=[list(i) for i in l]
p=sorted(l,key=itemgetter(0))
print(p[1][0])
s=sorted(l,key=itemgetter(1))
print(s[1][0])