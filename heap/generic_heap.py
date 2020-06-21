class Heap:
    # Initialize heap with empty storage and priority function
    # Defaults to a max heap function
    def __init__(self, priority=lambda x, y: x > y):
        self.storage = []
        self._priority = priority

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        pass

    def get_priority(self):
        # Return the top-most element if it exists, else return None
        return self.storage[0] if len(self.storage) else None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        # Loop until the element reaches the top or break out
        # when the element's parent has higher priority
        while index > 0:
            # Calculate the parent's index
            parent = (index - 1) // 2
            # If the element at index has higher priority than the parent element
            if self._priority(self.storage[index], self.storage[parent]):
                # swap the element and its parent
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # and update the index
                index = parent
            else:
                # The parent has higher priority, so we're done
                break

    def _sift_down(self, index):
        pass


if __name__ == '__main__':
    heap = Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(9)
    heap.insert(8)
    heap.insert(7)
    heap.insert(4)
    heap.insert(6)
    heap.insert(5)
    print(heap.storage)
