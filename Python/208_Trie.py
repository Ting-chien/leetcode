class Node:
    def __init__(self):
        self.children = {}  # key: 字元, value: TrieNode
        self.is_end = False # 是否為字串結尾

class Trie:
    """
    實作一個 Trie 資料結構，包含 insert, search, startWith
    三個函數。
    """
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Insert a word into trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Search word in trie, return True if found and is_end,
        return False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Search word in trie, return True if found and
        False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("apple"))
obj.insert("app")
print(obj.search("app"))