dig1=raw_input()
dig2=raw_input()
dig3=raw_input()
if dig1<dig2:
	if dig2<dig3:
		print dig3
	else:
		print dig2
elif dig2<dig3:
	if dig3<dig1:
		print dig1
	else:
		print dig3
elif dig3<dig1:
	if dig1<dig3:
		print dig2
	else:
		print dig1
