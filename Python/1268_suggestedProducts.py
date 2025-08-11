from typing import List


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
        

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        在 Leetcode 208. Trie 裡有實作 Trie 的 insert/search/prefix 函數，我們這裡保留
        insert 函數作為一開始塞入 products 所有字串的用途，另外實作一 suggest 函數，用來找出「最多
        三個」prefix 相符的方法。

        Approach
        1. Initialize trie and put all products into Trie
        2. For loop searchWord and get suggestion by every prefix
        """