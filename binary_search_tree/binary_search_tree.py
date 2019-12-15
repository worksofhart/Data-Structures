# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current_node = self
        finished = False
        while not finished:
            if current_node.value == value:
                return
            elif current_node.value < value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BinarySearchTree(value)
                    finished = True
            elif current_node.value > value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BinarySearchTree(value)
                    finished = True

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        current_node = self
        finished = False
        while not finished:
            if current_node.value == target:
                return True
            elif current_node.value < target:
                if current_node.right:
                    current_node = current_node.right
                else:
                    finished = True
            elif current_node.value > target:
                if current_node.left:
                    current_node = current_node.left
                else:
                    finished = True
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
