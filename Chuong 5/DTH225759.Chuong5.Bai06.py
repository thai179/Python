import re
def NegativeNumberInString(str):
    tmp=re.findall(r'-\d+',str)
    return tmp
str=input("nhập chuỗi: ")
print("Các số âm trong chuỗi là: ",NegativeNumberInString(str))
