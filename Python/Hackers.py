from operator import itemgetter
name,marks=[],[]
for x in range(0,int(input("what is number :"))):
   name.append(input())
   marks.append(float(input()))
al=list(zip(name,marks))
l=[list(i) for i in al]
p=sorted(l,key=itemgetter(0))
s=sorted(l,key=itemgetter(1))
re=p[1][0]
se=s[1][0]
if re ==se:
   print(re)
else:
   print(re)
   print(se)

