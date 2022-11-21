from typing import List


class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.m = len(maze)
        self.n = len(maze[0])
        maze[entrance[0]][entrance[1]] = '*'
        query=[(entrance,0)]
        exits = []
        while len(query) > 0:
            self.bfs(maze,query,exits,entrance)
        if exits:
            return min(exits)
        return -1

    def bfs(self, maze,query:list,exits,entrance):
        cord,point = query.pop(0)
        
        if cord != entrance and self.isBorder(cord):
            exits.append(point)
            return
    
        
            # right, left, down, up
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for move in moves:
            
            x = cord[0]+move[0]
            y = cord[1]+move[1]
            if x >= 0 and y >= 0 and x < self.m and y < self.n and maze[x][y] == '.':
                maze[x][y] = '*'
                query.append(([x,y], point+1))
                

    def isBorder(self, cord):
        return cord[0] == 0 or cord[1] == 0 or cord[0] == self.m - 1 or cord[1] == self.n - 1


s = Solution()

print(s.nearestExit(
    maze = [[".",".",".",".",".","+",".",".","."],[".","+",".",".",".",".",".",".","."],[".",".","+",".","+",".","+",".","+"],[".",".",".",".","+",".",".",".","."],[".",".",".",".","+","+",".",".","."],["+",".",".",".",".",".",".",".","."],[".",".",".","+",".",".",".",".","."],[".",".",".","+",".",".",".",".","+"],["+",".",".","+",".","+","+",".","."]],
    entrance = [8,4]
))

