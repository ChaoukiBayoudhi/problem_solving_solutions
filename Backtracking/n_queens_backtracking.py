class N_Queens_backtracking:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.solutions = []
    def is_Safe(self,L_index,C_index):
        pass
    def solve(self):
        pass
    def printSolution(self):
        pass
#Test

n=int(input('Enter number of queens'))
q=N_Queens_backtracking(n)
q.solve()
q.printSolution()