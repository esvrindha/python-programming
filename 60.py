vish=int(raw_input(""))
if vish < 0:
  print("")
else:
  sum=0
  while(vish > 0):
     sum += vish
     vish-= 1
  print(sum)
