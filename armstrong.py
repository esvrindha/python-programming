
vrin = int(input(""))

vamp = len(str(vrin))
sum = 0
bindu = vrin

while(bindu !=0):
  sum = sum + ((bindu % 10) ** vamp)
  bindu = bindu // 10

if sum == vrin:
   print("yes")
else:
   print("no")
