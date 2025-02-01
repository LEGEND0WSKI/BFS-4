# Time: O(n^2)
# Space:O(n^2)
# Leetcode:Yes
# Issues:initial flag boundary condition  c == -1


from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        arr = [0] * (n*n)       # stores travel and visited

        flag = True

        r = n-1
        c = 0

        for i in range(n*n):
            if board[r][c] == -1:
                arr[i] = board[r][c]
            else:
                arr[i] = board[r][c] - 1
            if flag:                # keep right
                c += 1
                if c == n:          # boundary reached?
                    flag = False    # flip and reset
                    r -= 1
                    c = n-1
            else:
                c -= 1              # keep left
                if c == -1:         # boundary reached?
                    flag = True     # flip and reset
                    r -= 1
                    c = 0

        q = deque()
        q.append(0)
        level = 0
        while q:
            size = len(q)

            for i in range(size):                   # keep popping entire queue
                currIdx = q.popleft()
                for k in range(1,7):                # 6 options
                    newIdx = currIdx + k
                    if newIdx == (n*n)-1 or arr[newIdx] == (n*n)-1: # end reached?
                        return level +1
                    if arr[newIdx] != -2:
                        if arr[newIdx] == -1:
                            q.append(newIdx)
                        else:
                            q.append(arr[newIdx])
                        arr[newIdx] = -2

            level += 1
    
        return -1