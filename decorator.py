def f1(fun):
    print("hax")
    return fun


@f1
def f2():
    print("ha")


f2()