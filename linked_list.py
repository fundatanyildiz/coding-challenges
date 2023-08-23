class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def print(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(current.data)
            current = current.next
        print(nodes)


first_node = Node(4)
second_node = Node(5)
ll = LinkedList(first_node)
ll.append(second_node)
ll.print()
