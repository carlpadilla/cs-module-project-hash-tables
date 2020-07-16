class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Load Factor = Total number of items stored / Size of the array
        # Your code here
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # utf_key = ord(key)
        # h = 5381
        # for c in utf_key:
        #     h = ((h*33) + c) % self.capacity
        # return h
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Figure out what the index of the key is:
        idx = self.hash_index(key)

        # set node to hash at computed index
        node = self.storage[idx]
        self.size += 1
        # Check to see if the node is empty:
        if node is None:
            # Create the node
            self.storage[idx] = HashTableEntry(key, value)
            # check the load factor of the table. If above 0.7, double the size of the table.
            if self.get_load_factor() >= 0.7:
                self.resize(self.capacity * 2)
            return

        prev = node
        while node is not None:
            if key == node.key:
                node.value = value
                return
            else:
                prev = node
                node = node.next
        prev.next = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Find the index
        idx = self.hash_index(key)
        node = self.storage[idx]
        prev = None
        # Iterate to the requested node
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            # Key not found
            return None
        else:
            # The key was found.
            self.size -= 1
            result = node.value
            # Delete this element in linked list
            if prev is None:
                self.storage[idx] = node.next
            else:
                prev.next = prev.next.next
            # return the deleted item
            return result

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Calculate the hash
        idx = self.hash_index(key)
        # Start at the first node in the hash table
        node = self.storage[idx]
        # Run through all of the nodes in the list at this index.
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # Store a reference to the current hash table
        current_table = self.storage

        # Store the current capacity
        current_capacity = self.capacity

        # Update the capacity to new_capacity
        self.capacity = new_capacity

        # Create a new list of size new_capacity
        self.storage = [None] * new_capacity

        for node in current_table:
            while node is not None:
                self.put(node.key, node.value)
                node = node.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
