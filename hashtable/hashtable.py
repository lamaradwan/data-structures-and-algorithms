from linked_list.linked_list import LinkedList


class HashTable:
    def __init__(self, size=10):
        """
        Takes one arguments:
        1. size: int
        returns: None
        """
        self.__size = size
        self.__buckets = [None] * size
        self.__keys = []

    def __hash(self, key):
        hash_key = 0
        for i in key:
          hash_key = hash_key + ord(i)
        hash_key = hash_key * 283
        return hash_key % self.__size

        # return sum([ord(i) for i in key]) * 283 % self.__size
    def hashing(self, key):
        hash_key = 0
        for i in key:
          hash_key = hash_key + ord(i)
        hash_key = hash_key * 283
        return hash_key % self.__size


    def set(self, key, value):
        hashed_key = self.__hash(key)
        if self.__buckets[hashed_key] == None:
            hash_list = LinkedList()
            self.__buckets[hashed_key] = hash_list
        self.__keys.append(key)
        self.__buckets[hashed_key].Insert((key, value))

    def get(self, key):
        hashed_key = self.__hash(key)
        ll = self.__buckets[hashed_key]
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
        bucket = self.__buckets[idx]
        if bucket is not None:
            current = bucket.head
            while current:
                if current.value[0] == key:
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
    print(hasho.get('lama'))
    print(hasho.get('amal'))

