from random import randrange
def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element,end='\t')
        print()
def LayDong(r):
 R=D[r]
 return R
def XuatList1Chieu(R):
    for element in R:
        print(element,end='\t')
def LayCot(c):
    C=[]
    for i in range(len(D)):
        C.append(D[i][c])
    return C
def MAX(D):
    max=D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if(max<D[i][j]):
                max=D[i][j]
    return max
m=int(input("Nhập số dòng:"))
n=int(input("Nhập số cột:"))
D=TaoMaTran(m,n)
XuatMaTran(D)
r=int(input("Mời bạn nhập dòng muốn xuất:"))
XuatList1Chieu(LayDong(r))
c=int(input("\nMời bạn nhập cột muốn xuất:"))
XuatList1Chieu(LayCot(c))
max=MAX(D)
print("\nSố lớn nhất trong ma trận=",max)