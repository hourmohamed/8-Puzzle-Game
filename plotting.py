import time 
import matplotlib.pyplot as plt
import bfs, dfs, Astar
from Astar import manhDist, eucliDist

def runBfs(initState):
    sTime = time.time()
    path, visited_len, counter=bfs.bfs(initState)
    eTime = time.time()
    totTime = eTime - sTime
    return totTime

def runDfs(initState):
    sTime = time.time()
    path, visited_len, counter=dfs.DFS(initState)
    eTime = time.time()
    totTime = eTime - sTime
    return totTime

def runAstarEucli(initState):
    sTime = time.time()
    path, visited_len, counter=Astar.aStarWithBothH(initState,eucliDist)
    eTime = time.time()
    totTime = eTime - sTime
    return totTime

def runAstarManh(initState):
    sTime = time.time()
    path, visited_len, counter=Astar.aStarWithBothH(initState,manhDist)
    eTime = time.time()
    totTime = eTime - sTime
    return totTime

def plotTimes(times):
    algor = list(times.keys())
    totTimes = [times[algo] for algo in algor]
    
    figure, axis = plt.subplots(figsize=(12, 6))
    barWidth = 0.2
    idx = list(range(len(algor)))
    
    for n, initState in enumerate(times[algor[0]].keys()):
        axis.bar([m + n * barWidth for m in idx],
                 [times[algo].get(initState, 0) for algo in algor],
                 barWidth, label=f'Initial State {n+1}')
        
    axis.set_xlabel('Algorithms')
    axis.set_ylabel('Times in sec')
    axis.set_title('Time Comparison Between Algorithms')
    axis.set_xticks([r + barWidth for r in range(len(algor))])
    axis.set_xticklabels(algor)
    axis.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    initStates = ['123405678', '123456780', '345012678']
    totTimes = {
        'BFS':{},
        'DFS':{},
        'A* Euclidean': {},
        'A* Manhattan': {}
    }
    
    for initState in initStates:
        totTimes['BFS'][initState] = runBfs(initState)
        totTimes['DFS'][initState] = runDfs(initState)
        totTimes['A* Euclidean'][initState] = runAstarEucli(initState)
        totTimes['A* Manhattan'][initState] = runAstarManh(initState)
        
    plotTimes(totTimes)
        