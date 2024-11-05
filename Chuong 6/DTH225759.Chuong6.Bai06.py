from random import randrange

n=int(input("Nhập số phần tử: "))
lst=[0]*n
for i in range(n):
    tmp=randrange(-100,100)
    if tmp not in lst:
        lst[i]=tmp
print("List ngẫu nhiên là:")
print(lst)