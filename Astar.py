import heapq
from helpers import find_blank_square, valid_actions, print_data_a_star, take_action

def a_star_search(start, goal, heuristic):
    visited = set()
    g = 0
    f = g + heuristic(start, goal)
    heap = [(f, g, start, [])]
    counter = 0
    max_depth = 0
    while heap:
        counter += 1
        f, g, state, path = heapq.heappop(heap)
        max_depth = max(max_depth, len(heap))
        
        
        if state == goal:
            print("\nFINAL STATE\n")
            print_data_a_star(g, heuristic(state, goal), f, state, path)
            print("NODES EXPANDED: {}".format(counter))
            print("MAXIMUM QUEUE DEPTH: {}".format(max_depth))
            
            return g, path
        if state in visited:
            continue
        
        visited.add(state)
        print_data_a_star(g, heuristic(state, goal), f, state, path)
        
        blank_square = find_blank_square(state)
        actions = valid_actions(state, blank_square)
        
        for (row, col, direction) in actions:
            new_state = take_action(state, (row, col, direction))
            new_path = path + [direction]
            cost = len(new_path)
            f = cost + heuristic(new_state, goal)
            heapq.heappush(heap, (f, cost, new_state, new_path))

    return None
