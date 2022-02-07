'''l = [x for x in range(2000,3200+1) if x%7==0 and x%5!=0]
x = str(l)
print(" ".join(x))'''
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
    print(x.upper())'''
'''
a="Tom",19,80
b ="John",20,90
c="Jony",17,91
d="Jony",17,93
e="Json",21,85

l = list(zip(a,b,c,d,e))
l1=[[i for i in list(sorted(l[j]))] for j in range(0,int(len(l)))]
print(list(zip(l1[0],l[1],l[2])))'''
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
m=28
n=9
print(f'the {m} is  {n}')
#print(id(x))


