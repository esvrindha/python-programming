v=int(raw_input(""))
r=list(map(int,raw_input("").split(' ')))
for i in range(v):
  if(r[i]<r[i+1]):
    print(i+1)
    break
   
