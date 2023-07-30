'''
Daily Tempratures
'''
class Solution:
    def dailyTempratures(self, tempratures : List[int]) -> List[int]:
        res = [0] * len(tempratures)
        stack = [] # pair : [temp, index]

        for i, t in enumerate(tempratures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res        

