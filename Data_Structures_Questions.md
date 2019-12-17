Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`? O(1). Always adding to the tail of the DLL that underlies the queue, which is an O(1) operation.

2. What is the runtime complexity of `dequeue`? O(1). Always removing from the head of the underlying DLL.

3. What is the runtime complexity of `len`? O(1). Len is incremented with every `enqueue` and decremented with every `dequeue` operation so no traversal needs to happen.

## Binary Search Tree

1. What is the runtime complexity of `insert`? Best case, O(1) on inserting the first node, worst case O(n) in an unbalanced tree where all nodes must be traversed to get to the insertion point, average case O(log n), because the height of a tree tends to grow at log n.

2. What is the runtime complexity of `contains`? Best case, O(1) if matching node is the head, worst case O(n) in an unbalanced tree where all nodes must be traversed to determine to find matching node, average case O(log n), because the height of a tree tends to grow at log n.

3. What is the runtime complexity of `get_max`? Best case, O(1) in a tree of 1 element or if max is maintained by every insert / delete operation, worst case O(n) in an unbalanced tree where every element is greater than the previous one, and average O(log n). Right-most node will need to be traversed starting from the top of the tree until no more right nodes are found, in general halving the search space for each level of the tree traversed, so log n.

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`? O(1)

2. What is the runtime complexity of `ListNode.insert_before`? O(1)

3. What is the runtime complexity of `ListNode.delete`? O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`? O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`? O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`? O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`? O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`? O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`? O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`? O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Worst case for `Array.splice` is O(n). `DoublyLinkedList.delete` will always be O(1) when a node reference is already available to it. If traversal must happen prior to delete to find the node, then worst case will be O(n).
