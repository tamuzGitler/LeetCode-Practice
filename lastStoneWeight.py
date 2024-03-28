import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-num for num in stones]
        heapq.heapify(stones)
        while(len(stones) > 1):
            y = - heapq.heappop(stones)
            x = - heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, - (y-x))
        return -stones[0] if stones else 0


if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    sol = Solution()
    print(sol.lastStoneWeight(stones))
