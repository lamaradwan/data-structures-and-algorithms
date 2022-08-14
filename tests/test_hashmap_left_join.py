from hashmap_left_join.hashmap_left_join import left_join
from hashtable.hashtable import HashTable


def test_same_word():
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

    actual = left_join(synonyms_ht, antonyms_ht)
    expected = [['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['outfit', 'grap', None], ['wrath', 'anger', 'delight']]
    assert actual == expected


def test_not_existed_word():
    synonyms_ht = HashTable()
    synonyms_ht.set('diligent', 'employed')
    synonyms_ht.set('fond', 'enamored')
    synonyms_ht.set('guide', 'usher')
    synonyms_ht.set('outfit', 'grap')
    synonyms_ht.set('wrath', 'anger')

    antonyms_ht = HashTable()
    antonyms_ht.set('nothing', 'idle')
    antonyms_ht.set('nothing1', 'averse')
    antonyms_ht.set('nothing2', 'follow')
    antonyms_ht.set('nothing4', 'jam')
    antonyms_ht.set('nothing3', 'delight')

    actual = left_join(synonyms_ht, antonyms_ht)
    expected = [['diligent', 'employed', None],
                ['fond', 'enamored', None],
                ['guide', 'usher', None],
                ['outfit', 'grap', None],
                ['wrath', 'anger', None]]
    assert actual == expected


def test_all_hashtable_intersection():
    synonyms_ht = HashTable()
    synonyms_ht.set('diligent', 'employed')
    synonyms_ht.set('fond', 'enamored')
    synonyms_ht.set('guide', 'usher')
    synonyms_ht.set('wrath', 'anger')

    antonyms_ht = HashTable()
    antonyms_ht.set('diligent', 'idle')
    antonyms_ht.set('fond', 'averse')
    antonyms_ht.set('guide', 'follow')
    antonyms_ht.set('wrath', 'delight')

    actual = left_join(synonyms_ht, antonyms_ht)
    expected = [['diligent', 'employed', 'idle'],
                ['fond', 'enamored', 'averse'],
                ['guide', 'usher', 'follow'],
                ['wrath', 'anger', 'delight']]
    assert actual == expected
