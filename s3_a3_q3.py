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


def find_min_max(head):
    curr = head
    min = 9999999999999
    max = -9999999999999
    while curr is not None:
        min = curr.data < min and curr.data or min
        max = curr.data > max and curr.data or max
        curr = curr.next
    print("Max element is", max)
    print('Minimum element is', min)


def count(head):
    curr = head
    c = 0
    while curr is not None:
        c += 1
        curr = curr.next
    print("Number of nodes is", c)


llist = LinkedList()
data = int(input())
llist.push(data)
inp = int(input("Enter 1 to continue or any other to quit "))
while inp == 1:
    data = int(input())
    llist.append(data)
    inp = int(input("Enter 1 to continue or any other to quit "))

llist.print_list()
find_min_max(llist.head)
count(llist.head)
