'''arr = ['cat', 'dog', 'tac', 'god', 'act']
x =[]
l=[[x for x in i]for i in map(list,arr)]
for j in range(0,3):
    for i in l[0]:
        break
    for k in l[1]:
        break
    if l[0]==l[1]:
            x.append(l[0] and l[1])

print(x)

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

y = [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
l = [i for i in map(list,y[0])]
x=[]
for i, row in enumerate(l):
    for j, n in enumerate(row):
         if n == y[1]:
             x.append([i,j])
print(x)