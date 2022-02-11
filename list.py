'''l = [x for x in range(2000,3200+1) if x%7==0 and x%5!=0]
x = str(l)
print(" ".join(x))'''
import random
import shlex

'''
x = int(input("what is num:"))
l = [i for i in range(1,x+1)]
sum = 1
for i in l:
    sum *=i
print(sum)
'''
'''
x = input('what is many number do you want: ')
dict ={i:i**2 for i in range(0,int(x)+1)}
print(dict)'''
'''x =34,67,55,33,12,98
g = list(x)
h = list(g.split(""))
print(h)'''

'''
str1 = input("what is num:")
l=str1.split(',')
print(list(l))
print(tuple(l))
'''
'''
for i in range(0,int(input("how many lines you want :"))):
    x = input("Enter the line : ")
    print(x.upper())

a="Tom",19,80
b ="John",20,90
c="Jony",17,91
d="Jony",17,93
e="Json",21,85
l=[]
for i in range(5):


print(tuple(l.sort()))'''
'''l1=[[i for i in list(sorted(l[j]))] for j in range(0,len(l))]
print(l1)
print(list(zip(l1,l[2])))
'''
'''
H="Hello worldHG!"
count=0
count1=0
for i in H:
    if i.islower():
        count += 1
    elif i.isupper():
        count1+=1
print("Lower case : ",count)
print("UPPER case : ",count1)

from string import capwords
x =30
X=6
y="hello world"

s="_".join(y)
print(s)
print(capwords(s.replace("_","")))'''
'''
l=1,2,3,4,5,6,7,8,9
x =[j for j in l]
print(x)
l1={i:i**2 for i in x if i%2!=0}
print(l1)


import random
x = random.sample([x for x in range(100,201) if x%2==0],5)
print(x)
import random
x = random.sample([x for x in range(1,1001) if x%7==0 and x%5==0],5)
print(x)'''
'''
list =[3,6,7,8]
random.shuffle(list)
print(list)

l=[5,6,77,45,22,12,24]
for i in l :
    if i%2==0:
        l.remove(i)
print(l)'''
'''
l=[12,24,35,70,88,120,155]
f=[x for x in l if x%7==0 and x%5==0]
l=[x for x in l if x not in f]
print(l)

l,f=[12,24,35,70,88,120,155],[0,4,5]

s=[l[x] for x in range(len(l)) if x not in f]
print(s)
l=[12,24,35,70,88,120,155]
s=[x for x in l if x not in [24]]
print(s)'''
'''
x,y=[1,3,6,78,35,55] , [12,24,35,24,88,120,155]
a,b=set(x),set(y)

l=a.intersection(b)
print(list(l))
l=[12,24,35,24,88,120,155,88,120,155]
count=[]
for x in l:
    if x not in count:
        count.append(x)
print(sorted(count,reverse=True))
'''
'''
x=1,2,3,4,5,6,7,8,9
x=[i for i in list(x) if i%2!=0]
print(x)
n=5#int(input("what "))
N=5
for x in range(0,n):
    for y in range(0,N):
        print(end=" ")
    N =N-1
    for y in range(0,n):
        print("*",end=" ")
    print()
'''
'''
d=[['D',300],['D',300],['W',200],['D',100]]
su =0
for x in d:
    if x[0] =="D":
        su+=x[1]
    else:su-=x[1]
print(su)'''
'''
n ,l=5,['p', 'q']
l1=[]
for i in range(1,n+1):
    for x in l:
        l1.append(x+str(i))
print(l1)'''
'''
l=[3, 4, 6, 28, 69, 71, 65, 93, 120,17,9, 7, 1, 0, 0 ]
x = sorted(set(l))
print(x)
'''