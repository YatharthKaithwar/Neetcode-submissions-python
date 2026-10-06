class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        prev2 = 0
        prev1 = 0

        for amount in nums:
            curr = max(prev1,prev2 + amount)
            prev2 = prev1
            prev1 = curr
        return curr 