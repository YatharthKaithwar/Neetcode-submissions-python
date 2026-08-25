class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        maxLength = 0
        left = 0

        for right,char in enumerate(s):
            if char in charMap and charMap[char]>=left:
                left = charMap[char]+1
            
            charMap[char] = right

            maxLength = max(maxLength,right-left+1)

        return maxLength