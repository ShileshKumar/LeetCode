"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        d={}
        a=head
        while a:
            d[a]=Node(a.val)
            a=a.next
        a=head
        while a:
            try:
                d[a].next=d[a.next]
            except:
                d[a].next=None
            try:
                d[a].random=d[a.random]
            except:
                d[a].random=None
            a=a.next
        return d[head]