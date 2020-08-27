'''
1. Sort our intervals by starts, but also we need to keep they original numbers, so I sort triplets: [start, end, index].
2. Create array of starts, which I call begs.
3. Creaty out result, which filled with -1.
4. Iterate over ints and for every end j, use bisect_left.
   Check that found index t < len(begs) and if it is, update out[k] = ints[t][2].
   Why we update in this way, because our intervals in sorter list have different order, so we need to obtain original index.

'''

ints = sorted([[j,k,i] for i,[j,k] in enumerate(intervals)])
        begs = [i for i,_,_ in ints]
        out = [-1]*len(begs)
        for i,j,k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        
        return out