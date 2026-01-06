class Solution:
    def getIntersectionNode( headA, headB):
        first_LL_set = set()
        current = headA

        while current != None:
            first_LL_set.add(current)
            current = current.next

        current = headB
        while current != None:
            if current in first_LL_set:
                return current
            current = current.next
        
        return None