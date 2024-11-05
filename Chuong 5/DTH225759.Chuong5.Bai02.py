def toiUuChuoi(s):
    arr=s
    arr=arr.strip()
    arr2=arr.split(' ')
    arr=""
    for x in arr2:
        word = x
        if len(word.strip())!=0:
            arr=arr+word+" "
    return arr.strip()
s=" ajndc k kvndk    kandkvnk     kdsnvk kdvn "
print(s,"=>",len(s))
s=toiUuChuoi(s)
print(s,"=>",len(s))