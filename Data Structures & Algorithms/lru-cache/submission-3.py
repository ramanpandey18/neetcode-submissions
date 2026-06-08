# class Node:
#     def __init__(self, key: int, val: int):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         # OrderedDict combines a hash map and a doubly linked list automatically
#         self.cache = OrderedDict()

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
        
#         # Move the accessed key to the end to mark it as Most Recently Used
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             # Update the value
#             self.cache[key] = value
#             # Move it to the end since it was updated
#             self.cache.move_to_end(key)
#         else:
#             # Insert the new key-value pair
#             self.cache[key] = value
            
#         # If we exceeded the capacity, pop the first item (Least Recently Used)
#         if len(self.cache) > self.cap:
#             # last=False pops from the left side (FIFO/LRU position)
#             self.cache.popitem(last=False)

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Maps key -> Node
        
        # Initialize dummy boundary nodes to prevent edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper function: Isolate and remove a node from its current neighbors
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper function: Place a node at the most recently used end (right before tail)
    def _insert(self, node: Node):
        mru_node = self.tail.prev
        
        mru_node.next = node
        node.prev = mru_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Refresh its recency position
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key already exists, get rid of its old node positioning
        if key in self.cache:
            self._remove(self.cache[key])
            
        # Add the fresh node into our structures
        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert(new_node)
        
        # If we went over capacity, evict the least recently used node (right after head)
        if len(self.cache) > self.cap:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
