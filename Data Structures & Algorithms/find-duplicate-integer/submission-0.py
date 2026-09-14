class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]# moves 1 step forward
            fast = nums[nums[fast]]#moves 2 step forward

            if slow==fast:# when they meet
                break

        slow = nums[0]#reset

        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow 