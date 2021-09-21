class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = new_node

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next


inp = input()
llist = LinkedList()
for i in inp:
    llist.append(int(i))
llist.print_list()
