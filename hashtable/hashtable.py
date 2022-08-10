from linked_list.linked_list import LinkedList


class HashTable:
    def __init__(self, size=1024):
        """
        Takes one arguments:
        1. size: int
        returns: None
        """
        self.size = size
        self.buckets = [None] * size
        self.keys = []

    def __hash(self, key):
        hash_key = 0
        for i in key:
          hash_key = hash_key + ord(i)
        hash_key = hash_key * 283
        return hash_key % self.size

        # return sum([ord(i) for i in key]) * 283 % self.__size
    def hashing(self, key):
        hash_key = 0
        for i in key:
          hash_key = hash_key + ord(i)
        hash_key = hash_key * 283
        return hash_key % self.size


    def set(self, key, value):
        hashed_key = self.__hash(key)
        if self.buckets[hashed_key] == None:
            hash_list = LinkedList()
            self.buckets[hashed_key] = hash_list
        self.keys.append(key)
        self.buckets[hashed_key].Insert((key, value))

    def get(self, key):
        hashed_key = self.__hash(key)
        ll = self.buckets[hashed_key]
        if ll == None:
            return None
        current = ll.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        return None

    def contains(self, key):
        """
        This method will take a key
        returns : True if the key exists in the hashmap, and False if it doesn't exist
        """
        idx = self.__hash(key)
        bucket = self.buckets[idx]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.data[0] == key:
                    return True
                current = current.next
        return False

        # if self.get(key):
        #   return True
        # return False

    def key(self):
        """
        this method will return a collections of all the keys in hashmap as an object
        """
        return self.__keys


if __name__ == '__main__':
    # print("lolo")
    hasho = HashTable()
    hasho.set('lama', 26)
    hasho.set('amal', 100)
    hasho.set('amalsss', 100)
    print(hasho.get('lama'))
    print(hasho.get('amal'))

