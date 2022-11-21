from typing import List


def removeStones(stones: List[List[int]]) -> int:
    
    rows = set()
    cols = set()
    remove_count = 0
    
    for stone in stones:
        if not (stone[0] not in rows and stone[1] not in cols):
            remove_count += 1
        rows.add(stone[0])
        cols.add(stone[1])
    return remove_count
                
        
removeStones([[0,1],[1,0],[1,1]])
# [[0,1],[1,0],[1,1]] -> 2
# [[0,1],[1,0]] -> 0