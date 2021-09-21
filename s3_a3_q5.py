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

    def delete_data(self, data):

        temp = self.head
        prev = temp
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None
        prev = None


def delete_vowels(linked_list):
    curr = linked_list.head
    while curr is not None:
        if curr.data in 'aeiouAEIOU':
            linked_list.delete_data(curr.data)
            curr = linked_list.head
        else:
            curr = curr.next


inp = input()
llist = LinkedList()
for i in inp:
    llist.push(i)

print("Before deletion")
llist.print_list()
delete_vowels(llist)
print("After Deletion")
llist.print_list()
