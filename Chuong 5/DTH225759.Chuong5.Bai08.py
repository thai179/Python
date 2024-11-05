import os
def TachTen(str):
    ten = os.path.basename(str)
    tmp,_= os.path.splitext(ten)
    return tmp
def TachTenMP(str):
    ten = os.path.basename(str)
    return ten
str=input("nhập dường dẫn bài hát: ")
print("Tên bài hát: ",TachTen(str))
print("Tên bài hát còn giữ lại đuôi .mp",TachTenMP(str))