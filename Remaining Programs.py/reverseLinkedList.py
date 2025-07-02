class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current:
        current.next, prev, current = prev, current, current.next
    return prev

def print_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original:")
print_list(head)

head = reverse(head)

print("Reversed:")
print_list(head)
