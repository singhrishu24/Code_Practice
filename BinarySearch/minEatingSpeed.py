'''
Min Eating Speed of KOKO.
'''

class Solution:
    def minEatingSpeed(self, piles: List[n], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res                
    

    '''
    Optimized code for space : removed "res" variable running over (piles)array
    while l <= r:
        k = (l + r) // 2
        hours = 0

        for p in piles:
            hours += (p + k - 1) // k 
        if hours <= h:
            r = k - 1
        else:
            l = k + 1
    return l        
    '''