import utils

# quicksort
def swap(A,i,j):
	tmp=A[i]
	A[i]=A[j]
	A[j]=tmp

def quicksort(A,p,q):
	if p<q:
		i=partition(A,p,q)
		quicksort(A,p,i-1)
		quicksort(A,i+1,q)
		
def quicksort_iterative(A,p,q):
	S=[] # stack
	S.push((p,q))
	while (len(S)>0):
		p,q = S.pop()
		if (p<q):
			i=partition(A,p,q)
			S.push(A,i+1,q)
			S.push(A,p,i-1) # this one is the next to be called (first in the recursive implementation)

# NB stack depth may be O(n) if we push the smallest one first
# if we push the largest one first, stack depth is O(log n)

# maintain p[1...i] [i+1...j] [...rest]
#			  <=x      >=x 
def partition(A,p,q):
	swap(A,p,randint(p,q)) # put a random element at the front
	x=A[p]
	i=p
	for j in xrange(p+1,q+1):
		if A[j] <= x:
			i=i+1
			swap(A,i,j)
	swap(A,p,i) # put the pivot in its right place
	return i

# randomized select

def randselect(A,p,q,i): # ith smallest in A[p..q]
	if (p==q): return A[p]
	r=partition(A,p,q)
	k=r-p+1 # rank of A[r] in A[p..q]
	if (i==k): return A[r]
	if (i<k): return randselect(A,p,r-1,i)
	if (i>k): return randselect(A,r+1,q,(i-k))
	