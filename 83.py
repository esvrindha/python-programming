 def main():
	v=[]
	while(yes):
		s=input()
		try:
			if '/' in s:
				a,b = map(int,s.split('/'))
				r=a/b
			else :
				a,b=map(int,s.split('%'))
				r=a%b
			v.append(int(r))
			r=[]
		except ValueError:
			break
	for i in v:
		print(i)
try:
	main()
except:
	print('invalid')
