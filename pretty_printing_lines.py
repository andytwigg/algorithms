import utils

# 15-3
# max line length M
# line l contains words [i..j]
# C[j]=cost of printing words 1..j starting on a blank line
# 		 = min_{i<j: len(i..j)<M} C[i-1] + (M-len(i..j))^3 # put words i..j on last new line

def toLengths(s):
	return map(lambda x:len(x), s.split(" "))

def calcPrintNeat(s,M):
	l=toLengths(s)
	n=len(l)
	C=[0]*n
	W=[0]*n
	# precompute partial sums badly!
	L=[sum(l[:i]) for i in range(n)]
	for j in range(1,n):
		starti=min(i for i in range(0,j) if (L[j]-L[i] < M))
		C[j]=1e6
		for i in range(starti,j):
			x=C[i-1]+(M-L[j]+L[i])**3
			if (x<C[j]):
				C[j]=x
				W[j]=i # means last line in optimal soln ending in word j starts at word i
	return W

def printNeat(s,W,j):
	if (j<1):
		return
	words=s.split(" ")
	l=toLengths(s)
	i=W[j]
	printNeat(s,W,i-1) # reverse the print out order!
	str=""
	for k in range(i,j+1): str+=words[k]+" "
	print(str)

# S="the angry horse jumped over the lazy dog"
# W=calcPrintNeat(S,10)
# printNeat(S,W,len(W)-1)
