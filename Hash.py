class HashMap:
    def __init__(self):
        self.size = 6  # Size of the array
        self.map = [None] * self.size  # array where the data will be stored
        # 'None' to force python to construct a list to have a fixed length

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size  # return index of the key

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:  # if it contains empty we can add to the map
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:  # if cell is not none then we iterate
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            self.map[key_hash].pop(i)
            return True

    def print(self):
        print('----PHONEBOOK-----')
        for item in self.map:
            if item is not None:  # prints every not none in the array
                print(str(item))


h = HashMap()
h.add('Bob', '567-8008')
h.add('Eddy', '567-8118')
h.add('Eddy', '567-8813')
h.add('Mike', '567-1288')
h.print()
h.delete('Bob')
h.print()
print('Mike: ' + h.get('Mike'))


