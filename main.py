from uniformCost import uniform_cost_search
from Astar import a_star_search
from heuristics import misplaced_tiles_heuristic, euclidean_heuristic
from helpers import is_solvable

if __name__ == "__main__":
    
    print("Welcome to Bilal Nasirs 8 puzzle solver\n")
    print("1. Use a default puzzle")
    print("2. Use a custom puzzle")
    
    puzzle_choice = int(input("Enter your choice (1 or 2):"))
    
    if puzzle_choice == 1:
        print("1. Trivial")
        print("2. Very Easy")
        print("3. Easy")
        print("4. Doable")
        print("5. Oh Boy")
        print("6. Impossible")
        start_choice = int(input("Enter your choice (1, 2, 3, 4, 5, or 6):"))
        if start_choice == 1:
            start = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        if start_choice == 2:
            start = ((1, 2, 3), (4, 5, 6), (7, 0, 8))
        if start_choice == 3:
            start = ((1, 2, 0), (4, 5, 3), (7, 8, 6))
        if start_choice == 4:
            start = ((0, 1, 2), (4, 5, 3), (7, 8, 6))
        if start_choice == 5:
            start = ((8, 7, 1), (6, 0, 2), (5, 4, 3))
        if start_choice == 6:
            start = ((1, 2, 3), (4, 5, 6), (8, 7, 0))
    if puzzle_choice == 2:
        start = []
        for i in range(3):
            row = tuple(map(int, input(f"Enter values for row {i + 1} separated by spaces: ").split()))
            start.append(row)
        start = tuple(start)


    goal = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    solvable = is_solvable(start)
    
    if solvable:
        print("\nSelect a algorithm:")
        print("1. Uniform Cost")
        print("2. A* with misplaced tile")
        print("3. A* with euclidean distance")
    
        algorithm_choice = int(input("Enter your choice (1, 2, or 3): "))
        print("\nSTART STATE\n")
        print("{} {} {}".format(*start[0]))
        print("{} {} {}".format(*start[1]))
        print("{} {} {}".format(*start[2]))
        print("\n") 
    
        if algorithm_choice == 1:
            uniform_cost_search(start, goal)
        elif algorithm_choice == 2:
            a_star_search(start, goal, misplaced_tiles_heuristic)
        elif algorithm_choice == 3:
            a_star_search(start, goal, euclidean_heuristic)
    else:
        print("Puzzle Not Solvable")