from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        ending_char = word[-1]
        ending_points = []
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == ending_char:
                    ending_points.append((i,j))
    
        if ending_points:
            for point in ending_points:
                seen_point={}
                # seen_point[f'{point[0]},{point[1]}']=1
                result = self.dfs(board,point,seen_point,word,word_idx=len(word)-1)
                if result:
                    return True
        return False
    
    def dfs(self,board,cord,seen_point:dict,word:str,word_idx:int):
        x,y = cord
        seen_point[f'{x},{y}']=1
        if word_idx == 0 and \
            board[x][y] == word[word_idx]:
                return True
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for move in moves:
            nx,ny = move
            nx = x + nx
            ny = y + ny
            if nx >= 0 and ny>= 0 and ny<self.n and nx<self.m and not seen_point.get(f'{nx},{ny}'):
                if board[nx][ny] == word[word_idx-1]:
                    if self.dfs(board,(nx,ny),seen_point,word,word_idx-1):
                        return True
        seen_point.pop(f'{x},{y}')
        return False
        

s = Solution()

print(s.exist(board = 
              [["A","B","C","E"],
               ["S","F","E","S"],
               ["A","D","E","E"]], word = "ABCESEEEFS"))