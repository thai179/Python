#Chương trình tính năm nhuần
print("chương trình tính năm nhuần")
nam=int(input("nhập vào năm cần tính: "))
if(nam%4==0 and nam%100!=0 or nam%400==0):
    print("đây là năm nhuần")
else :
    print("đây không là năm nhuần")
