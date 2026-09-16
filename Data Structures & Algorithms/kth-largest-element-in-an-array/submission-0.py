class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap,num)#pushing elements

            if len(minHeap)>k:# if exceeds k
                heapq.heappop(minHeap)#pop the top smallest elem
        
        return minHeap[0]