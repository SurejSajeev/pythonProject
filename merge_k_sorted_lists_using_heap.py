import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define a custom wrapper class for ListNode to enable comparisons
class ListNodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

def mergeKSortedLists(lists):
    min_heap = []  # Min-heap to store nodes

    # Push the head of each linked list into the min-heap
    for lst in lists:
        if lst:
            heapq.heappush(min_heap, ListNodeWrapper(lst))

    dummy = ListNode()
    current = dummy

    while min_heap:
        node = heapq.heappop(min_heap).node
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, ListNodeWrapper(node.next))

    return dummy.next

# Example usage:
# Create sample linked lists
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

# Merge the linked lists
merged_list = mergeKSortedLists([list1, list2, list3])

# Print the merged result
result = []
while merged_list:
    result.append(merged_list.val)
    merged_list = merged_list.next

print(result)
