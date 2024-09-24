class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:

                while stack and stack[-1] > 0 and abs(asteroid) > stack[-1]:  # remove smaller astroids moving right
                    stack.pop()
                if stack and stack[-1] > abs(asteroid):
                    continue
                elif stack and (stack[-1]) == abs(asteroid):
                    stack.pop()
                else:
                    stack.append(asteroid)

        return stack


if __name__ == '__main__':
    asteroids = [2, -2]
    sol = Solution()
    print(sol.asteroidCollision(asteroids))
