class Solution:
    def carFleet(self, target: int, position, speed):
        fleet_stack = [[position[0], speed[0]]]
        for i in range(1, len(position)):
            cur_pos = position[i]
            if fleet_stack[-1][0] == target:
                fleet_stack.append([position[i], speed[i]])
            elif cur_pos + speed[i] <= fleet_stack[-1][0] + fleet_stack[-1][1]:
                while cur_pos < fleet_stack[-1][0]:
                    fleet_stack[-1][0] += fleet_stack[-1][1]
                    cur_pos += speed[i]
                    if cur_pos >= fleet_stack[-1][0]:
                        fleet_stack[-1][0] = speed[i]
            else:
                fleet_stack.append([position[i], speed[i]])
        return len(fleet_stack)


if __name__ == '__main__':
    # target1 = 12
    # position1 = [10, 8, 0, 5, 3]
    # speed1 = [2, 4, 1, 1, 3]
    # sol = Solution()
    # print(sol.carFleet(target1, position1, speed1))
    #
    # target2 = 10
    # position2 = [3]
    # speed2 = [3]
    # sol = Solution()
    # print(sol.carFleet(target2, position2, speed2))

    target2 = 100
    position2 = [0,2,4]
    speed2 = [4,2,1]
    sol = Solution()
    print(sol.carFleet(target2, position2, speed2))
