class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Whenever we need the shortest path in an unweighted graph, think:
         # If endWord is not available,
        # we can never reach it.
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)

        queue = deque()

        # Store:
        # (word, number of words used)
        queue.append((beginWord, 1))

        # Avoid visiting the same word again
        visited = set()
        visited.add(beginWord)

        while queue:

            word, steps = queue.popleft()

            # We reached the target
            if word == endWord:
                return steps

            # Try changing every character
            for i in range(len(word)):

                # Try every letter a-z
                for char in "abcdefghijklmnopqrstuvwxyz":

                    # Create the new word
                    newWord = (
                        word[:i] +
                        char +
                        word[i + 1:]
                    )

                    # We only care about words
                    # that are actually in wordList.
                    if newWord not in wordSet:
                        continue

                    # Don't visit the same word again
                    if newWord in visited:
                        continue

                    visited.add(newWord)

                    # One more word in the sequence
                    queue.append((newWord, steps + 1))

        # No transformation possible
        return 0
        