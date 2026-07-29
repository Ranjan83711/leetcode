# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst=[]
        temp=head
        while temp:
            lst.append(temp.val)
            temp=temp.next
        # return lst
        if lst==lst[::-1]:
            return True
        else:return False

        