import utils

# multidimensional partial sums
# given d-dimensional array A and query Q=[a1,b1]x[a2,b2]x...x[a_d,b_d]
# compute sum_{x_1...x_d in Q} A[x_1...x_d]

# RMQ: range minimum query
# input: array A
# query: given i,j, output min(A[i..j])
# see http://www.math.tau.ac.il/~haimk/seminar04/LCA-seminar-modified.ppt

# space O(sqrt N), time O(sqrt N)

from math import sqrt,log

def RMQ_1_precompute(A):
    n=len(A)
    k=int(sqrt(n))
    M=[min(A[k*i:k*(i+1)]) for i in range(k)]
    return M

def RMQ_1_query(A,M,i,j):
    k=len(M)
    l=i/k+1
    r=j/k
    mid=min(M[l:r+1]) # fully covered segments
    left=min(A[i:k*l+1]) # left part
    right=min(A[r*k:j]) # right part
    return min(left,mid,right)

# space O(N log N), time O(1)
# select two blocks that entirely (not disjoint!) cover the query range
# return their min (relies on idempotent)

def RMQ_2_precompute(A):
    n=len(A)
    # compute ranges of powers of two
    k=int(log(n,2))
    M=[[min(A[i:i+2**j]) for j in range(k)] for i in range(n)]
    return M

def RMQ_2_query(A,M,i,j):
    n=len(A)
    k=int(log(j-i,2))
    # min of A[i..i+2^k], A[j-2^k+1..j]
    return min(M[i][k], M[j-2**k+1][k])

# space O(N) time O(log N)
# using dyadic ranges / segment trees
