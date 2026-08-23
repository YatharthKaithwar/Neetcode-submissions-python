class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid]==target:
                return mid

            if nums[l]<=nums[mid]:#checking if left half is sorted?

                if nums[l]<=target<nums[mid]:##if no. in left half
                    r=mid-1
                else:# else no. right half
                    l=mid+1
            else:#else right half is sorted

                if nums[mid]<target<=nums[r]:#if target in right half
                    l=mid+1
                else:#else in left half
                    r=mid-1
        return -1