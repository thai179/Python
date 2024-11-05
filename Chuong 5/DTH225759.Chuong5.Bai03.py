def KTSoNT(n):
    dem=0
    for i in range(1,n+1):
        if n % i ==0:
            dem+=1
    return dem==2
s=input("nhập vào chuỗi của bạn cách nhau bởi ';' :")
arr=s.split(';')
demsochan=0
demsoam=0
demsont=0
sum=0
for x in arr:
    print(x)
    so = int(x)
    if so%2==0:
        demsochan+=1
    if so<0:
        demsoam+=1
    if KTSoNT(so):
        demsont+=1
    sum+=so
print("Số lượng sô chăn: ",demsochan)
print("Số lượng sô âm: ",demsoam)
print("Số lượng sô nguyên tố: ",demsont)
print("Trung bình cộng của mảng là: ",sum/len(arr))

