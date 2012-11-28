import utils

# 15-12: signing players
# go over positions, not players (since <=1 player per position constraint)
# V[i,c]=max value of signing players in positions 1..i with budget <= c
#		= max_{players p in position i} V[i-1,c-c(p)]+v(p)  (take player p), V[i-1,c] (take noone in position i)


# 16-5: offline caching, FAR
# optimal substructure: consider 
# greedy choice: consider an optimal replacement strategy at time t. Then the element
# accessed farthest in the future will be the one evicted (cut-and-paste to see why)

def FAR(S):
	T={} # T[i] = list of requests for element i in increasing time order
	i=0
	for k in S:
		if (not T.has_key(k)):
			T[k]=[]
		T[k].append(-i) # use -time since we're going to use min heap
		i=i+1
	return T
