class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxwtr = 0

        while left < right:
            width = right - left
            
            currHeight = min(heights[left],heights[right])
            currwtr = width*currHeight
            maxwtr = max(maxwtr,currwtr)

            if heights[left]<heights[right]:
                left +=1
            else:
                right-=1
        return maxwtr


