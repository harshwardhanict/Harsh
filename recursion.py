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

l=(2, (4, 6), 8, 10,10, 14,(), 14,(2,12),(2,12),(14),(34,7,5))
count={}
for i in l:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
l=[i for i,j in count.items() if j>1]
print(l)