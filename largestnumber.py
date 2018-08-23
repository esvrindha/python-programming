dig1=int(raw_input(""))
dig2=int(raw_input(""))
dig3=int(raw_input(""))
if (dig1>dig2)and(dig1>dig3):
    largest = dig1
elif (dig2>dig1)and(dig2>dig3):
    largest = dig2
else:
    largest= dig3
print(largest)
