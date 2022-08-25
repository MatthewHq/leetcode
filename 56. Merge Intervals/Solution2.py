class Solution:
    def merge(self, intervals):
        completed = []

        intervals.sort()
        intervals.reverse()
        # print(intervals)

        while len(intervals) > 1:
            # print("=====")
            # print(completed)
            # print(intervals)
            # print("=====")
            
            curr = len(intervals)-1
            next = curr-1
            p1 = intervals[curr]
            p2 = intervals[next]

            if not p1[1] < p2[0]:
                newInt = [p1[0], max(p1[1], p2[1])]
                intervals.pop()
                intervals.pop()
                intervals.append(newInt)
            else:
                completed.append(intervals.pop())
        completed.append(intervals[0])
        
        return completed
        # print(completed)
        # print(intervals)


# intervals = [[1, 3], [2, 6], [12, 19], [23, 25], [28, 30],  # [[1, 6], [8, 19], [23, 26], [28, 30], [32, 34]]
#              [32, 33], [33, 34], [8, 13], [23, 26], [29, 30]]
# intervals = [[1, 4], [0, 0], [2, 2]]  # [[0, 0], [1, 4]]
# intervals = [[1, 4], [0, 2], [3, 5]]  # [[0, 5]]
# intervals = [[1, 4], [5, 6]]  # [[1, 4], [5, 6]]
# intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]  # [[5, 5], [2, 4]]
intervals = [[2, 3], [2, 2], [3, 3], [1, 3],
             [5, 7], [2, 2], [4, 6]]  # [[1,3],[4,7]]

intervals = [[1, 3], [0, 2], [2, 3], [4, 6], [
    4, 5], [5, 5], [0, 2], [3, 3]]  # [[0,3],[4,6]]
intervals = [[1, 1], [3, 3], [0, 0], [0, 0], [1, 1]]

sol = Solution()
print(sol.merge(intervals))
