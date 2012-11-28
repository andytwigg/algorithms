import utils

from random import randint

# x^n = (x^(n/2))^2 n even 
#		x.x^(n-1) n odd
def pow(x,n):
	if (n==0):
		return 1
	elif (n%2==0):
		y=pow(x,n/2)
		return y*y
	else:
		return x*pow(x,n-1)

def fib(n):
	L=[0]*(n+1)
	L[1]=1
	for i in range(2,n+1):
		L[i]=L[i-1]+L[i-2]
	return L[n]
	
def polynomial_add(A,B):
	n=len(A)
	return [A[i]+B[i] for i in range(n)]

def polynomial_mult(A,B):
	n=len(A)
	A.extend([0]*n)
	B.extend([0]*n)
	# coefficient of x^j in A*B=sum of all coefficients of x^k,x^{j-k} in A,B
	C = [sum(A[k]*B[j-k] for k in range(j+1)) for j in range(2*n-1)]
	return C

def polynomial_eval(A,x):
	y=0
	for a in A:
		y = x*y+a # going from highest to lowest coefficient
	return y

# O(n^lg 3) multiplication
# input: (Ax+B) * (Cx+D) = x^2(AC)+x(AD+BC)+(BD)
# (1)=(A+B)+(C+D)=AC+AD+BC+BD, (2)=AC, (3)=BD
# then (AD+BC)=(1)-(2)-(3)

def polynomial_mult_fast(A,B):
	n=len(A)
	if (n==0):
		return []
	if (n==1):
		return [A[0]*B[0]]
	Al=A[:n/2]
	Au=A[n/2:]
	Bl=B[:n/2]
	Bu=B[n/2:]
	x=polynomial_mult_fast(polynomial_add(Al,Au),polynomial_add(Bl,Bu))
	y=polynomial_mult_fast(Au,Bu)
	z=polynomial_mult_fast(Al,Bl)
	zz=polynomial_add(x,map(lambda x:x*-1,y))
	zz=polynomial_add(zz,map(lambda x:x*-1,z))
	C=y
	C.extend(zz)
	C.extend(z)
	return C
	
