vrin=int(raw_input(""))
e=0
while (vrin!=0):
  r=vrin%10;
  e=e*10+r
  vrin/=10;
print(e)
