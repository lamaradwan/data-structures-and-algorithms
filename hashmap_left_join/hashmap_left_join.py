from hashtable.hashtable import HashTable


def left_join(ht1, ht2):
    ht1_keys = ht1.key()
    ht2_keys = ht2.key()
    result = []

    for i in range(len(ht1_keys)):
        if ht1_keys[i] == ht2_keys[i]:
            temp_arr = []
            temp_arr.append(ht1_keys[i])
            temp_arr.append(ht1.get(str(ht1_keys[i])))
            temp_arr.append(ht2.get(str(ht2_keys[i])))
            result.append(temp_arr)
        else:
            temp_arr = [ht1_keys[i], ht1.get(str(ht1_keys[i])), None]
            result.append(temp_arr)
    return result


if __name__ == '__main__':
    synonyms_ht = HashTable()
    synonyms_ht.set('diligent', 'employed')
    synonyms_ht.set('fond', 'enamored')
    synonyms_ht.set('guide', 'usher')
    synonyms_ht.set('outfit', 'grap')
    synonyms_ht.set('wrath', 'anger')

    antonyms_ht = HashTable()
    antonyms_ht.set('diligent', 'idle')
    antonyms_ht.set('fond', 'averse')
    antonyms_ht.set('guide', 'follow')
    antonyms_ht.set('flow', 'jam')
    antonyms_ht.set('wrath', 'delight')
    print(left_join(synonyms_ht, antonyms_ht))
    # output
    # [
    #     ["font", "enamored", "averse"],
    #     ["wrath", "anger", "delight"],
    #     ["diligent", "employed", "idle"],
    #     ["outfit", "garb", NULL],
    #     ["guide", "usher", "follow"]
    # ]
