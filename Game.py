import bfs
import dfs
import Astar
from Astar import eucliDist, manhDist
import time

class Game:
    def run_game(self):
        while True:
            initial_state = input('Enter initial state for the game (9 characters from 0 to 8): ')
             #fadel condition non-repeated
            if len(initial_state) == 9 and all(c in '012345678' for c in initial_state):
                break 
            else:
                print("Invalid input. Please enter exactly 9 characters, each from 0 to 8.")
        
        print("Pick the algorithm")
        print("1 - BFS")
        print("2 - DFS")
        print("3 - A*")
        
        while True:
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                time_1 = time.time()
                path, expanded_len, counter = bfs.bfs(initial_state)
                time_2 = time.time()
                print(f"path: {path}")
                print(f"expanded length: {expanded_len}")
                print(f"counter: {counter}")
                print(f"time taken for bfs: {time_2-time_1}")
                
            elif choice == '2':
                time_1 = time.time()
                path, expanded_len, count = dfs.DFS(initial_state)
                time_2 = time.time()
                print(f"path: {path}")
                print(f"expanded length: {expanded_len}")
                print(f"time taken for bfs: {time_2-time_1}")
                
            elif choice == '3':
                time_1 = time.time()
                path, expanded_len = Astar.aStarWithBothH(initial_state, eucliDist)
                time_2 = time.time()
                print(f"path: {path}")
                print(f"expanded length: {expanded_len}")
                print('A* implementation')
                print(f"time taken for bfs: {time_2-time_1}")
                
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    game = Game()
    game.run_game()
