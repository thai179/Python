def fibonacci(n):
    if n<=2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
def listfibo(n):
    for i in range(1,n+1):
        print(fibonacci(i),end='\t')
n=int(input("Nhâp vào sô N để tính dãy fibonacci: "))
print(fibonacci(n))
listfibo(n)
