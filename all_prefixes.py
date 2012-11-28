import utils
	
# all combinations of prefixes of strings in a list
# len(prefix(L)) = \prod_i (1+len(L[i]))
# eg len(prep.prefix([['h','m','s'],['a','b','c','d'],['x','y','z'],['m','f']]))=240
def prefix(L):
	if (len(L)==0):
		return [[]]
	s=L[0]
	T = prefix(L[1:]) # tail(L)
	return [s[:i]+j for i in range(0,len(s)+1) for j in T]

