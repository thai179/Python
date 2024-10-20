def tongUoc(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
n=int(input("hãy nhập sô muốn kiểm tra: "))
if n==tongUoc(n):
    print(n,"là số hoàn hảo")
else: print(n,"không là số hoàn hảo")
if n<tongUoc(n):
    print(n,"là số thịnh vượng")
else: print(n,"không là số thịnh vượng")