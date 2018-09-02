vrin = int(input(""))
factorial = 1
if vrin < 0:
   print("Sorry,factirial does not exist for negative numbers")
elif vrin == 0:
   print("1")
else:
   for i in range(1,vrin + 1):
       factorial = factorial*i
   print(factorial)
   
