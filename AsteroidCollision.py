class Solution:
    def asteroidCollision(self, asteroids) :
        stack = []
        for astroid in asteroids:

            while stack and stack[-1] > 0 > astroid:
                if stack[-1] < abs(astroid):
                    stack.pop()
                    continue
                elif  stack[-1] == abs(astroid):
                    stack.pop() # destroid astroid
                break
            else:
                stack.append(astroid)
        return stack

if __name__ == '__main__':
    asteroids1 = [5, 10, -5]
    asteroids2 = [8, -8]
    asteroids3 = [10, 2, -5]
    asteroids4 = [-2,-1,1,2]
    asteroids5 = [-2,1,1,-1]
    asteroids6 = [1,-2,-2,-2]
    asteroids7 = [-2,-2,1,-2]

    sol = Solution()
    print(sol.asteroidCollision(asteroids1))
    print(sol.asteroidCollision(asteroids2))
    print(sol.asteroidCollision(asteroids3))
    print(sol.asteroidCollision(asteroids4))
    print(sol.asteroidCollision(asteroids5))
    print(sol.asteroidCollision(asteroids6))
    print(sol.asteroidCollision(asteroids7))