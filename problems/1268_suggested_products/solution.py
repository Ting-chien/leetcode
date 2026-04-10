from typing import List


class Node:
    def __init__(self):
        self.children: dict[str, Node] = {}  # key: 字元, value: TrieNode
        self.is_end: bool = False # 是否為字串結尾


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

    def startsWith(self, prefix: str) -> bool:
        """
        Search word in trie, return True if found and
        False otherwise.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        suggesstion = self.suggest(node, prefix, [prefix] if node.is_end else [])
        return suggesstion
    
    def suggest(self, node: Node, path: str, suggesstion: List[str] = []):
        """
        Return at most three suggesstion from Trie. Traverse
        through trie lexicographically.

        For example,

                    b
                  / | \
                a.  i.  l
              / |.  |.  |
             r. t.  k.  u
                    e   e
        
            we will find bar -> bat -> bit -> blue(won't show)
            in lexicographically order.

            suggesstion=[bar, bat, bit]
            b -> a -> r 
                   -> t
              -> i -> k -> e
        """
        for char, child in sorted(node.children.items()):
            if len(suggesstion) >= 3:
                return suggesstion
            if child.is_end:
                suggesstion.append(path+char)
            self.suggest(node=child, path=path+char, suggesstion=suggesstion)
        return suggesstion

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        在 Leetcode 208. Trie 裡有實作 Trie 的 insert/search/prefix 函數，我們這裡保留
        insert 函數作為一開始塞入 products 所有字串的用途，另外實作一 suggest 函數，用來找出「最多
        三個」prefix 相符的方法。

        Approach
        1. Initialize trie and put all products into Trie
        2. For loop searchWord and get suggestion by every prefix

        Edge cases:
        1. All lowercase letters ? Yes
        2. What is suggesstion means ? => All match in prefix
        3. What if no match ? => Return []
        """
        # Initialize trie and import products
        trie = Trie()
        for p in products:
            trie.insert(p)

        # Print from root
        res = []
        for i in range(len(searchWord)):
            suggesstion = trie.startsWith(prefix=searchWord[:i+1])
            res.append(suggesstion)

        return res


# Example 0:
# Input: products = ["bar", "bat", "bike", "blue"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
# res = Solution().suggestedProducts(products = ["bar", "bat", "bike", "blue"], searchWord = "mouse")


# Example 1:
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
res = Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")
print(res)