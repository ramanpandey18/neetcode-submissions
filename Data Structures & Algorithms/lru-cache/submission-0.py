class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # OrderedDict combines a hash map and a doubly linked list automatically
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move the accessed key to the end to mark it as Most Recently Used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value
            self.cache[key] = value
            # Move it to the end since it was updated
            self.cache.move_to_end(key)
        else:
            # Insert the new key-value pair
            self.cache[key] = value
            
        # If we exceeded the capacity, pop the first item (Least Recently Used)
        if len(self.cache) > self.cap:
            # last=False pops from the left side (FIFO/LRU position)
            self.cache.popitem(last=False)
        
        
