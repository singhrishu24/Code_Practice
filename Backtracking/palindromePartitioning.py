'''
Palindrome Partitioning
'''
class Solution:
    def partition(self, s : str) -> List[List[str]]:
        res, partition = [], []

        # define dfs recursive backtracking
        def dfs(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    partition.append(s[i : j+1])
                    dfs(j+1)
                    partition.pop()
        # dfs call
        dfs(0)
        return res

        # Plaindrome function
        def isPalin(self, s, l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True
