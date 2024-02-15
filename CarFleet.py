

class Solution:
    def carFleet(self, target: int, position, speed):
        arr = list(zip(position, speed))
        arr.sort()
        arr = arr[::-1]
        stack = [arr[0]]
        for data in arr[1:]:
            basckPos, backCurSpeed = data # unpack
            backCarTime = (target - basckPos) / backCurSpeed
            frontPos, frontCurSpeed = stack[-1]
            frontCarTime = (target - frontPos) / frontCurSpeed
            if backCarTime > frontCarTime: # back car and front car cannot become a fleet
                stack.append(data)
        return len(stack)


if __name__ == '__main__':
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    sol = Solution()
    print(sol.carFleet(target1, position1, speed1))

    target2 = 10
    position2 = [3]
    speed2 = [3]
    sol = Solution()
    print(sol.carFleet(target2, position2, speed2))

    target2 = 100
    position2 = [0,2,4]
    speed2 = [4,2,1]
    sol = Solution()
    print(sol.carFleet(target2, position2, speed2))
