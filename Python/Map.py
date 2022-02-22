# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums3 = [7, 8, 9]
# color = ['Red', 'Blue', 'Black', 'White', 'Pink']
# m=map(list,color)
# print(list(m))
#
# print(list(map(lambda x,y,z:x+y+z,nums1,nums2,nums3)))
# nums1 = [6, 5, 3, 9]
# nums2 = [0, 1, 7, 7]
# m=nums1+nums2
# print(m)
# print(list(map(lambda x,y:x-y,nums2,nums1)))
# x=[('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]
# print(list(map(lambda x:int(x[2][:2]),x)))
# l=[{'x': 20, 'y': 50, 'a': 10, 'b': 23},{'o': 20, 'g': 90, 'f': 10, 'e': 23},{'k': 80, 'h': 60}]
# x=map(str,l)
#
a = [1,2,3]

b = {1: [4,5,6],2: [7,8],3: [9, 10],4: [11, 12, 13],9: [14, 15],10: [16],13: [19, 20],19: [21]}
Output: [1, 4, 11, 12, 13, 19, 21, 20, 5, 6, 2, 7, 8, 3, 9, 14, 15, 10, 16]
l=[]
# for x in a:
#     for y in b.keys():
#         if x==y:
#             l.append(x)
#             for i in b[x]:
#                 if i in b.keys():
#                         l.append(i)
#                         l.append(b[i])
#

print(l)
