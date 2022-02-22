'''x ="google.com'"
count={}
for i in x:
   if i not in count:count[i]=1
   else:count[i]+=1
print(count)
a='restart'
b=a[0]
a = a.replace(b,"$")
print(b+a[1:])'''
'''
x ='abc', 'xyz'
x=list(x)
x[0],x[1]=x[1],x[0]
print(" ".join(x))'''
'''
a = input("what is your string : ")
b=["ly"]
c=["ing"]
x=a.endswith("ing")
if x == True:
    a = list(a)
    a[-3:],b[0:]=b[0:],a[-3:]
    print("".join(a))
elif x == False:
    a=list(a)
    print("".join(a+c))'''
'''
x ="what is your string exercises"
lit = x.split()
z=max(lit,key=len)
print(z,len(z))'''
'''
a ='The lyrics is not that poor!'
a=a.replace("poor!","good!")
a=a.replace("not","")
print(a)
b = a.split()
if "not" in b:
    b.remove("not")
    print(" ".join(b))
'''
'''
a ='The lyrics is not that poor!'
n = str(input("What you want to remove :"))
b = a.find(n)
print(a.replace(a[b:b+len(n)],""))

str = 'The lyrics is not that poor!'
lis=str.split()
l=enumerate(lis)
print()
'''
'''
x ="red, white, black, red, green, black"
x = x.split()
x=set(sorted(x))
print("".join(x))'''
