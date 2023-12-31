#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lNode = head
        node = head
        pNode = None

        nCount = 0
        while True:
            nCount += 1
            if nCount > n:
                pNode = node
                node = node.next
            if not lNode.next:
                break
            lNode = lNode.next

        if pNode is None: # mean we have remove the first node
            if nCount == 1:
                return ListNode('')
            head = node.next
        else:
            pNode.next = node.next
        return head




if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)

    s = Solution()
    l = s.removeNthFromEnd(l, 1)
    print('---------------------')
    print(l.val)
    print(l.next.val)
    print(l.next.next.val)
    print(l.next.next.next.val)
    # print(l.next.next.next.next.val)

