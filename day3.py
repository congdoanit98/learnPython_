# #IF, ELSE, ELIF
# if 3<6:
#     print('3 is less than 6')
# if 5>6:
#     print('6 is less than 5')
# n= 60
# if n<45:
#     print('n is bigger than 50')
# elif n <35:
#     print('haha')
# else: print(':((')
#
# if 3>4:
#     print(':((')
# else:
#     print(':))')
#
# number = 1
# if number < 0:
#     print('so am')
# print('so duong')
#
# n = 9
# if n <10:
#     if n % 2 ==0:
#         print('so chan')
#     else:
#         print('so le')
# else:
#     if n % 2 == 0:
#         print('so chan but lon hon 10')
#     else:
#         print('so le but lon hon 10')

# LOOP STATEMENT
# number = 5
# while number <=8:
#     print(number)
#     number +=1

# n = int(input('Nhap so'))
# while n > 6:
#     if n % 2 == 0:
#         print(n)
#
#         print('so chan')
#     else:
#         print(n)
#         print('so le')
#     n -= 1

# for x in [1,2,3,4]:
#     print(x)
#
# print(range(5))
# print(list(range(5)))
# print(list(range(1,8,3)))
#
# for i in range(3, 24, 5):
#     print(i, end=' ')

# # LEN
# t = [2 , 8 , 5]
# for i in range(len(t)):
#     print(t[i])
#     t[i] = t[i] + 3
# print(t)

# # DEF
# def display(qq):
#     for i in qq:
#         print(i, end=' ')
# t = [2,3,5]
# display(t)

# # ENUMERATE
# t = [2,5,8,6,45]
# for i, v in enumerate(t):
#     print(i, v)
#
# t = [2,3,5,6,7]
# for a in t:
#     print(a)
# else:
#     print('end of loop')

# # CONTROL FLOW
# i = 0
# j = 100
# while i < 10:
#     i += 1
#     print(i)
#     while j <105:
#         j += 1
#         print(j)
#         break
# else:
#     print('hello')

# Exercise
def pyrammid(d):
    for i in range(d+1):
        for j in range(i):
            print('*',end='')
        print('\n')
pyrammid(5)

def fibo(n):
    t = [0,1]

    for i in range(2,n+1):
        a = t[i-1] + t[i-2]
        t.append(a)
    del t[0]
    return t
print(fibo(2))

def prime_number(n):
    s={2}
    for i in range(2,n+1):
        for j in (range(2,i)):
            if (i%j == 0):
                break
            else:
                s.add(i)
    for i in range(len(s)):
        print(s.pop(), end=' ')

prime_number(2)
def ex1(t):
    for i in range(t+1):
        print('*'*i)
        i+=1
ex1(4)
