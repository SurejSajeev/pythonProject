class ListNode:
    def __init__(self, val, next_val=None):
        self.val = val
        self.next = next_val


class LinkedList:
    def __init__(self):
        self.head = None

    def add_elem(self, elem):
        new_elem = ListNode(elem)
        if not self.head:
            self.head = new_elem
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_elem

    def __str__(self):
        current = self.head
        while current.next:
            print(f"{current.val} -->")
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(5):
        ll.add_elem(i)
    print(ll)