# Time: O(m8n)
# Space:O(m*n)
# Leetcode:Yes
# Issues:None

from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = {(-1,-1),(-1,1),(-1,0),(1,1),(1,-1),(1,0),(0,1),(0,-1)}
        m = len(board)
        n = len(board[0])

        if board[click[0]][click[1]] == "M":    # if 1st click is a Mine? update at once
            board[click[0]][click[1]] = 'X'
            return board
        
        def countMines(board, i , j):           # function to count adjacent mines
            count = 0
            for di in dirs:
                r = i + di[0]
                c = j + di[1]
                
                if 0 <= r < m and 0 <= c < n and board[r][c] == 'M':    # inbounds and a MINE? count++
                    count += 1
            return count

        q = deque()                             
        q.append([click[0],click[1]])           # push to queue and update to 'Blank'
        board[click[0]][click[1]] = 'B'
        
        

        while q:
            curr = q.popleft()
            count = countMines(board,curr[0],curr[1])
            if count != 0:
                board[curr[0]][curr[1]] = str(count)
            else:
                for di in dirs:
                    r = curr[0] + di[0]
                    c = curr[1] + di[1]
                
                    if 0 <= r < m and 0 <= c < n and board[r][c] == 'E':
                        board[r][c] = 'B'
                        q.append((r,c))
        return board


                
