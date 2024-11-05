n=int(input("Nhập số phần tử: "))
lst=[0]*n
i=0
while i<n:
    tmp=int(input(f"nhập số thứ[{i}]:"))
    if tmp>=lst[i-1]:
        lst[i]=tmp
        i+=1
print("List ngẫu nhiên là:")
print(lst)