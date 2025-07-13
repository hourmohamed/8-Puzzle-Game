
import heapq
from math import sqrt
from Tree import Tree

G_STATE = '012345678'

def manhDist(nstate):
    dist = 0
    for i in range(9):
        if nstate[i] != '0':
            x1, y1 = i % 3, i // 3
            x2, y2 = int(nstate[i]) % 3, int(nstate[i]) // 3
            dist += abs(x1 - x2) + abs(y1 - y2)
    return dist
# for both x1,y1 are the current element position
# x2,y2 are the goal position of this element
# the heuristic function of the state is how close is the given state
# to the goal state which is [012345678] so we calculate it by ->
# adding each heuristic function of each element in the state.

def eucliDist(nstate):
    dist = 0
    for i in range(9):
        if nstate[i] != '0':
            x1, y1 = i % 3, i // 3
            x2, y2 = int(nstate[i]) % 3, int(nstate[i]) // 3
            dist += sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return dist

def aStarWithBothH(initState, heuristic):
    priorityQueue = []
    initHeuristic = heuristic(initState)
    parentCost = 0
    heapq.heappush(priorityQueue, (initHeuristic, initState, [initState], parentCost))
    explored = set()
    statesCost = {initState: initHeuristic}

    tree = Tree()

    while priorityQueue:
        cCost, cState, cPath, cparentCost = heapq.heappop(priorityQueue)
        if cState in explored:
            continue

        explored.add(cState)
        if cState == G_STATE:
            print("Final State: ", cState)
            print("Path to goal:", cPath)
            print("Cost of path:", cparentCost)
            print("Nodes expanded:", len(explored))
            print("Search depth:", cparentCost)
            return cPath, len(explored), cparentCost

        vM = tree.valid_move(cState)
        vM = vM.split(',')
        vM = [item for item in vM if item]
        # converting vM to int for offset calculation
        for neighbor in vM:
            nState = tree.move(cState, neighbor)
            if nState not in explored:
                nCost = len(cPath) + 1 + heuristic(nState)
                # if not included in frontier or included but with higher cost
                if nState not in statesCost or nCost < statesCost[nState]:
                    heapq.heappush(priorityQueue, (nCost, nState, cPath + [nState], cparentCost+1))
                    statesCost[nState] = nCost

    return []


# counter == depth