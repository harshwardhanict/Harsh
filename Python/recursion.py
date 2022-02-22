'''def recusr(x):
    if x==1:
        return x
    else:
        return (x*recusr(x-1))

print(recusr())
x=[1, 2, (3, 4), [5, 6]]
def sum(x):
 total=0

 for a in x:
     if type(a) == type([]):
        total=total + sum(a)
     elif type(a)==type(()):
         total = total + sum(a)
     else:
        total=total + a
 return total
print(sum(x))'''
'''
def g(x):
   if x == 1:
       return 1
   else:
       return 1/x + g(x-1)

print(g(10))'''
'''
def g(x):
   if x <0:
       return 0
   else:
       return 1/pow(2,x) + g(x-1)


def po(n,x):
    if x == 1:
        return n
    else:
        return pow(n,x)
'''
'''
x,y=14,15
if x>y:
    l=[i for i in range(2,x) if i%2==0]
elif y>x:
    l = [i for i in range(2, y) if i%2==0]
print(l)
l1 = [i for i in l if x%i==0]
print(l1)
'''
'''
def sum(n):
    if n == 0:
        return n
    else:
      return n + sum(n-1)

print(sum(4))
'''
'''
l=list(range(1,int(input('number :'))))
print(type(l))

def sum_list(a):
    if len(a) < 1:
        return 0
    else:
     return a[0] + sum_list(a[1:])

print(sum_list(l))'''
