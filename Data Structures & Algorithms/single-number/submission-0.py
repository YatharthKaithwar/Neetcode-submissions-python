class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for num in nums:
            unique = unique^num
        return unique