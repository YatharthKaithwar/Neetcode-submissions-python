class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def Backtrack(remaining: int, comb: list[int],start: int):
            if remaining == 0:
                result.append(list(comb))
                return
            
            elif remaining<0:
                return

            for i in range (start,len(nums)):
                comb.append(nums[i])

                Backtrack(remaining-nums[i],comb,i)

                comb.pop()
        Backtrack(target,[],0)
        return result