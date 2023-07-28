'''
Valid Anagram.
If keys of the the HashMap is the same it will be a anagram. 
".get" is used if that key does not exist it will give the defalut value.

Alt method : use sorting for memeory optimization.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT    