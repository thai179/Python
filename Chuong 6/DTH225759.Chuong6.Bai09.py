def SoNT(so):
    dem=0

    for i in range(1,so):
        if so%i==0:
            dem+=1
    if dem == 1:
        return 1
    return 0
n=int(input("nhap so phan tu cua mang: "))
a = []
i=0
while i<n:
    tmp=int(input(f"nhap phan tu thu[{i}]: "))
    if tmp>0:
        a.append(tmp)
        i+=1
dem=0
for i in range(n):
    if a[i]%2!=0:
        print(a[i],end=" ")
        dem+=1
print(",co %d so le trong mang" %(dem))
dem=0
for i in range(n):
    if a[i]%2==0:
        print(a[i],end=" ")
        dem+=1
print(",co %d so chan trong mang" %(dem))
print("nhung so nguyen to trong mang: ",end=(""))
for i in range(n):
    if SoNT(a[i]):
        print(a[i],end=(" "))
print("\nnhung so khong phai so nguyen to trong mang: ",end=(""))
for i in range(n):
    if not SoNT(a[i]):
        print(a[i],end=(" "))