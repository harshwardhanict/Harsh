'''dict={8: 33,3: 21,22: 10, 1: 20, 2: 30}
print(sorted(dict.items(),key=lambda x:x[2]))'''
'''dic1={1:1, 2:20}
dic2={3:3, 4:40}
dic3={5:50,6:60}
dict12={}
dict12.update(dic1)
dict12.update(dic2)
dict12.update(dic3)
'''
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for i,j in zip(d1,d2):
    if i==j:
        d[i]=d1[i]+d2[j]
    else:
        d[i]=d1[i]
        d[j]=d2[j]
'''
'''
d1 = {'a': 100, 'b': 54, 'c':247}
d=[x for x in d1.values()]
sum=1
for i in d:
    sum*=i
print(sum)

from operator import itemgetter
d1 = [{'name': 'avish', 'age': 14, 'roll':47},
        {'name': 'dhruvil', 'age': 40, 'roll':24}]


print(sorted(d1,key=itemgetter('age')))'''
'''dict=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
l=set()
for x in dict:
    for i,j in x.items():
        l.add(j)
print(list(l))
'''
# d1 = {'a': 100, 'b': 54, 'c':247,"d":247,"e":54}
# data = {'1':['a','b'], '2':['c','d']}
# l=[x for x in data.values()]
# s=set()
# for x in range(2):
#     for y in range(0,2):
#
#         #print(l[] + l[x])
# print(s)
# d1 = {'a': 100, 'b': 54, 'c':247,"d":247,"e":54}
# dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for x in zip(*([i]+j for i,j in sorted(dict.items()))):
#     print(*x)
# l=[]
# l1=[]
# for x in range(0,int(input("what is number :"))):
#     l.append(input())
#     l1.append(int(input()))
# l=[('harry', 67), ('berry', 45), ('tina', 34), ('akriti', 32), ('jayu', 33)]
#
# l=[list(i) for i in l]
# print(l)
# dict=dict(zip(l,l1))
#print(dict)
# l={'harry': 67, 'berry': 45, 'tina': 34, 'akriti': 32, 'jayu': 33}
# p=sorted(l,key=lambda x,y:x[1])

# l=[lambda x:x*10 for x in range(0,10)]
# for x in l:
#     print(l)

# List = [[2,3,4],[1, 62, 9, 12],[1, 6, 9, 12]]
# x=list(filter(str,List[1]))
# y=list(map(str,List[1]))
# print(type(y[0]))
# print(type(y))
# print(type(x))
#

n = int(input())
x=input()
x.split()
l=[]
for i in x:
    l.append(i)

