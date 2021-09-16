class TrieNode:
    def __init__(self,val=""):
        self.val=val
        self.nextnodes=dict()
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nowNode=self.root
        for i in word:
            if i in nowNode.nextnodes.keys():
                nowNode=nowNode.nextnodes[i]
            else:
                tempNode=TrieNode(i)
                nowNode.nextnodes[i]=tempNode
                nowNode=nowNode.nextnodes[i]
        nowNode.nextnodes[""]=1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        nowNode=self.root
        for i in word:
            if i in nowNode.nextnodes.keys():
                nowNode=nowNode.nextnodes[i]
            else:
                return False
        if "" in nowNode.nextnodes.keys():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        nowNode=self.root
        for i in prefix:
            if i in nowNode.nextnodes.keys():
                nowNode=nowNode.nextnodes[i]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)