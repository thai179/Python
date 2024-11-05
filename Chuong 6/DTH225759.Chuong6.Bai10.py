def TaoMaTran(m,n):
    D=[]
    for i in range(m):
        row=[]
        for j in range(n):
            tmp=int(input(f"nhap a[{i}][{j}]:"))
            row.append(tmp)
        D.append(row)
    return D
def CongMaTran(A,B):
    D=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[i])):
            tmp= A[i][j]+B[i][j]
            row.append(tmp)
        D.append(row)
    return D
def HoanViMaTran(A):
    D=[]
    for i in range(len(A[0])):
        row =[]
        for j in range(len(A)):
            tmp = A[j][i]
            row.append(tmp)
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element,end='\t')
        print()
hanga=int(input("nhap so hang A: "))
cota=int(input("nhap so cot A: "))
hangb=int(input("nhap so hang B: "))
cotb=int(input("nhap so cot B: "))

A=TaoMaTran(hanga,cota)
B=TaoMaTran(hangb,cotb)


if hanga == hangb and cota == cotb:
    print("tong 2 ma tran =")
    tmp=CongMaTran(A,B)
    XuatMaTran(tmp)
XuatMaTran(A)
print("ma tran hoan vi")
tmp = HoanViMaTran(A)
XuatMaTran(tmp)



