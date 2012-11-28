
def binary_search(A,x):
	n=len(A)
	if (n==1): return 
	if (x==A[n/2]): return x
	if (x<A[n/2]): return binary_search(A[:n/2],x)
	if (x>A[n/2]): return binary_search(A[n/2:],x)

def matrix(m,n):
	return [[0]*n for _ in xrange(m)]
