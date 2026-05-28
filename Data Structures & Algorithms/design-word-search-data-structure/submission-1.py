class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:

            if char not in current.children:

                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):

            current = node

            for i in range(index, len(word)):

                char = word[i]

                if char == ".":

                    for child in current.children.values():

                        if dfs(i + 1, child):

                            return True

                    return False

                else:

                    if char not in current.children:

                        return False

                    current = current.children[char]

            return current.is_end

        return dfs(0, self.root)
        
