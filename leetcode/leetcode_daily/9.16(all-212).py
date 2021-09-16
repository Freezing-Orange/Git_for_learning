from typing import List
class TrieNode:
    def __init__(self):
        self.nextnodes=dict()


class Solution:
    def __init__(self):
        self.res=[]
        self.root=TrieNode()
    def insert(self, root, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nowNode=root
        for i in word:
            if i in nowNode.nextnodes.keys():
                nowNode=nowNode.nextnodes[i]
            else:
                tempNode=TrieNode()
                nowNode.nextnodes[i]=tempNode
                nowNode=nowNode.nextnodes[i]
        nowNode.nextnodes["word"]=word
        
    def delete(self, root, word: str):
        '''
        删除一个存在的单词
        '''
        nodesRoute=[]
        nowNode=root
        for i in word:
            nodesRoute.append(nowNode.nextnodes[i])
            nowNode=nowNode.nextnodes[i]
        for i in range(len(word)-1,-1,-1):
            if i==len(word)-1:
                del nodesRoute[i].nextnodes["word"]
            else:
                del nodesRoute[i].nextnodes[word[i+1]]
            if len(nodesRoute[i].nextnodes):
                return
        del self.root.nextnodes[word[0]]
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root=TrieNode()
        for i in words:
            self.insert(self.root,i)
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                self.dfs(board,self.root,i,j)
        return self.res

    def dfs(self, board,t,i,j):
        if i<0 or j<0 or i>=len(board) or j>=len(board[i]):
            return
        c=board[i][j]
        if c=="#" or c not in t.nextnodes.keys():
            return
        t=t.nextnodes[c]
        if "word" in t.nextnodes.keys():
            word=t.nextnodes["word"]
            self.res.append(word)
            self.delete(self.root,word)
        board[i][j]="#"
        self.dfs(board,t,i+1,j)
        self.dfs(board,t,i-1,j)
        self.dfs(board,t,i,j+1)
        self.dfs(board,t,i,j-1)
        board[i][j]=c
        return