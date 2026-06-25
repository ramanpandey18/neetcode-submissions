class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word   # mark end of word

        ROWS, COLS = len(board), len(board[0])
        results = []

        # ── Step 2: DFS from every cell ────────────────────────────────
        def dfs(node, r, c):
            ch = board[r][c]

            # No path in Trie → prune this branch immediately
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # Found a complete word
            if next_node.word:
                results.append(next_node.word)
                next_node.word = None   # de-duplicate: don't find it again

            # Mark cell as visited by temporarily replacing its character
            board[r][c] = '#'

            # Explore all 4 neighbors
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(next_node, nr, nc)

            # Restore cell (backtrack)
            board[r][c] = ch

            # Trie pruning: if this node has no more children worth exploring, remove it
            if not next_node.children:
                del node.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c)

        return results