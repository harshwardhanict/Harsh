'''x = int(input("hh; "))
l =[i for i in range(0,x+1)]
print(" ".join(map(str,l)))
'''

'''
y = [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19,19]),2]

l = [i for i in map(list,y[0])]
x =[[i, j] for i, row in enumerate(l) for j, n in enumerate(row) if n == y[1]]
print(x)
'''

#
# def divide(x, y):
#     try:
#
#         result = x /y
#         print("Yeah ! Your answer is :", result)
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     else:print(result)
#     finally :print("its working")
#
#
#
# l1=[]
# for i in range(3):
#     s=input("Enter input:")
#     l=s.split(",")
#     print(l)
#     t=tuple(l)
#     print(t)
#     l1.append(t)
#     l1.sort()
# print(l1)
# l = [(100,(0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55))]
# l1 = [i for i in map(list,l)]
# p=list(l1[0][1])
# l2=[i for i in p if i>l[0][0]]
# print(l2)
