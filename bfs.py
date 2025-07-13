from queue import Queue
from Tree import Tree
GOAL_STATE = "012345678"


def bfs(intial_state):
    print("in bfs")
    tree = Tree()
    frontier = Queue()
    # enter the state + path 
    frontier.put([intial_state, [intial_state], 0])
    explored = set()
    in_frontier = set()  
    in_frontier.add(intial_state)
    max_depth = 0
    
    #  starting the tree with level 0
    counter = -1  

    while frontier:

        state, path, depth = frontier.get()
        explored.add(state)
        in_frontier.remove(state)

        if GOAL_STATE == state:
            print(f"path: {path}")
            print(f"expanded length: {len(explored)}")
            print(f"counter : {counter}")
            return path, len(explored), max_depth
                
        valid_moves = tree.valid_move(state)
        valid_moves = valid_moves.split(',')
        valid_moves = [item for item in valid_moves if item]

        if depth>max_depth:
            max_depth = depth

        for neighbor in valid_moves:
            new_state = tree.move(state[:], neighbor)

            if new_state not in explored and new_state not in in_frontier:
                frontier.put((new_state, path + [new_state], depth+1))
                in_frontier.add(new_state)

        counter+=1
    

# if __name__ == "__main__":
#     testState = "012345678"
#     print("\nInitial state: ", testState)
#     path, no_ex = bfs(testState)
#     print("\npath: ", path)
#     print("\nnumber of expanded nodes: ", no_ex)
