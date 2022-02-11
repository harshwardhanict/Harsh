'''l=(2, (4, 6), 8, 10,10, 14,(), 14,(2,12),(2,12),(14),(34,7,5))
count={}
for i in l:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
l=[i for i,j in count.items() if j>1]
print(l)'''
'''
l=(2, (4, 6), 8, 10,10, 14,(), 14,(2,12),(2,12),(14),(34,7,5))
l1=[]
for j in l:
    if type(j)==type(()):
        l1.append(list(j))
    else:
        l1.append(j)
print(l1)
'''
'''
l=(2, (4, 6), 8, 10,10, 14,(), 14,(2,12),(2,12),(14),(34,7,5))
print()
t=(100,200,300)
p=('{}'.format(t))
print(type())
print(type(t))
'''
# x=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# l=[[j for j in i] for i in x]
# sum =[]
# su=0
# for i in l:
#     for j in range(0,4):
#
#     print(su)
#
#         #sum.append(su)
