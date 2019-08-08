def checkPrimeNumber(n):
    a = int
    if n == 2:
        a = 1
    for i in range(2,n):
        if n % i == 0:
            a = 0
            break
        else:
            a = 1
    return a
def swap(n):
    l = list(str(n))
    a = l[0]
    del l[0]
    l.append(a)
    kq = 0
    for i in range(len(l)):
        kq = kq + int(l[i])* (10**(len(l) - i - 1))
    return kq

def kiemtra(n):
    l = list(str(n))
    for i in range(len(l)):
        if checkPrimeNumber(n)  == 0:
            print('Not curcle prime number')
            break
        else:
            print(n)
            n = swap(n)
    # so = n
    # if checkPrimeNumber(n) == 1:
    #     print(n)
    #     n = swap(n)
    #     if n != so:
    #         kiemtra(n)
    #     else:
    #         return 0
    # else:
    #     print('khong phai')


kiemtra(3119)
