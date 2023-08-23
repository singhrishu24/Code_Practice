'''
Combination Sum 2
Link : https://leetcode.com/problems/combination-sum-ii/
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        # define function and Base Case
        def backtrack(cur, startPos, target):
            # we are reducing the target value as we get matches
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return
            
            prev = -1 
        # decision of Adding the element
            for i in range(startPos, len(candidates)):
                # when we skip the value we skip the duplicate
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
        # initialize backtracking and return 
        backtrack([], 0, target)
        return res