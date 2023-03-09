class N_Queens_backtracking:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.solutions = []

    #verify if the queen in [L_index, C_index] in not threatened
    #returns True if the queen is safe, False if not
    # def is_Safe(self,L_index:int,C_index:int)->bool:
    #     #check the line
    #     for i in range(self.n):
    #         if self.board[L_index][i]=='R':
    #             return False
    #     #check the column
    #     for i in range(self.n):
    #         if self.board[i][C_index]=='R':
    #             return False
    #     #check the diagonals
    #     for i in range(self.n):
    #         for j in range(self.n):
    #             if (i+j)==(L_index+C_index) or (i-j)==(L_index-C_index):
    #                 if self.board[i][j]=='R':
    #                     return False
    #     return True

    def is_Safe(self,possible_solution)->bool:
        for i in range(len(possible_solution)-1):
            diff=abs(possible_solution[i]-possible_solution[-1])
            if diff==0 or diff==len(possible_solution)-i-1:
                return False
        return True
    
    def solve(self,possible_solution):
        if len(possible_solution)==self.n:
            #self.solutions.append(possible_solution[:])
            #or
            self.solutions.append(list(possible_solution))
            

        else:    
            for i in range(self.n):
                possible_solution.append(i)
                if self.is_Safe(possible_solution):
                    self.solve(possible_solution)
                possible_solution.pop()
                
    def printSolution(self):
        print(self.solutions)
        print()
        for i in range(len(self.solutions)):
            print(f'Solution {i+1}')
            for j in range(len(self.solutions[i])):
                for k in range(len(self.solutions[i])):
                    if k==self.solutions[i][j]:
                        print('R',end=' ')
                    else:
                        print('0',end=' ')
                print()
            print()
#Test
#Number of pssible solutions :
# N(n) = n! / (1! * (n-1)! ) + (2! * (n-2)! ) + ... + ((n-1)! * 1!) 

n=int(input('Enter number of queens'))
q=N_Queens_backtracking(n)
q.solve([],0)
print('there is ',len(q.solutions),' solutions.')
q.printSolution()



class Chessboard:
    def __init__(self, size, solutions):
        self.size = size
        self.solutions = solutions
        
        self.square_size = 50
        self.board_size = size * self.square_size
        self.colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'cyan', 'magenta', 'brown', 'gray', 'pink']
        
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.board_size, height=self.board_size)
        self.canvas.pack()
        
        self.draw_board()
        self.draw_solutions()
        
        self.root.mainloop()
        
    def draw_board(self):
        for i in range(self.size):
            for j in range(self.size):
                x1 = j * self.square_size
                y1 = i * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                if (i + j) % 2 == 0:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='white')
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='black')
        
    def draw_solutions(self):
        for i, solution in enumerate(self.solutions):
            color = self.colors[i % len(self.colors)]
            for row, col in enumerate(solution):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

# Solve the 8-queens problem
# board_size = 8
# solutions = solve_n_queens(board_size)
n=int(input('Enter number of queens'))
q=N_Queens_backtracking(n)
q.solve([],0)
# Create the chessboard GUI application
chessboard = Chessboard(n, q.solutions)
