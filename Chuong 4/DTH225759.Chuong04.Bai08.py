from math import log10
print("Chuong trinh tinh loga(x): ")
a= x= 0
while True:
    a = float(input("Nhap so a: "))
    x = float(input("nhap vao so x: "))
    if a<=1 or x<1:
        print("nhap khong hop le!")
    else:
        break 
print(" ket qua loga(x)= ",log10(x)/log10(a))