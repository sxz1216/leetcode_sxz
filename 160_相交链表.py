class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        pA = headA
        pB = headB
        while pA:
            pA = pA.next
            lenA += 1
        while pB:
            pB = pB.next
            lenB += 1
        pA = headA
        pB = headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                pA = pA.next
        else:
            for i in range(lenB-lenA):
                pB = pB.next
        while pA!=pB:
            pA = pA.next
            pB = pB.next
        return pA