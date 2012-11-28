import utils

# mergesort
def mergesort(A):
	n=len(A)
	if (n<=1):
		return A
	L=mergesort(A[0:n/2])
	R=mergesort(A[n/2:n])
	return merge(L,R)

def merge(L,R):
	A = []
	i=0
	j=0
	while (i<len(L) and j<len(R)):
		if (L[i] <= R[j]):
			A.append(L[i])
			i=i+1
		else:
			A.append(R[j])
			j=j+1
	# check for any leftovers
	if (i<len(L)):
		for k in L[i:]:
			A.append(k)
	if (j<len(R)):
		for k in R[j:]:
			A.append(k)

	return A
