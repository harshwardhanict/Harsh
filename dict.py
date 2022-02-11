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
dict=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

d= [[j for i,j in x.items()] for x in dict]
print(d)
