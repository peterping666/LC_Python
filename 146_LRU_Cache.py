class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        target = self.dict[key]
        self.remove(target)
        self.add(target)
        return target.value

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            newNode = Node(key, value)
            self.add(newNode)
        else:
            target = self.dict[key]
            target.value = value
            self.remove(target)
            self.add(target)

    def add(self, node: Node) -> None:
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.dict[node.key] = node
        if len(self.dict) > self.capacity:
            self.remove(self.head.next)

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.dict[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)