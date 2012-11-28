import utils


# longest common subsequence
# let C[i,j] = |LCS(x[1..i], LCS(y[1..j]))
# C[i,j] = C[i-1,j-1] + 1 if x[i]==y[j] # take i,j - can only make LCS longer
#          max(C[i,j-1], C[i-1,j]) # advance one of them

def LCS(x,y):
	m=len(x)
	n=len(y)
	C=matrix(m+1,n+1)
	P=matrix(m+1,n+1)
	for i in range(1,m+1):
		for j in range(1,n+1):
			if (x[i-1]==y[j-1]):
				C[i][j]=C[i-1][j-1]+1
				P[i][j]=1 # mark it
			else:
				C[i][j]=max(C[i][j-1],C[i-1][j])
	# reconstruct
	S=[]
	i=m
	j=n
#	for l in C: print l
#	print "---------------------------"
#	for l in P: print l
	while(i>0 and j>0):
			if (P[i][j]==1):
				assert (x[i-1] == y[j-1])
				S.append(x[i-1])
				i=i-1
				j=j-1
			else:
				if (C[i-1][j]>=C[i][j-1]):
					i=i-1
				else:
					j=j-1
	S.reverse()
	return S

# exercise: LCS with space O(min(n,m))


# problem 15-2: longest palindrome subsequence
# every common subsequence between S, reversed(S) is a palindrome subsequence of S
# eg ChARACter, retCARAhC

