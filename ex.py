# # ex1
# list =[]
# for i in range(10):
#     list.append(i)
# print(list)
#
# for i in range(len(list)):
#     list[i] = list[i] * 10
# print(list)

# ex2
# list = ['a','b','c']
# list.reverse()
# print(list)

# ex3

# # ex4
# my_list = [12,65,54,39,102,339,221,50,70]
# result =[]
# for i in range(len(my_list)):
#     if my_list[i] % 13 == 0:
#         result.append(my_list[i])
# print(result)

# ex5
# f = open('input.txt','r')
# a = f.read()
# print(a)
list = [[1,2,3,4,5,6,7,8,9],[2,4,6,8,10,12,14,16,18]]
for i in range(len(list[0])):
    for j in range(len(list[0])):
        a=list[0][i]*list[1][j]
        print(a, end=' ')
    print('\n')
