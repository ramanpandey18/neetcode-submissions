class Solution:
    def canFinish(self, numCourses, prerequisites):

        # graph[prerequisite] = courses that depend on it
        #
        # Example:
        # [0, 1] means:
        # 1 must be taken before 0
        #
        # So:
        # 1 -> 0
        graph = {}

        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = []
            graph[prereq].append(course)

        state = [0] * numCourses   

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
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
