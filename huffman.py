# optimal prefix free code (huffman)
# nb the keys don't need to be ordered (unlike optimal binary search trees)
# f(i)=frequency of key i
# optimal substructure: consider an optimal tree T for characters C
# and two sibling leaves x,y with parent z
# then T\{x,y} is an optimal tree for C\{x,y}
# dyn prog: T(i)=T(i\{x,y})+f(x)+f(y)

# greedy:

import utils

from heapq import heappush, heappop, heapify

def huffman(f):
	n=len(f)
	Q=[(f[i],i) for i in range(n)]
	heapify(Q)
	T={i:None for i in range(n)}
	for i in range(n-1): #i=0..n-2
		fx,x=heappop(Q)
		fy,y=heappop(Q)
		z=len(T) # next free slot in T
		T[z]= (x,y) # z=new node(x,y)
		heappush(Q,(fx+fy,z)) # push(Q,(fx+fy,z))
	T[len(T)]=heappop(Q)[1] # the root node
	return T

def printTree(tree, key, depth = 0):
	if tree[key] == None or len(tree[key]) == 0:
		print "\t" * depth, "leaf:"+str(key)
	else:
		for k in tree[key]:
			print "\t" * depth, k
			printTree(tree, k, depth+1)
			
def codeCost(T,f,i,d=0):
	if (T[i]==None):
		return d*f[i]
	else:
		return codeCost(T,f,T[i][0],d+1) + codeCost(T,f,T[i][1],d+1)
		

