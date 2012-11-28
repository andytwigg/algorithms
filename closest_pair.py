import utils

def point_dist(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2

def closest_pair_brute(P):
    d,p,q = min((point_dist(p,q),p,q) for p in P for q in P if q!=p)
    return p,q

def closest_pair_(P,X,Y):
    # P is a set of points
    # X is P sorted by x-value, Y is X sorted by y-value
    n=len(P)
    if (n<=3):
        return closest_pair_brute(P)

    # find a vertical line l that bisects P into two sets P_L,P_R
    # X is already sorted by x-value, so can extract median directly
    l=X[n/2][0]
    P_l = [p for p in P if p[0]<=l]
    P_r = [p for p in P if p[0]>l]
    
    # divide X into X_l=P_l, X_r=P_r, sorted by x-value
    X_l = X.filter(lambda p:p[0]<=l)
    X_r = X.filter(lambda p:p[0]>l)
    
    # divide Y into Y_l=P_l, Y_r=P_r, sorted by y-value
    Y_l = Y.filter(lambda p:p[0]<=l)
    Y_r = Y.filter(lambda p:p[0]>l)
    
    # recurse
    pl,ql = closest_pair_(P_l,X_l,Y_l)
    pr,qr = closest_pair_(P_r,X_r,Y_r)
    d_l = point_dist(pl,ql)
    d_r = point_dist(pr,qr)
    d = min(d_l,d_r)
    
    # closest pair is either (pl,ql) or (pr,pq) or 
    # one crossing the cut: p in P_l, q in P_r with d(p,q) < d
    # NB for any p,q both in P_l, we have d(p,q)>=d (and for P_r) (by the recursive step)
    # -> at most 4 points to check against in a dxd square in each side
    
    # step 1: filter out any points from Y not in the 2d-wide strip around l
    Y_strip = Y.filter(lambda p:l-d < p[0] < l+d)
    
    # step 2: for each p in strip, test d(p,q) for the 7 points following p in the strip
    d_strip,p_strip,q_strip = 2*d, None, None
    for i in xrange(len(Y_strip)):
        p = Y_strip[i]
        upper=min(i+8,len(Y_strip))
        d_strip,p,q = min((point_dist(p,q),p,q) for q in Y_strip[i:upper])
        if (d_strip<d):
            p_strip,q_strip = p,q
    if (d_strip<d):
        return d_strip,p_strip,q_strip
    elif (d_l < d_r):
        return d_l,pl,ql
    else:
        return d_r,pr,qr
    
def closest_pair(P):
    # create the sorted X,Y to start the process
    X = sorted(P,key=lambda p:p[0])
    Y = sorted(P,key=lambda p:p[1])
    return closest_pair_(P,X,Y)
