class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:

    def __init__(self):
        self.bucket = 10000
        self.storage = [None] * 10000
        self.head = None

    def hashFunct(self, key):
        return key % self.bucket

    def helperPrev(self, key):
        prev = self.head
        curr = self.head.next
        # till null and we find the key
        while curr is not None and curr.key != key:
            prev = curr
            curr = curr.next
        return prev
    
    def insert(self, key, value):
        idx = self.hashFunct(key)

        if self.storage[idx] is None:
            self.storage[idx] = Node(-1, -1) # Dummy Node 

        self.head = self.storage[idx]
        prev = self.helper(key)
        if prev.next is None:
            prev.next = Node(key, value) # fresh node
        else:
            prev.next.value = value # already existing node

    def get(self, key):
        idx = self.hashFunct(key)

        if self.storage[idx] is None:
            return -1
        
        self.head = self.storage[idx]
        prev = self.helper(key)
        if prev.next is None:
            return -1 # node doesn't exist
        else:
            #  existing node
            return prev.next.value


    def remove(self, key):
        idx = self.hashFunct(key)

        if self.storage[idx] is None:
            return

        self.head = self.storage[idx]
        prev = self.helper(key)
        if prev.next == None:
            return  # node doesn't exist
        else:
            temp = prev.next
            prev.next = prev.next.next
            temp.next = None
