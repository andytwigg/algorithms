import utils

# deterministic select

# in time T(n):
# divide the n elements into n/5 groups each of 5 elements - O(n)
# find the median of each group - O(n)
# x = recursively find the median of the n/5 medians - T(n/5)
# partition around x. let k = rank(x)
# if i=k then return x
# if i<k then return select(ith smallest in lower part) - <= T(7n/10)
# if i>k then return select((i-k)th smallest in upper part) - <= T(7n/10)

#for the recurrence, we have
# T(n) <= T(7n/10)+T(2n/10)+O(n)
# we can now check by substitution that T(n)<=cn since 7/10+2/10 < 1

# optimal binary search trees
# p(i) = pr(key ki) accessed
# p(i,j) = sum_{k=i}^j p(k)
# T(i,j) = min expected cost of a BST on keys ki..kj
# T(i,j) = min_{i<r<j} (p(i,r-1)+T(i,r-1)) + p(r+1,j)+T(r+1,j) + p(r))
#			min_{i<r<j} (T(i,r-1)+T(r+1,j)+p(i,j))
# (creating a tree with root k_r, left subtree i..r-1 right subtree r+1..j -> increases expected cost of each tree by (1*pr(accessing that tree))

# activity selection problem
# s_i, f_i = start, finish time of task i
# c[i,j]=size of maximum set of tasks that start after f_i and finish before s_j
# c[i,j]=max_{k where s_k > f_i and f_k < s_j} (c[i,k] + c[k,j] + 1)
# or 0 if there are no such k
# but greedy since we can always pick the task that finishes first at each step (and that starts after the last one selected has finished)
