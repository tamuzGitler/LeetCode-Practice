def solution(plan):
    min_number_of_runs = 0
    rows = len(plan)
    cols = len(plan[0])

    visited = []
    for row in range(rows):
        for col in range(cols):
            if (row, col) in visited:
                continue
            encounter_dirty_floor = [False]  # can change into global variable
            visit_all_directions(plan, row, col, encounter_dirty_floor, visited)
            if encounter_dirty_floor[0]:
                min_number_of_runs += 1

    return min_number_of_runs


def visit_all_directions(plan, row, col, encounter_dirty_floor, visited):
    if row < 0 or row >= len(plan):  # check rows
        return
    if col < 0 or col >= len(plan[0]):  # check cols
        return
    if (row, col) in visited:
        return
    if plan[row][col] == '#':  # wall
        return
    visited.append((row, col))

    if plan[row][col] == '*':  # clean
        encounter_dirty_floor[0] = True

    visit_all_directions(plan, row - 1, col, encounter_dirty_floor, visited)
    visit_all_directions(plan, row + 1, col, encounter_dirty_floor, visited)
    visit_all_directions(plan, row, col - 1, encounter_dirty_floor, visited)
    visit_all_directions(plan, row, col + 1, encounter_dirty_floor, visited)


if __name__ == '__main__':
    plan = ['**###**', '*#*#*#*', '##*#*##', '*#***#*', '.#####.', '..*#*..']

    print(solution(plan))
