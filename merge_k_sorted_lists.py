class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKSortedLists(lists):
    if not lists:
        return None

    def mergeTwoLists(l1, l2):
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            print(current.val)

        current.next = l1 or l2
        return dummy.next

    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged.append(mergeTwoLists(lists[i], lists[i + 1]))
            else:
                merged.append(lists[i])
        lists = merged

    return lists[0]


if __name__ == '__main__':
    # Example usage:
    # Create sample linked lists
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    # Merge the linked lists
    merged_list = mergeKSortedLists([list1, list2, list3])

    # Print the merged result
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
