class Solution:
    def canFinish(self, numCourses, prereqs):
        graph = {}
        for prereq in prereqs:
            if prereq[0] in graph:
                graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]]
        for course in range(numCourses):
            if self._hasCycle(graph, course, set(), {}):
                return False

        return True

    def _hasCycle(self, graph, course, seen, cache):
        if course in cache:
            return cache[course]
        if course in seen:
            return True
        if course not in graph:
            return False
        seen.add(course)
        ret = False
        for neighbors in graph[course]:
            if self._hasCycle(graph, neighbors, seen, cache):
                ret = True
                break
        seen.remove(course)
        cache[course] = ret
        return ret


print(Solution().canFinish(2, [[1, 0]]))
# True

print(Solution().canFinish(2, [[1, 0], [0, 1]]))
# False
