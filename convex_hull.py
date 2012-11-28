import utils


def convex_hull(P):
    U=[]
    L=[]
    P.sort()
    for p in P:
        while len(U)>1 and ccw_turn(U[-2],U[-1],p): U.pop()
        U.append(p)

        while len(L)>1 and (not ccw_turn(L[-2],L[-1],p)): L.pop()
        L.append(p)

    return U,L

def graham_scan(P):
    # take entry with min y value, breaking ties on x
    p0=min(P, key=lambda (x,y):(y,x))
    P.remove(p0)
    # sort the remaining entries by polar angle with p0
    sort_polar(P,p0)
    S=[P[0],P[1],P[2]]
    for p in P[3:]:
        # while not ccw(next-to-top(S, top(S), p))
        while (not ccw_turn(S[-2],S[-1],p)): S.pop()
        S.append(p)
    return S
            
def polar_cmp(x1,y1,x2,y2):
    # (x2,y2) >= (x1,y1) iff (x1,y1) is clockwise from (x2,y2)
    return (x1*y2 - x2*y1)

def ccw_turn(x1,y1,x2,y2,x3,y3):
    # ccw turn iff (p3-p1) is ccw from (p2-p1)
    return (polar_cmp(x3-x1,y3-y1,x2-x1,y2-y1) <= 0)

def sort_polar(P,p=(0,0)):
    # sort by increasing polar angle with origin point p
    P.sort(lambda (x1,y1),(x2,y2):polar_cmp(x1-p[0],y1-p[1],x2-p[0],y2-p[1]))

def point_dist(a,b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2

def rotatingCalipers(P):
    H = convex_hull(P)
    n=len(H)
    # start with an antipodal pair
    i=H.index(min(H))
    j=H.index(max(H))
    while (i<n or j>0):
        yield H[i],H[j]

        # test angles, and move the largest one
        # if (H[j]-H[j-1]) is clockwise from (H[i+1]-H[i])
        if (polar_cmp(H[j][0]-H[j-1][0],H[j][1]-H[j-1][1],H[i+1][0]-H[i][0],H[i+1][1]-H[i][1])>0):
            i=i+1
        else:
            j=j-1

def diameter(P):
    points = rotatingCalipers(P)
    diam,pair = max((point_dist(p,q),(p,q)) for p,q in points)
    return pair
	