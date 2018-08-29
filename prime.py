teja=int(input(""))
vrin=0
for i in range(2,teja//2+1):
    if(teja%i==0):
        vrin=vrin+1
if(vrin<=0):
    print("yes")
else:
    print("no")
