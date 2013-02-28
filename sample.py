import random 
from numpy.random import binomial
import numpy as np
import pandas as pd
from collections import defaultdict
from itertools import izip

'''
Some stream sampling and approximate join sampling algorithms

Created on 7 Feb 2013

@author: Andy Twigg <andy.twigg@gmail.com>
'''

# stream sampling with replacement
# S = stream to sample from
# k = sample sizei
# n = len(S). If none then a pass is made to determine n
# the output is not random; you may want to post-shuffle
# memory O(1)
def sample_with_replacement(S,k,n=None):
	if n is None:
		n=len(S)

	def gen_fixed_weights(S,w):
		for s in S:
			yield (s,w)

	return sample_with_replacement_weighted(gen_fixed_weights(S,1),k,n)

# weighted stream sampling with replacement
# S = stream of (element,weight) to sample from
# k = sample size
# W = sum of weights in S. If none then a pass is made to determine w
# the output is not random; you may want to post-shuffle
# memory O(1)
def sample_with_replacement_weighted(S,k,W=None):
	D=0
	if W is None:
		W=sum(w for (_,w) in S)
	for (s,w) in S:
		if k<=0: return
		x = binomial(k,float(w)/(W-D))
		for _ in xrange(x):
			yield s
		k-=x
		D+=w

# sample each element of S wp p
# memory O(1)
def sample_coin_flips(S,p):
	for s in S:
		if (random.random() <= p):
			yield s

# fisher-yates shuffle
# shuffle inplace
def shuffle(S):
	for i in xrange(len(S)):
		swap(S,i,random.randint(0,i+1))

# reservoir sampling
# a uniform sample from S of length k
# memory O(k)
def sample_reservoir_without_replacement(S,k):
	n = len(S)
	R = S[:k]
	for i in xrange(k,n):
		j=random.randint(0,i)
		if (j < k): # wp k/i
			R[j]=S[i]
	return R

# convenience methods
def pick_one(S):
	return S[random.randint(0,len(S))]

def pick_one_stream(S):
	return sample_reservoir_without_replacement(S,1)[0]

# sample from a stream S without replacement
# memory O(1)
def sample_without_replacement(S,k,n=None):
	if n is None:
		n=len(S)

	n_sampled = 0
	for (i,s) in enumerate(S):
		# pick wp (k-n_sampled)/(n-i)
		if (random.random() <= float(k-n_sampled)/n):
			yield s
			n_sampled += 1

# See On random sampling over joins, Chaudhuri et al.
# approximately sample from the join of data1,data2
# R1,R2: DataFrame
# return: DataFrame containing an approximate sample of the join
# A = join column	

# naive sampling - when no column statistics are known
def join_naive_sample(R1,R2,A,k):
	J = pd.merge(R1,R2,on=A)
	return sample_reservoir_without_replacement(J.values,k)

# stream-sample: requires 2 passes over R1, and index+statistics for R2
# each output tuple requires a sample from 
# the tuples of R2 where attribute A matches some value 
def join_stream_sample(R1,R2,A,k):

	stats=compute_column_stats(R2,A)

	def weighted_stream(S,V,stats):
		for (s,v) in izip(S,V):
			yield (s,stats[v])


	# WR weighted sample from R1 of size k
	W=sum([stats[v] for v in R1[A].values]) # 1 pass over R1
	S1=sample_with_replacement_weighted(weighted_stream(R1.values,R1[A].values,stats),k,W) # 1 pass over R1

#	R2=R2.set_index([A])
	# index of A in tuples
	A_ix1 = find(R1.columns.values,A)
	A_ix2 = find(R2.columns.values,A)

	for t1 in S1:
		v=t1[A_ix1]
		# sample random tuple t2 from all tuples t in R2 with t[A]=v
		S2=R2[R2[A]==v].values
		t2=pick_one_stream(S2)
		# output t1 x t2
		yield np.append(t1,np.delete(t2,A_ix2))

	
# compute column stats for relation R on attribute A
# return: stats where stats[v]=#tuples in R where R[A]==v
def compute_column_stats(R,A):
	stats=defaultdict(int)
	for t in R[A].values:
		stats[t]+=1
	return stats

def swap(S,i,j):
	tmp = S[i]
	S[i] = S[j]
	S[j] = tmp

def find(X,a):
	for (i,x) in enumerate(X):
		if x==a: return i
	return None

def test():
	left = pd.DataFrame({'A': [1,2,2,2,2,2,2,2,2,2,2], 'B': [0,1,2,3,4,5,6,7,8,9,10]})
	right = pd.DataFrame({'A': [2,1,1,1,1,1,1,1,1,1,1], 'C': [0,1,2,3,4,5,6,7,8,9,10]})
	return list(join_stream_sample(left,right,'A',5))



