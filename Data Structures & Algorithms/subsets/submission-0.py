class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def recursion(i):

            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            recursion(i+1)

            subset.pop()
            recursion(i+1)

        recursion(0)
        return res