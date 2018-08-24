vrin = int(input(""))
 
if (( vrin%400 == 0)or (( vrin%4 == 0 ) and ( vrin%100 != 0))):
    print("yes")
else:
    print("no")
