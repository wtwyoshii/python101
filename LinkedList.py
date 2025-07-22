class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    def delete(self, data):
        current_node = self.head


        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next



my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.display()