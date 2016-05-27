def prob_1 (n):
	return n%2==0

def prob_2 (f):
	c= (f-32)/1.8
	return c 

def prob_3 (b,p):
	res=1
	for i in range (p):
		res=res*b
		i=i+1	
	return res 

def prob_4 (C,l):
	h = len c
	li=l-h
	li=li//2
	ld=l-li
	return ("*"*li, c , "*"*ld)	

def prob_5 (a,b):
	res= (a[0]*b[0])+(a[1]*b[1])
	return res 

def prob_6 (l):
	l.sort()
	l.reverse()
	return l 