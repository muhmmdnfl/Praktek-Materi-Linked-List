class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position!")
            return
        elif position == 0:
            self.insert_at_beginning(data)
        else:
            new_node = Node(data)
            curr = self.head
            count = 0
            while count < position - 1 and curr.next != self.head:
                curr = curr.next
                count += 1
            if count == position - 1:
                new_node.next = curr.next
                curr.next = new_node
            else:
                print("Position out of range!")

    def delete(self, data):
        if self.is_empty():
            print("Linked List Kosong!")
            return

        curr = self.head
        prev = None

        # Jika data ada di head
        if curr.data == data:
            if curr.next == self.head:
                self.head = None
            else:
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            return

        curr = self.head
        while curr.next != self.head:
            prev = curr
            curr = curr.next
            if curr.data == data:
                prev.next = curr.next
                return

        print("Simpul tidak ditemukan!")

    def display(self):
        if self.is_empty():
            print("Linked List Kosong!")
            return
        curr = self.head
        while True:
            print(curr.data, end=" ")
            curr = curr.next
            if curr == self.head:
                break
        print()

    def search(self, data):
        if self.head is None:
            print("Linked List Kosong!")
            return False
        curr = self.head
        while True:
            if curr.data == data:
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False


# Testing Circular Linked List
cll = CircularLinkedList()

cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_end(30)
cll.insert_at_end(40)

print("Data dalam Circular Linked List setelah proses insert:", end=" ")
cll.display()

print()
print(f'Simpul 30 ada dalam list?: {cll.search(30)}')
print(f'Simpul 100 ada dalam list?: {cll.search(100)}')

print("\nDelete simpul 30 dan simpul 20:")
cll.delete(30)
cll.delete(20)

print("Data dalam Circular Linked List setelah di delete:", end=" ")
cll.display()

print('\nInput simpul dengan nilai 50 di posisi indeks ke-1:')
cll.insert_at_position(50, 1)

print("Data terbaru dalam Circular Linked List:", end=" ")
cll.display()
