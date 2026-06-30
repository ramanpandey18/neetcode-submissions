class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max_area = 0
        # # Stack stores (start_index, height)
        # # start_index = how far LEFT this bar's rectangle can extend
        # stack = []

        # for i, h in enumerate(heights):
        #     # This tracks where the current bar's rectangle can START
        #     start = i

        #     # Pop all bars taller than current height
        #     while stack and stack[-1][1] > h:
        #         idx, height = stack.pop()
        #         # This bar's rectangle: from idx to current i (exclusive)
        #         # width = i - idx
        #         max_area = max(max_area, height * (i - idx))
        #         # Current bar can extend back to where this popped bar started
        #         start = idx

        #     stack.append((start, h))

        # # Bars still in stack can extend all the way to the right end
        # for idx, height in stack:
        #     max_area = max(max_area, height * (len(heights) - idx))

        # return max_area


        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area

        
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
        for idx, height in stack:
            max_area = max(max_area, height * (len(heights) - idx))
        return max_area