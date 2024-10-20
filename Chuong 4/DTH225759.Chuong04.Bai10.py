import time
import os
n = int(input("Nhap N: "))
while n%2==0:
    n = int(input("Nhap lai (so le): "))
mid=n//2
# hinh 1
for i in range(n):
    for j in range(n):
        if i<=mid:       
            if j>=mid and j<=mid+i:
                print("*", end =" ")
            elif i==mid:
                print("*", end =" ")
            else:
                print (" ", end =" ")
        else:
            if j<n-i:
                print ("*", end =" ")
            else:
                print (" ", end =" ")
    print()
time.sleep(5)
os.system('cls')
#hinh 2
for i in range(n):
    for j in range(n):
        if i<=mid:       
            if j==mid or j==mid+i:
                print("*", end =" ")
            elif i==mid:
                print("*", end =" ")
            else:
                print (" ", end =" ")
        else:
            if j==n-i-1 or j==0:
                print ("*", end =" ")
            else:
                print (" ", end =" ")

    print()
time.sleep(5)
os.system('cls')

#hinh 3
for i in range(n):
    for j in range(n):
        if i<=mid:       
            if j>=mid and j<n-i:
                print("*", end =" ")
            else:
                print (" ", end =" ")
        else:
            if j<=mid and j>=n-i-1:
                print ("*", end =" ")
            else:
                print (" ", end =" ")
    print()
time.sleep(5)
os.system('cls')
#hinh 4
for i in range(n):
    for j in range(n):
        if i<=mid:       
            if j==mid or j==n-i-1 :
                print("*", end =" ")
            elif i==0 and j>=mid:
                print("*", end =" ")
            else:
                print (" ", end =" ")
        else:
            if j==mid or j==n-i-1 :
                print ("*", end =" ")
            elif i==n-1 and j<= mid:
                 print("*", end =" ")
            else:
                print (" ", end =" ")
    print()

            
