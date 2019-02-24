 import sys
 def getl():
	v=[]
	r=[]
	while(True):
		try:
			a,b = map(int,sys.stdin.readline().split())
		except ValueError:
			break
		v.append(a)
		v.append(b)
		r.append(l)
		v=[]
	for i in r:
		print(i[1]-i[0])
try:
	getv()
except:
	print('notvalid')
