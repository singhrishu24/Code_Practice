'''
Group the Anagrams together in a array.
Step 1 : Mapping charCOunt to list of Anagrams.
Step 2 : Mapping the character to value. Using ASCII Value.
Step 3 : Append the string s for a particular count.
'''
class Solution:
    def groupAnagrams(self, strs: List[strs]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()        