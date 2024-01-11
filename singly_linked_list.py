class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


if __name__ == '__main__':
    # Creating a singly linked list
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)

    # Printing the elements in the singly linked list
    current = singly_linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
