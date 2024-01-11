class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size


    def hashfunction(self, key):
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, data):
        index = self.hashfunction(key)
        if not self.table[index]:
            self.table[index] = Node(key, data)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, data)

    def get(self, key):
        index = self.hashfunction(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None


hash_table = HashTable(5)

# Insert key-value pairs into the hash table
hash_table.insert("Alice", 25)
hash_table.insert("Bob", 30)
hash_table.insert("Charlie", 22)

# Retrieve values from the hash table
print("Alice's age:", hash_table.get("Alice"))      # Output: Alice's age: 25
print("Bob's age:", hash_table.get("Bob"))          # Output: Bob's age: 30
print("Charlie's age:", hash_table.get("Charlie"))