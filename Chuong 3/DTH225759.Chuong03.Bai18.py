n=int(input("nhập n:"))
for i in range(0,n):
    for j in range(0,n):
        if i == 0 or i==n-1 or j == 0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(0,n):
    for j in range(0,n):
        if j >= n-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
mid = n//2
for i in range(0,n):
    for j in range(0,n):
        if i<=mid:
            if i==mid:
                print("*",end=" ") 
            elif j==0 or j==i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if j==n-1 or j==i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()