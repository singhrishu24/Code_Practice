'''
Largest area of rectangle in Histogram.
'''

class Solution:
    def largestRecatngleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))


        # For the elements left in the stack after popping.
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea            