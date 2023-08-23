'''
Combination Sum : return a list of all unique combinations of candidates which sum to taregt 
'''
class Solution: 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:       
        res = []

        def dfs(i, cur, total):
            # Base Case
            if total == target:
                res.append(cur.copy())
                return 
            if i >= len(candidates) or total > target:
                return 

            # decision of adding the element
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # decision of NOT adding the element 
            # pointer moves if we do not add the element
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0) 
        return res      
        