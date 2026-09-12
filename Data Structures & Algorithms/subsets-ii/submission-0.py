class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start , subset):
            res.append(subset.copy())

            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:#skip the duplicate
                    continue
                
                subset.append(nums[i])#do
                backtrack(i+1,subset)#search
                subset.pop()#undo
        backtrack(0,[])
        return res