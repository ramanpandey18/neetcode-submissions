class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(list)

        # Every character must exist in the graph
        for word in words:
            for char in word:
                graph[char]

        # Build ordering rules
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Invalid case: ["abc", "ab"]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    break

        state = {}
        result = []

        def dfs(char):
            # Cycle detected
            if state.get(char) == 1:
                return False

            # Already completely processed
            if state.get(char) == 2:
                return True

            state[char] = 1

            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False

            state[char] = 2
            result.append(char)

            return True

        for char in graph:
            if not dfs(char):
                return ""

        return "".join(result[::-1])
        