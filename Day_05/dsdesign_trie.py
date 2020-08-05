class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        current = self.trie
        for letter in word:
            current = current.setdefault(letter, {})
        current['_end_'] = word

    def search(self, word):
        return self.recursive_search(word, len(word), self.trie)

    def recursive_search(self, word, length, node):

        # prevent value in '_end_' be treated as new child
        if type(node) is not dict:
            return False

        current = node
        for i in range(len(word)):
            letter = word[i]

            # once meet '.', do recursive search for all it's children
            if letter == '.':
                return any([self.recursive_search(word[i+1:], length, current[child]) for child in current])

            # prefix not match, return False directly
            if letter not in current:
                return False

            current = current[letter]

        # once it runs to this line, it means all explicit letters are matched
        # so we only have to check the target word's length is matched
        return len(current.get('_end_', '')) == length

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)