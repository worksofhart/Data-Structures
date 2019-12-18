from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.nodes = 0
        self.cache = {}  # Dictionary representing every key currently in cache, used as a quick lookup table to avoid linked list traversal
        # Linked list storing every node currently in cache, in order from most recent at head to least at tail
        self.storage = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.cache:
            return None
        else:
            # Move to head since it's now most recently used
            node = self.cache[key]
            self.storage.move_to_front(node)
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # If key found, update node's value and move it to the front of the list since it's now the most recently used
        if key in self.cache:
            node = self.cache[key]
            node.value = (key, value)
            self.storage.move_to_front(node)
            return
        # If we've reached max capacity, evict least recently used node
        if self.limit == self.nodes:
            tail = self.storage.tail
            del self.cache[tail.value[0]]
            self.storage.remove_from_tail()
            self.nodes -= 1
        # Add key, value pair to our DLL
        self.storage.add_to_head((key, value))
        self.cache[key] = self.storage.head
        self.nodes += 1
