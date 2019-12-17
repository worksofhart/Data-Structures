from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.length > 0:
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.storage.length
