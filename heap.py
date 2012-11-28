import utils
		
# heap
# array A, with A[0] used to store size(A)

def parent(i): return i/2
def left(i): return 2*i
def right(i): return 2*i+1

def check_heap(A,i):
	if (i==0 or i>A[0]):
		return True
	if (i==1):
		return check_heap(A,left(i)) and check_heap(A,right(i))
	else:
		return (A[i]<=A[parent(i)]) and check_heap(A,left(i)) and check_heap(A,right(i))

# (max-)heap property: A[parent(i)]>=A[i]
# heapify: O(log n)
# T(n) <= T(2n/3) + O(1)
def heapify(A,i): # heapify the tree rooted at position i assuming subtrees left(i), right(i) are heaps
	n=A[0]
	l=left(i)
	r=right(i)
	#print i,A[i]
	# left child is largest
	if ((l<=n) and (A[l] > A[r]) and (A[l] > A[i])):
		swap(A,l,i)
		heapify(A,l)
	# right child is largest
	elif ((r<=n) and (A[r] > A[l]) and (A[r] > A[i])):
		swap(A,r,i)
		heapify(A,r)


# build-heap: bottom-up, O(n)

def build_heap(A):# we will overwrite the first element
	A[0]=len(A)-1
	n=A[0]
	for i in range(n/2,0,-1): # n/2...1
		heapify(A,i)
	
# heapsort: O(n log n), worst-case, in-place
# instead of repeatedly extracting max, do the following:
# first, build a heap from A
# with n=A[0], swap A[1] with A[n], decrement A[0] (size)
# heapify(A,1), and repeat until n=2

def heapsort(A):
	build_heap(A)
	n=A[0]
	for i in range(n,0,-1): # n...2
		swap(A,1,i)
		A[0] = A[0]-1
		heapify(A,1)
	A[0]=0

# extract-max: O(log n)
# store max=A[1], set A[1]=A[n], reduce A[0] by 1, heapify(A,1)
def extract_max(A):
	n=A[0]
	if (n==0): return None
	x=A[1]
	A[1]=A[n]
	A[0] = A[0]-1
	heapify(A,1)
	return x

# insert: O(log n)
# insert at end of array, then percolate up until heap property no longer violated
def heap_insert(A,k):
	A[0]=A[0]+1
	n=A[0]
	# assume we have size in A
	A[n]=k
	while (n>1 and A[parent(n)]<k):
		swap(A,n,parent(n))
		n=parent(n)

# increase-key: O(log n)
# can only go up in the heap
# basically the last 3 lines of heap_insert
def heap_increase_key(A,i,k):
	A[i]=k
	while (i>1 and A[parent(i)]<k):
		swap(A,i,parent(i))
		i=parent(i)

# decrease-key: O(log n)
# can only go down in the heap
def heap_decrease_key(A,i,k):
	A[i]=k
	heapify(A,i)
