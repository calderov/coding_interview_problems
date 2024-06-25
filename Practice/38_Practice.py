# 208. Implement Trie (Prefix Tree) (Medium)
# A trie (pronounced as "try") or prefix tree is a tree data structure used
# to efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
# 
# Implement the Trie class:
# - Trie() Initializes the trie object.
# 
# - insert(String word) Inserts the string word into the trie.
# 
# - search(String word) Returns true if the string word is in the trie
#                       (i.e., was inserted before), and false otherwise.
# 
# - startsWith(String prefix) Returns true if there is a previously
#                             inserted string word that has the prefix prefix,
#                             and false otherwise.
# 
# Example:
# trie = new PrefixTree();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

from collections import deque

class Node:
    def __init__(self, label=""):
        self.label = label
        self.neighbors = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if word == "":
            self.root.isWord = True
            return

        pending = deque(word)
        node = self.root

        while pending:
            c = pending.popleft()
            
            if c in node.neighbors:
                node = node.neighbors[c]
                node.isWord = node.isWord or len(pending) == 0
                continue

            node.neighbors[c] = Node(node.label + c)
            node = node.neighbors[c]
            node.isWord = node.isWord or len(pending) == 0

    def search(self, word: str) -> bool:
        if word == "":
            return self.root.isWord

        pending = deque(word)
        node = self.root

        while pending:
            c = pending.popleft()

            if c not in node.neighbors:
                return False

            node = node.neighbors[c]
            if node.isWord and len(pending) == 0:
                return True

        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True

        pending = deque(prefix)
        node = self.root

        while pending:
            c = pending.popleft()

            if c not in node.neighbors:
                return False

            node = node.neighbors[c]
            if len(pending) == 0:
                return True

        return False

if __name__ == "__main__":
    # Example 1
    trie = PrefixTree()
    
    trie.insert("app")
    trie.insert("apple")
    
    print(trie.search("app"), True)     # return True
    print(trie.startsWith("appl"), True) # return True
    print()

    # Example 2 ["PrefixTree", "insert", "", "search", "", "startsWith", "a"]
    trie = PrefixTree()
    
    trie.insert("")
    
    print(trie.search(""), True)     # return True
    print(trie.startsWith("a"), False) # return False