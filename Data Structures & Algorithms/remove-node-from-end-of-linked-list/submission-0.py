# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
    
        fast = dummy
        slow = dummy
    
    # 2. Advance the fast pointer n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
    # 3. Move both pointers together until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next
        
    # 4. Relink the slow pointer's next to skip the target node
        slow.next = slow.next.next
    
    # 5. Return the true head of the modified list
        return dummy.next
        