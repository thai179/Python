from math import sqrt
def TinhCanBacHai(n):
    kq=0
    for i in range (0,n):
        kq = sqrt(2+kq)
    return kq
n=int(input("Nhap N: "))
print("Ket qua phep tinh la: ",TinhCanBacHai(n))
