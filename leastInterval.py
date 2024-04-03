from collections import Counter, deque
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count_dict = Counter(tasks)
        appearances = (list(count_dict.values()))
        appearances = [-app for app in appearances]
        heapq.heapify(appearances)  # use most common letter
        queue = deque()
        time = 0
        while (appearances or queue):
            if appearances:
                app = heapq.heappop(appearances) + 1
                if app != 0:
                    queue.appendleft([app, time + n])
            if queue and queue[-1][1] == time:  # can insert back to heap
                app = queue.pop()[0]
                heapq.heappush(appearances, app)

            time += 1
        return time


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    tasks = ["A", "C", "A", "B", "D", "B"]
    n = 1
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 3
    sol = Solution()
    time = sol.leastInterval(tasks, n)
    print(time)
