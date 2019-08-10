# remember the knowkegde of yesterday
# a = input()
# b = input()
# c = input()
# d = input()
# e = a + b + c + d
# print(e)

# String and index
# mystr = 'Doan Black'
# print(mystr[0])
# print(mystr[5])
# a = input()
# print(len(a))
# print(a[:4])
# print(a[3:6])
# print(a[8:])

# mystr = 'Doan Black'
# print('D' in mystr)
# print('an' in mystr)
# print('we' in mystr)

# find function: need remember
# email = input('input your email:')
# print(email[:email.find('@')])

# A = [4,5,6,7]
# B = A
# C = A.copy()
# A.append(8)
# B.clear()
# print(A)
# print(B)
# print(C)

# S = [0,2,3,9,3]
# print(S.index(2))
# S.insert(3,55)
# print(S)
# S.remove(3)
# S.reverse()
# print(S)
# t = int(input('Input number to count:'))
# print(S.count(t))

# S.sort()
# S.insert(3,1)
# S.sort()
# print(S)
# print(S.pop())
# print(S)

# # Ex1
# L = [1,2,3]
# L.append('a')
# print(L)
#
# # Ex2
# l = [1,2,3]
# d = l
# g = l.copy()
# l.clear()
# print(d)
# print(l)
# print(g)
#
# #Ex3
# L = [1,2,3]
# print(L.count(3))
# L.append(3)
# print(L.count(3))
#
# # Ex4
# L = [1,2,3,4,6,5,7]
# print(L.index(6))
# L.insert(1,6)
# print(L.index(6))
#
# # Ex5
# L = [1,2,3,4,6,5,7,6]
# print(L.index(6))
# L.remove(6)
# print(L.index(6))
# L.reverse()
# print(L.index(6))
# print(L)
#
# # Ex6
# L = [1,7,2,5,4,6,7,10,32,-4]
# L.sort()
# print(L)
# L.reverse()
# print(L)
# print(L.pop())
# print(L)

# # TUPLE
# t1 = (1,2,3,'a','b')
# print(t1[1:4])
# print(t1[1:4:2])
# print(t1*3)
# t2 = (2,4,8,50)
# print(max(t2))
# print(min(t2))
# print(t2.count(8))

# a = (2,6)
# f ,s =a
# print('first =',f, 'second =', s)
# print(type(a))
# b=[]
# print(type(b))

# swapping value
# a = 2
# b = 5
# a,b = b,a
# print(a,b)

# student = [('doan',[179,50]),('lam',[169,30])]
# print(student[0])
# print(student[1][1][1])

# # SET
# s1 = {1,2,3}
# print(s1)
# s2 = set('doan')
# print(s2)
# print(set('hello'))
# s3 = {"nguyen", "cong", "doan"}
# print(s3)
# s1.add(6)
# print(s1)
# print('doan' in s3)
# s2.clear()
# print(s2)
# s1.update((7,8,9))
# print(s1)
#
# s4 = {1,2,3}
# s5 = {3,4,5}
# print(s4&s5)
# print(s4|s5)
# print(s4.difference(s5))

#DICTIONARY
mix = {'color':['red','yellow'],'size':['big','small']}
print(mix)
print(mix['size'])
    # print 'small'
print(mix['size'][1])
    # add items in dictionary
mix['height'] = ['tall','short']
print(mix)
del mix['color']
print(mix)
print(mix.get('height',0))
    # Tra ve default neu khong tim thay key trong dictionary
print(mix.get('doan',5))
print(mix.keys())