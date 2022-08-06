from hashtable.hashtable import HashTable


# Verify Setting a key/value to your hashtable results in the value being in the data structure
# Verify Retrieving based on a key returns the value stored
def test_set_key_value():
    hash1 = HashTable()
    hash1.set('lama', 'python Developer')
    actual = hash1.get('lama')
    expected = 'python Developer'
    assert actual == expected


# Successfully returns None for a key that does not exist in the hashtable
def test_get_none_value():
    hash1 = HashTable()
    actual = hash1.get('l')
    expected = None
    assert actual == expected


# Successfully returns a list of all unique keys that exist in the hashtable
def test_return_list_of_keys():
    hash1 = HashTable()
    hash1.set('lama', 'python Developer')
    hash1.set('faris', 'DevOps')
    hash1.set('zaid', 'Industrial Engineer')
    assert hash1.key() == ['lama', 'faris', 'zaid']


# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_handling_collision():
    hash1 = HashTable()
    hash1.set('lama', 35)
    hash1.set('amal', 55)
    assert hash1.get('amal') == 55
    assert hash1.get('lama') == 35


# Successfully hash a key to an in-range value
def test_hash_a_key():
    hash1 = HashTable()
    assert hash1.hashing('lama') == 3
