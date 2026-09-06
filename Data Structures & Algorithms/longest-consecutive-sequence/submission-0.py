class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestStreak = 0

        for num in nums:
            if num-1 not in numSet:
                currNum = num
                currStreak =1

                while currNum +1 in numSet:
                    currNum += 1
                    currStreak +=1

                longestStreak = max(longestStreak,currStreak)
        
        return longestStreak