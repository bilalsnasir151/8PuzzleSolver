def find_blank_square(state):
    for i, row in enumerate(state):
        for j, col in enumerate(row):
            if col == 0:
                return i, j

def valid_actions(state, blank_square):
    row, col = blank_square
    actions = []
    if row > 0:
        actions.append((row - 1, col, 'UP'))
    if row < 2:
        actions.append((row + 1, col, 'DOWN'))
    if col > 0:
        actions.append((row, col - 1, 'LEFT'))
    if col < 2:
        actions.append((row, col + 1, 'RIGHT'))
    return actions
    

def take_action(state, action):
    row, col, direction = action
    blank_square = find_blank_square(state)
    blank_row, blank_col = blank_square
    new_state = [list(row) for row in state]
    new_state[blank_row][blank_col], new_state[row][col] = new_state[row][col], new_state[blank_row][blank_col]
    return tuple([tuple(row) for row in new_state])
    
def print_data_a_star(g, h, f, state, path):
    print("Cost/Depth: {}".format(g))
    print("Heuristic value: {}".format(h))
    print("f: {}".format(f))
    print("Puzzle state:")
    print("{} {} {}".format(*state[0]))
    print("{} {} {}".format(*state[1]))
    print("{} {} {}".format(*state[2]))
    print("Moves: {}\n".format(path))

def print_data(g, state, path):
    print("Cost/Depth: {}".format(g))
    print("Puzzle state:")
    print("{} {} {}".format(*state[0]))
    print("{} {} {}".format(*state[1]))
    print("{} {} {}".format(*state[2]))
    print("Moves: {}\n".format(path))


def is_solvable(puzzle):
    inversion_count = 0
    flat_puzzle = [tile for row in puzzle for tile in row]
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] != 0 and flat_puzzle[j] != 0 and flat_puzzle[i] > flat_puzzle[j]:
                inversion_count += 1
    return inversion_count % 2 == 0
