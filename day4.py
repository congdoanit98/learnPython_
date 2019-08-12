# # FUNCTION
# def add(a,b):
#     return a + b
# print(add(3,4))
#
# def haha(c,d):
#     return c+d, c-d
# print(haha(6,5))
# t,y = haha(9,8)
# print(t,y)
#
# def my_s(str):
#     print(str + ' jjjjj')
# my_s('haha')
# my_s()

# def power(base, exp):
#     return base ** exp
# print(power(3,4))
# print(power(exp=4,base=3))
#
# def addd(a1, a2=2, a3=3):
#     return a1 + a2 + a3
# print(addd(3,8,9))
# print(addd(5))
#
# def po2(*ddd):
#     a,b,c,d = ddd
#     return a +b + c + d
#
# print(po2(1,2,3,7))

# # LAMBDA FUNCTION
# vuong = lambda x,y: x+y
# print(vuong(5,7))
# # MODULE
# import test as doan
# print(doan.add(3,5))
# from test import *
# v = add(5,6)
# print(v)

# INPUT/OUTPUT
# file1 = open('document.txt','r')
# filect = file1.readlines()
# for i in filect:
#     print(i)
# file1.close()
#
# f = open('out.txt','wt')
# print('hi', file=f)
# f.close()
f = open('out.txt','rb+')
print(f.write(b'0123456789abcdef'))
f.seek(5)
print(f.read(1))
f.seek(-8,2)
print(f.read(1))
print(f.read(2))
f.close()