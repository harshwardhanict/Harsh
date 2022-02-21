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

# dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(*dict)
# for x in zip(*([i]+j for i,j in sorted(dict.items()))):
#      print(*x)

# def f1(*args,**kwarg):
#     print(args)
#     print(kwarg)
#
# f1(5,6,7,x=20,y=50,a=10,b=23)
#
# x={'x': 20, 'y': 50, 'a': 10, 'b': 23}
# y={'o': 20, 'g': 50, 'f': 10, 'e': 23}
# print(sorted(x.items(),key=lambda x:x[0]))
# y={'xxx', 'y', 'a', 'b'}
# print()
# x=[90,35,2,120,100]
# print(list(filter(lambda y:y*2,x)))
# p=sorted(x,key=lambda x:x*2)

#
# print(p)
# def f1():
#     x =100
#     return x
#
# x=f1()-1
# print(x)
#
# l=[1,2,3,4]
# l1=["a","b","c","d"]
# l3={i:j for i,j in zip(l1,l)}
# print(l3)
l=[{'x': 20, 'y': 50, 'a': 10, 'b': 23},{'o': 20, 'g': 90, 'f': 10, 'e': 23},{'k': 80, 'h': 60}]
# x=dict(l[0],**l[1])
# x = dict(map(map(lambda x:x,l)),l))

# dict={x for x in l}
# print(dict)
# m=map((lambda x,y:{x:y}),l)
# print(m)
# for x in range(len(l)):
#     m=map(lambda y:y,l[x])
#     print(list(m))
# print(list(m))
# y = filter(int,l)
print()
print()
# x= dict(map(lambda x:dict(x),l))
# a1 = [{'d':1,'c':2},{'c':3,'d':4},{1:'a',2:'b'}]
# l=[1,2,3,4,5]
# print(dict(map(lambda x:set(x),a1)))
#
# x={"a":
#        {"b":{
#            "e":False,
#            "f":
#                 {"l":{"q":False,"r":False},
#                 "m":{"s":False,"t":False}},
#            "g":False},
#         "c":
#             {"h":False,
#              "i":{"n":False,"o":False}
#              },
#         "d":
#             {"j":False,
#              "k":
#                  {"p":
#                        {"u":False,
#                         "v":{"x":False,"y":False},
#                         "w":"z"}
#                   }
#              }
#        }
# }
#
#
# def f(x,y):
#   l=[]
#   for i,j in x.items():
#     if i!=y and type(j)==dict:
#       f(j,y)
#     elif i==y:
#         print(j.keys())
#
# y=input("Which Branch you want : ")
# print(f(x,y))


# x=[{"name":"harry","age":89,"enroll":1180},{"name":"harsh","age":93,"enroll":1190},{"name":"hax","age":92,"enroll":1100}]
# print(list(map(lambda x:x["name"],x)))


# x={"name":"harry","age":89,"enroll":1180}
# print(set(x))
#
# list1 = (1, 2, 3, 4, 5, 6 )
# list2=(21,32,17)
# print(list1+list2)
# print(list1[1])
# # list1.pop(3)
# print(list1)

x =2
y=2.233
str(x+y))
# x = input("www: ")
# l=x.split(" ")
#
# print(" ".join(l))