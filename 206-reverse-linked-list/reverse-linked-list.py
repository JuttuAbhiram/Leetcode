# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        stack=[]
        temp=head
        while temp:
            stack.append(temp)
            temp=temp.next
        new_head=stack.pop()
        temp=new_head

        while stack:
            temp.next=stack.pop()
            temp=temp.next
        temp.next=None
        return new_head    