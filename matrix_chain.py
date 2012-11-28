import utils

# matrix chain multiplication
# let T[i,j] = cost of multiplying (Ai...Aj)
#			 = min_{i<=k<j} (rows(Ai)*cols(Ak)*cols(Aj) + T[i,k] + T[k+1,j])
#			 = min_{i<=k<j} (P(i-1)*P(k)*P(j) + T[i,k] + T[k+1,j])
# since matrix i is P(i-1)xP(i)
# also need S[i,j] = optimal k for multiplying (Ai...Aj)

def matrix_chain(p):
	n=len(p)-1
	T=matrix(n,n)
	S=matrix(n,n)
	for i in range(n-1,-1,-1):
		for j in range(i+1,n):
			T[i][j]=1e6 # hack
			for k in range(i,j):
				v=p[i]*p[k+1]*p[j+1] + T[i][k] + T[k+1][j] # shifted the indexes of P to account for zero-indexing on i,j etc.
				if (v<T[i][j]):
					T[i][j]=v
					S[i][j]=k
	return T,S

def print_matrix_chain(S,i,j):
		if (i==j):
			return " A_"+str(i)+" "
		else:
			s= "("
			k=S[i][j]
			s+=print_matrix_chain(S,i,k)
			s+=print_matrix_chain(S,k+1,j)
			s+= ")"
			return s
			
def print_matrix_mult(S,i,j):
	if (i == j-1):
		print str(i)+" x "+str(j)
	else:
		k=S[i][j]
		print_matrix_mult(S,i,k)
		print_matrix_mult(S,k+1,j)
		
