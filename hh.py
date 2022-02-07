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


def divide(x, y):
    try:

        result = x /y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:print(result)
    finally :print("its working")



# Look at parameters and note the working of Program
divide(20,0)


