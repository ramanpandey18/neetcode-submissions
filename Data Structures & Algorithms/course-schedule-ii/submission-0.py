class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Course Schedule I:
        #     detect cycle
        #         ↓
        #     True / False


        # Course Schedule II:
        #     detect cycle
        #         ↓
        #     store finished courses
        #         ↓
        #     reverse result
        #         ↓
        #     course order

        # 0 → haven't started
        # 1 → currently inside DFS
        # 2 → completely finished

        graph = {}

        for course, prereq, in prerequisites:
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)

        state = [0] * numCourses
        result = []

        def dfs(course):
            if state[course] == 1:
                return False
            
            if state[course] == 2:
                return True
            
            state[course] = 1
            for next_course in graph.get(course, []):
                if not dfs(next_course):
                    return False
            state[course] = 2
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result[::-1]


