import utils

# rod cutting

# rod can be cut at positions x[0]...x[n-1]
# cutting a length l costs l
# C[i,j]=cost of cutting rope from cut i to j
# C[i,i]=0
# C[i,j]=|x[j]-x[i]| + min_{i<=k<=j} C[i,k]+C[k,j] # cutting at k

X=sorted([randint(1,20) for _ in range(4)]) # 20 cuts between 1-100

def cut(X):
	n=len(X)
	C=matrix(n,n)
	for i in range(n-1,-1,-1): # i=n-1 to 0
		for j in range(i,n): #j=i to n-1
			C[i][j] = X[j] - X[i] + min(C[i][k]+C[k][j] for k in range(i,j+1))

	return C[0][n-1]

	
# rod cutting from CLRS

# C[n]=max profit from cutting rod of length n
# C[0]=0
# C[i]=max_{k<=i} P[k]+C[i-k]
# (more complex, equivalent):
# C[i] = max(P[i], max_{k<i} C[i-k])

P=[0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

def cutrod(P,n):
	C=[0]*(n+1)
	for i in range(1,n+1):
		C[i]=max(P[k]+C[i-k] for k in range(1,i+1)) 
	return C[n]

def cutrod_sizes(P,n): # returns the first size to cut
	C=[0]*(n+1)
	S=[0]*(n+1)
	for i in range(1,n+1):
		for k in range(1,i+1):
			if (C[i] < P[k]+C[i-k]):
				C[i] = P[k]+C[i-k]
				S[i] = k # length of first piece to cut off a rod of length i
	return S

def cutrod_solution(P,n):
	S = cutrod_sizes(P,n)
	cuts=[]
	while (n>0):
		cuts.append(S[n])
		n=n-S[n]
	return cuts