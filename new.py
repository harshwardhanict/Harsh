
'''

print (myDict)'''
import datetime

'''myDict = [[x*x for x in range(10) if x==6] for x in range(3)]

print(myDict)

string = 'GeeksGeeks'

# Toggle case of each character
List = list(map(lambda i: chr(ord(i)^32), string))

# Display list
print(str(List))

arr = ['cat', 'dog', 'tac', 'god', 'act']
x ={}



dict = {}
for strVal in arr:
 key = ''.join(sorted(strVal))
 if key in dict.keys():
            dict[key].append(strVal)
 else:
            dict[key] = []
            dict[key].append(strVal)

for key, value in dict.items():
        print(' '.join(value))
'''
'''
f = ['cat', 'car', 'fear', 'center']
l=[[x for x in i]for i in map(list,f)]
k=[]
for j in l:
    k.append(len(j))
print(k)'''
'''
f = ['ca',('cat', 'cag', 'shatter', 'donut', 'at', 'cado', '')]

h =[i for i in range(len(f[1])) if f[0] in f[1][i]]
print(h)
'''
'''
l = [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
l1 = []
for i in l:
    print(i[0],i[1])
    for j in i[1]:
        if(i[0] > j):
            l1.append(j)
            print(i[1])
'''
'''
from datetime import datetime,timedelta

x = datetime.now()
y = x.date() + timedelta(days=2)
z = x.date() + timedelta(days=1)
a=x-(z-y)
print(a)

'''
