username = "chaiaurcode"

# def func():
#     # username = "chai"
#     print(username)

# print(username)
# func()

x = 90

# def func2(y):
#     z = x + y
#     return z

# print(func2(10))


# def func3():
#     global x
#     x = 88

# func3()
# print(x)


# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2

# myResult = f1()
# myResult()


def chaiCoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))
print(g(3))