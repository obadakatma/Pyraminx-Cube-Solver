from collections import deque
from Cube import Pyraminx
import time
import json
 
def bfs_generate_combinations(solved_state):
    visited = set()
    queue = deque([solved_state])
    visited.add(solved_state)
    allStates = {}
    mov = 0
    allStates[solved_state] = mov
    moves = [(r,d) for r in ['U','R','L','B'] for d in [0,1]]
    while queue:
        currentState = queue.popleft()
        cube = Pyraminx(state=currentState)

        # Generate new states by applying all possible moves
        for move in moves:
            newState = None
            if move[0] == 'U':
                newState = cube.up(move[1])
            elif move[0] == 'R':
                newState = cube.right(move[1])
            elif move[0] == 'L':
                newState = cube.left(move[1])
            elif move[0] == 'B':
                newState = cube.back(move[1])
            newState = newState.stringify()
            
            if newState not in visited:
                visited.add(newState)
                queue.append(newState)
                mov = move[0]+('`' if move[1] == 0 else '')
                allStates[newState] = mov
    return allStates

start = time.time()

l = bfs_generate_combinations("rrrrrrrrryyyyyyyyygggggggggbbbbbbbbb")

json_object = json.dumps(l, indent=4)
with open("Combinations.json", "w") as outfile:
    outfile.write(json_object)

print("time = ",time.time()-start)
print("Number of combinations : ",len(l))
