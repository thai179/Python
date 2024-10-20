x=int(input("Nhập x: "))
n=int(input("Nhập n: "))
s=0
for i in range(1,2*(n)+2,2):
    tu=x**i
    mau=1
    for j in range(1,i+1):
        mau=mau*j
    s+=tu/mau
print("S({0},{1}) = {2}".format(x,n,s))