from hashtable.hashtable import HashTable


def repeated_word(string):
    hasho = HashTable()
    lower = string.lower()
    string2 = lower.replace(',', '')
    split_text = string2.split(' ')
    hasho.set(split_text[0], 1)
    for i in range(1, len(split_text)):
        if hasho.contains(split_text[i]) is True:
            hashed_key = hasho.hashing(split_text[i])
            ll = hasho.buckets[hashed_key]
            if ll is None:
                return None
            current = ll.head
            while current:
                if current.data[0] == split_text[i]:
                    return current.data[0]
                current = current.next
        else:
            hasho.set(split_text[i], 1)


if __name__ == "__main__":
    # text = 'lama is hiring is is'
    # print(text.split(' '))
    print(repeated_word(
        'Once upon a time, there was brave princess who...'))
