"""
Implement a trie with insert,search and starts_with methods

interface Trie {
void insert(String word);
Boolean search(String word);
Boolean startsWith(String prefix);
"""


class TrieNode:
    def __init__(self):
        self.end = False
        self.keys = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, node=None):
        if not node:
            node = self.root
        if len(word) == 0:
            node.end = True
            return
        elif word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word=word[1:], node=node.keys[word[0]])
        else:
            self.insert(word=word[1:], node=node.keys[word[0]])

    def search(self, word, node=None):
        if not node:
            node = self.root
        if len(word) == 0 and node.end:
            return True
        elif len(word) == 0:
            return False
        elif word[0] not in node.keys:
            return False
        else:
            return self.search(word=word[1:], node=node.keys[word[0]])

    def starts_with(self, prefix, node):
        if not node:
            node = self.root
        if len(prefix) == 0:
            return True
        elif prefix[0] not in node.keys:
            return False
        else:
            return self.starts_with(
                prefix=prefix[1:], node=node.keys[prefix[0]]
            )


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))
    print(t.starts_with("app", t.root))
