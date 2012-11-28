import utils


# 15-6
# r(i)=weight of person i
# W(i)=max legal weight of all descendants of i
#	  = max(# take i, # don't take i)
#	  = max(r(i)+sum_{k:grandchildren of i} W(k), sum_{k:children of i} W(k))
# running time = O(n deg^2)

# 17-1 coin changing
# optimal substructure: consider an optimal solution S of value v
# Then taking out a coin c => S\c is an optimal solution of value v-c
# => S[v] = min_c S[v-c]+1
# example where greedy fails: $1, $0.9, $0.2, $0.01
# then making change for $1.1 needs 2 coins but greedy uses 11 coins

def change(c,x): # making change for amount x using coins c
	# rescale to ints
	y=min(c)
	c=map(lambda z:int(z/y),c)
	x=x/y
	maxc=max(c)
	x=int(x)
	print "rescaled target="+str(x)
	n=len(c)
	S=[0]*(x+1)
	T=[0]*(x+1)
	for i in range(1,x+1):
		S[i]=1e6
		for j in c:
			if (i>=j):
				v=S[i-j]+1
				if (v<S[i]):
					S[i]=v
					T[i]=j # an optimal soln of value i has >=1 coin of value j
		if (S[i]==1e6): S[i]=0 # hack
	return T

def coins(T,x):
	if (x<=0):
		return []
	else:
		return coins(T,x-T[x])+[T[x]]