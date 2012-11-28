import utils

# output all ways of parenthesizing n "(",")" (nth Catalan number)
def bracket(n):
	if (n==0):
		return [""]
	L=[]
	for i in range(1,n+1):
		L = L+["("+l+")"+r for l in bracket(i-1) for r in bracket(n-i)]
	return L

# to count the number of ways
# we have P(n)=sum_i P(i)*P(n-i)
# (1..i) (i+1..n)
def parens(n):
	A=[0]*n
	A[0]=1
	for i in range(1,n):
		A[i]=sum((A[j]*A[i-j-1]) for j in range(0,i))
	return A[n-1]
	
