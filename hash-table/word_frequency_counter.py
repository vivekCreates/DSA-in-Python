class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, sentence):
        words = sentence.split()
        for word in words:
            index = self.hash_function(word)
            chain = self.table[index]

            # check if word exists
            for i, (k, v) in enumerate(chain):
                if k == word:
                    chain[i] = (k, v + 1)  # update count
                    break
            else:
                chain.append((word, 1))  # insert new word

    def count_frequency(self):
        freq = {}
        for chain in self.table:
            for word, count in chain:
                freq[word] = count
        return freq


ht = HashTable()
ht.insert("the cat and the dog and the cat")
print(ht.count_frequency())
