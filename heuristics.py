def misplaced_tiles_heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                h += 1
    return h
    
def euclidean_heuristic(state, goal):
    h = 0
    for row in range(3):
        for col in range(3):
            if state[row][col] != 0:
                goal_position = None
                for goal_row in range(3):
                    for goal_col in range(3):
                        if goal[goal_row][goal_col] == state[row][col]:
                            goal_position = (goal_row, goal_col)
                            break
                    if goal_position is not None:
                        break
                h += ((row - goal_position[0]) ** 2 + (col - goal_position[1]) ** 2) ** 0.5
    return h
