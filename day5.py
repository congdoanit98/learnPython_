# import math as m
# try:
#     print(math.pi)
# except NameError:
#     print('Exception')

# def divide(x,y):
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         print('Division by zero')
#     else:
#         print('Result is', result)
#     finally:
#         print('Clap!')
# divide(2,1)
# print()
# divide(2,0)
# # try except
# A = '1'
# B = 2
# try:
#     print(A + B)
# except TypeError:
#     print('type error')
#     A = int(A)
#     print(A+B)

# def devide(x,y):
#     try:
#         result = x /y
#     except ZeroDivisionError:
#         print('division by zero')
#     except:
#         print('Exception')
#     else:
#         print(f'{x:0.1f}/{y:0.1f}={result:0.1f}')
#     finally:
#         print('Excuting finally clasue')
# for i in range(4):
#     if i == 3:
#         i='0'
#     print(devide(10,i))

# # CLASS
# class MyClass:
#     var = 42
#     def hello_world():
#         return 'Hello, world!'
#
# print(MyClass.var)
# MyClass.var = 23
# print(MyClass.var)
# print(MyClass.hello_world())

# class MyCounter:
#     def set(self):
#         self.counter = 0
#         return self.counter
# C1 = MyCounter()
# C1.set()
# print(C1.counter)

# class MyCounter:
#     def __init__(self, value = 0):
#         self.counter = value
#
# C1 = MyCounter()
# C2 = MyCounter(45)
# print(C1.counter)
# print(C2.counter)

counter = 100
class MyCounter:
    counter = 200
    def __init__(self, value = 0):
        print("counter:",value)
        self.counter = value
    def get(self):
        return self.counter
    def set(self, value):
        counter = value
C1 = MyCounter()
C2 = MyCounter(42)
C1.set(10)
print(C1.counter+C2.counter)
print(MyCounter.get(C1)+C2.get())
print(counter)