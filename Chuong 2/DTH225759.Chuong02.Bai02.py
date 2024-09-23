t=-1
while(t<0):
    t=int(input("nhập vào số giây: "))
hour=(t//3600)%24
minute=(t%3600)//60
second=(t%3600)%60
if hour > 12:
    print(hour-12,":",minute,":",second,"PM")
else:
    print(hour,":",minute,":",second,"AM")