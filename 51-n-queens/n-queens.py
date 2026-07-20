class Solution(object):       
    def solveNQueens(self,n): #function banane ka structure 
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = set()
        diag1 = set()
        diag2 = set() #tracking ke liye kali containers banana
        board = [["."]*n for _ in range (n)] #board banana
        result = [] #ans store karne ki jaga

        def backtrack(row): #iner function(asli logic)
            if row == n:
                result.append(["".join(r) for r in board])
                return #stope condition , base case 
            for col in range(n): #har colum try karna
                if col not in cols and (row - col)not in diag1 and (row + col)not in diag2: #safe hai yaa nhi chack karna
                    board[row][col] = "Q"
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col) #queen place karna
                    backtrack(row + 1) #agli row tr karna 
                    board[row][col]= "."
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)  #undo karna , backtrack

        backtrack(0)
        return result #sba suru karna or and dena

