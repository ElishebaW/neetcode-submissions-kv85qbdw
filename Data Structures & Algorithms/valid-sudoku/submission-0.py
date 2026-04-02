class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #maybe use some type of array to keep track
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)] 

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    num = board[r][c]
                    if num in rows[r]:
                        return False
                    
                    if num in cols[c]:
                        return False
                    
                    box_index = (r // 3) * 3 + (c // 3)
                    if num in boxes[box_index]:
                        return False
                    
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)
        
        return True

                






