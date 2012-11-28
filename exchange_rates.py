import utils

# ex 15.3-6
# exchange rates r_ij i,j=1..n
# C(i,j) = rate of exchanging i->j
#		 = max (r_ij, max_{i<k<j} C(i,k) * C(k,j))

def exchange(r):
	n=len(r)
	C=matrix(n,n)
	for i in range(0,n):
		for j in range(i+1,n):
			C[i][j] = max(r[i][j], max(C[i][k]*C[k][j] for k in range(i,j)))
	return C[0][n-1]
    
def greedy_task_selection(s,f,k,n):
	m=k+1
	while (m<=n and s[m]<f[k]): # find the first compatible task
		assert (f[m]>=f[m-1]) # assume tasks are sorted by increasing finish time
		m=m+1
	if (m>n): return []
	else: return [m] + greedy_task_selection(s,f,m,n)
	

# as before but with a value v_i for completing task t_i, and objective to maximize total value
# c[i,j]=max_{k st s_k>f_i f_k<s_j} (c[i,k]+c[k,j]+v_k)



# 0-1 knapsack
# w_i,v_i = weight, value of item i
# C[i,w] = max value of items 1..i with weight <= w
# C[i,w] = max (C[i-1,w-w_i] + v_i, C[i-1,w])
# => time O(nW), space O(nW)

# 16.2-3: smallest weight has largest value
# => w_i/v_i > w_j/v_i for i<j
# greedy-choice: consider optimal solution for items of weight >=w, then this has smallest item of weight >=w




# 16.2-5: set x_1..x_n of points (in R)
# find smallest set of unit length intervals containing all points
# easy to see that no intervals should overlap, should start at x_1
# greedy-choice: consider optimal solution for points > i.
# then it contains an interval starting at i
# => start at x_1, cover by an interval, go to next point

def greedy_intervals(x):
	n=len(x)
	I=[(x[0],x[0]+1.0)]
	r=x[0]+1.0
	for i in range(0,n):
		if (r<x[i]):
			I.append((x[i],x[i]+1.0))
			r=x[i]+1.0
	return I

