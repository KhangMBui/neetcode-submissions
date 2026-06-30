class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not numCourses or not prerequisites:
            return True
        
        # Benefit from DFS perhaps
        # Firstly, create a dictionary: { course : [prereqs]}
        # { 2: [1], 1: [0, 0.5]}, etc.

        # We need to detect a cycle 
        # (bc it'd be impossible to complete courses involved in the cycle)


        pre_map = defaultdict(list)
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        # We iterate over each course, run a DFS from
        # that course, and first try to finish its prereq courses
        # by recursively traversing through them
        # To detect a cycle, we initialize a hash set called path,
        # which contains the nodes visited in the current DFS call
        # If we encounter a course already in path, we can conclude that
        # a cycle is detected
        path = set()

        def dfs(course: int) -> bool:
            if course in path: # cycle detected
                return False
            # We reached a point where there's no
            # prerequisites
            if not pre_map[course]:
                return True
            
            # Add the current course to the set:
            path.add(course)
            
            pre_course = pre_map[course]

            for pre in pre_course:
                if not dfs(pre):
                    return False
            
            # Done checking this course's prerequisites:
            path.remove(course)

            # mark this course as having no remaining unsafe prerequisites
            pre_map[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True