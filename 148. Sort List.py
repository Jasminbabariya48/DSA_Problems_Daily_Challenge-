from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def findmid(self, head):
        slow = head
        fast = head.next
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def merge(self, left, right):
        if left == None:
            return right
            
        if right == None:
            return left
            
        ans = ListNode(-1)
        temp = ans
            
        while left != None and right != None:
            if left.val < right.val:
                temp.next = left
                temp = left
                left = left.next
            else:
                temp.next = right
                temp = right
                right = right.next
                
        while left != None:
            temp.next = left
            temp = left
            left = left.next
            
        while right != None:
            temp.next = right
            temp = right
            right = right.next
                
        ans = ans.next
        return ans


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        mid = self.findmid(head)
        
        left = head
        right = mid.next
        mid.next = None
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        result = self.merge(left, right)
        
        return result
    
if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    
    obj = Solution()
    ans = obj.sortList(head)
    
    while ans != None:
        print(ans.val, end = " ")
        ans = ans.next
        