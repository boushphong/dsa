# Trie
Trie is a tree-like data structure that is used to store a dynamic set of strings. 
- It is used to store strings that can be searched in `O(N)` (Word Length) time complexity, where N is the length of the string. 
- It is also used to store strings that share a common prefix.

| Operation            | Time Complexity | Explanation                                                                                                                              |
|----------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Insert**           | `O(N)`          | Inserting a word requires traversing its characters, where `N` is the length of the word.                                                |
| **Search**           | `O(M)`          | Searching for a word requires traversing its characters, where `N` is the length of the word.                                            |
| **Starts with**      | `O(N)`          | Checking if any word starts with a given prefix also involves traversing the prefix's characters, where `N` is the length of the prefix. |
| **Space Complexity** | `O(N * M)`      | In the worst case, where `N` is the number of words and `M` is the average length of words, each character is stored in a Trie node.     |

## Implementation
```python
class Trie:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def __repr__(self):
        return str(self.children)

    def insert(self, word) -> None:
        curTrieNode = self
        for letter in word:
            curTrieNode = self._insertLetter(letter, curTrieNode)
        curTrieNode.isEndOfWord = True

    @staticmethod
    def _insertLetter(letter, node):
        if letter not in node.children:
            node.children[letter] = Trie()
        return node.children[letter]

    def startsWith(self, prefix) -> bool:
        curTrieNode = self
        for letter in prefix:
            curTrieNode = self._search(letter, curTrieNode)
            if not curTrieNode:
                return False
        return True

    def search(self, word) -> bool:
        curTrieNode = self
        for letter in word:
            curTrieNode = self._search(letter, curTrieNode)
            if not curTrieNode:
                return False
        return curTrieNode.isEndOfWord

    @staticmethod
    def _search(letter, node):
        if letter not in node.children:
            return
        return node.children[letter]


if __name__ == '__main__':
    trie = Trie()
    trie.insert("hello")
    trie.insert("helld")
    print(trie.startsWith("hell"))  # True
    print(trie.startsWith("hello"))  # True
    print(trie)  # {'h': {'e': {'l': {'l': {'o': {}, 'd': {}}}}}}
```
