class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        juhi=head
        while juhi:
            while juhi.next and juhi.val==juhi.next.val:
                juhi.next=juhi.next.next
            juhi=juhi.next
        return head
