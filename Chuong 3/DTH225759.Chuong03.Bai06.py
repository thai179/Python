import math
n=100
while n<0 or n>99:
    n=int(input("nhập số n(-99 đến 99): "))
docdv=["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
dochc=["Mười","Hai mươi","Ba mươi","Bốn mươi","Năm mươi","Sáu mươi","Bảy mươi","Tám mươi","Chín mươi"]
dochdv=["mốt","hai","ba","bốn","lăm","sáu","bảy","tám","chín"]
if n<=9 and n>=0:
    print(docdv[n])
elif n==10:
    print(dochc[0])
elif n==11:
    print(dochc[0],"một")
else:
    tmp= n//10
    tmp2=n%10
    print(dochc[tmp-1],dochdv[tmp2-1])

