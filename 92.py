def sumitall():
	v=int(input())
	r=[]
	sum=0
	for i in range(v):
		r.append(int(input()))
		sum+=r[i]
	print(sum)
try:
	sumitall()
except:
	print('invalid')
