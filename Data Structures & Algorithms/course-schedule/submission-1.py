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

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely checked

        state = [0] * numCourses

        def dfs(course):

            # We reached a course that is already
            # in our current DFS path.
            #
            # Example:
            # 0 -> 1 -> 2 -> 0
            #
            # This means there is a cycle.

            if state[course] == 1:
                return False

            # This course was already completely checked.
            # We already know there is no cycle from here.
            #
            # So don't run DFS again.
            if state[course] == 2:
                return True

            # Mark this course as currently being explored.
            state[course] = 1

            # Look at every course that depends on this course.
            for next_course in graph.get(course, []):

                # If any path contains a cycle,
                # the whole answer is False.
                if not dfs(next_course):
                    return False

            # We finished checking this course.
            # No cycle was found from here.
            state[course] = 2

            return True

        # Try every course.
        for course in range(numCourses):

            if not dfs(course):
                return False

        return True
        