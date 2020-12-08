class TriNode:
        def __init__(self, isword = False):
            self.Next = [None] * 26
            self.isWord = isword


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TriNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            index = ord(ch) - 97
            if not node.Next[index]:
                node.Next[index] = TriNode()
            node = node.Next[index]
        node.isWord = True



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self.root
        for ch in word:
            index = ord(ch) - 97
            if not node.Next[index]:    return False
            node = node.Next[index]
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            index = ord(ch) - 97
            if node.Next[index] == None:    return False
            node = node.Next[index]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)