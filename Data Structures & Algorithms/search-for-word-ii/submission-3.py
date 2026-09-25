class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            current_node = root
            for char in word:
                if char not in current_node.children:
                    current_node.children[char] = TrieNode()
                current_node = current_node.children[char]
            current_node.word = word

        ROWS = len(board)
        COLS = len(board[0])
        results = []

        def dfs(trie_node, current_row, current_col):
            current_char = board[current_row][current_col]

            if current_char not in trie_node.children:
                return 
            
            next_trie_node = trie_node.children[current_char]
            if next_trie_node.word:
                results.append(next_trie_node.word)
                next_trie_node.word = None
            
            board[current_row][current_col] = "#"
            
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for row_change, col_change in directions:
                new_row = current_row + row_change
                new_col = current_col + col_change

                if new_row < 0 or new_row >= ROWS:
                    continue
                
                if new_col < 0 or new_col >= COLS:
                    continue
                
                if board[new_row][new_col] == "#":
                    continue
                
                dfs(next_trie_node, new_row, new_col)
            
            board[current_row][current_col] = current_char

            if not next_trie_node.children:
                del trie_node.children[current_char]

        for row in range(ROWS):
            for col in range(COLS):
                dfs(root, row, col)
        
        return results







        # ──────────────────────────────────────────────────────────────
        # Step 1: Build the Trie from all the words
        # ──────────────────────────────────────────────────────────────

        root = TrieNode()

        for word in words:
            current_node = root

            for char in word:

                if char not in current_node.children:
                    current_node.children[char] = TrieNode()

                current_node = current_node.children[char]

            # Store the complete word at the ending Trie node.
            # This lets us know when DFS has found a complete word.
            current_node.word = word


        ROWS = len(board)
        COLS = len(board[0])

        results = []


        # ──────────────────────────────────────────────────────────────
        # Step 2: DFS from every cell in the board
        # ──────────────────────────────────────────────────────────────

        def dfs(trie_node, current_row, current_col):

            # Get the character from the current board cell.
            current_char = board[current_row][current_col]


            # No path in Trie → prune this branch immediately.
            #
            # Example:
            # If the Trie expects "cat..." but the board gives us
            # "z", there is no reason to continue this DFS path.
            if current_char not in trie_node.children:
                return


            # Move one step forward in the Trie.
            next_trie_node = trie_node.children[current_char]


            # Found a complete word.
            #
            # Example:
            # If next_trie_node.word == "cat",
            # then we have successfully formed "cat" on the board.
            if next_trie_node.word:

                results.append(next_trie_node.word)

                # De-duplicate:
                # We already found this word, so don't add it again
                # if another path finds the same word.
                next_trie_node.word = None


            # Mark the current board cell as visited.
            #
            # We temporarily replace its character with '#'
            # so that the current DFS path cannot use this cell again.
            original_char = board[current_row][current_col]
            board[current_row][current_col] = '#'


            # ──────────────────────────────────────────────────────────
            # Explore all 4 neighbors
            #
            # (-1, 0) = UP
            # ( 1, 0) = DOWN
            # ( 0,-1) = LEFT
            # ( 0, 1) = RIGHT
            # ──────────────────────────────────────────────────────────

            directions = [
                (-1, 0),   # UP
                (1, 0),    # DOWN
                (0, -1),   # LEFT
                (0, 1)     # RIGHT
            ]

            for row_change, col_change in directions:

                # Calculate the neighboring cell.
                new_row = current_row + row_change
                new_col = current_col + col_change


                # ──────────────────────────────────────────────────────
                # Boundary check
                #
                # new_row must be between:
                #     0 and ROWS - 1
                #
                # new_col must be between:
                #     0 and COLS - 1
                # ──────────────────────────────────────────────────────

                if new_row < 0 or new_row >= ROWS:
                    continue

                if new_col < 0 or new_col >= COLS:
                    continue


                # Don't use a cell that is already part of
                # the current DFS path.
                if board[new_row][new_col] == '#':
                    continue


                # The neighbor is valid.
                # Continue DFS from this neighboring cell.
                dfs(
                    next_trie_node,
                    new_row,
                    new_col
                )


            # ──────────────────────────────────────────────────────────
            # Step 3: Backtracking
            # ──────────────────────────────────────────────────────────

            # Restore the original character.
            #
            # We marked this cell as '#' before DFS,
            # but other paths are allowed to use this cell.
            board[current_row][current_col] = original_char


            # ──────────────────────────────────────────────────────────
            # Step 4: Trie pruning
            # ──────────────────────────────────────────────────────────

            # If this Trie node has no children left,
            # there is no useful word remaining below this node.
            #
            # Remove this branch from the parent Trie node
            # so future DFS calls don't waste time exploring it.
            if not next_trie_node.children:
                del trie_node.children[current_char]


        # ──────────────────────────────────────────────────────────────
        # Step 5: Start DFS from every cell
        # ──────────────────────────────────────────────────────────────

        for row in range(ROWS):
            for col in range(COLS):

                dfs(root, row, col)


        # Return all words found in the board.
        return results