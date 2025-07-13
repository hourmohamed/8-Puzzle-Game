from Tree import Tree
from collections import deque

GOAL_TEST = '012345678'
MAX_DEPTH = 35

def DFS(initial_state):
    #zero for initial depth
    frontier = deque([(initial_state, [initial_state],0)]) 
    visited = set()
    tree = Tree()
    # starting the tree with level 0
    counter = 0
    max_depth = 0
    
    while frontier:
        state, path, depth = frontier.pop()
        # print(f"depth: {depth}")
        
        if state in visited:
            continue

        visited.add(state)

        if state == GOAL_TEST:
            print("Success")
            print("Path:", path)
            print(f"expanded length: {len(visited)}")
            return path, len(visited),max_depth
        
        if depth>max_depth:
            max_depth = depth
        # if depth exceeds the maxDepth then we skip it as if it doesn't have any children
        if depth >= MAX_DEPTH:
            continue
        
        valid_moves = tree.valid_move(state)
        valid_moves = valid_moves.split(',')
        valid_moves = [item for item in valid_moves if item]

        for neighbor in valid_moves:
           next_state = tree.move(state[:], neighbor)
           if next_state not in visited:
                frontier.append((next_state, path + [next_state], depth + 1))
               
        counter+=1
        # print(counter)
        
           
        
    print("Failure")
    # print("Expanded nodes:", visited)
    return [], len(visited), 0

# if __name__ == "_main_":
#     initial_state = '102345678'
#     path, expanded_len=DFS(initial_state)
#     print(f"path: {path}")
#     print(f"expanded length: {expanded_len}")