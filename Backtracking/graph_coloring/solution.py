import random
class GraphColoring_backtracking:
    def __init__(self,n,m):
        self.n=n #number of vertices
        self.m=m #number of colors
        self.graph=[] #adjacent matrcice
        self.result=[] # list of list of all faisable solution
    #get the graph from the keyboard
    #choice =0 =>non directed graph
    def get_adjacent_matrix(self, choice=0):
        if choice == 0:
            for i in range(self.n):
                self.graph[i][i]=0
                for j in range(i):
                    self.graph[i][j]=input('Enter the weight between node %s and node%s '%(i+1,j+1))
                    self.graph[j][i]=self.graph[i][j]
        else:

for i in range(self.n):
                for j in range(self.n):
                    self.graph[i][j]=input('Enter the weight between node %s and node%s '%(i+1,j+1))
                    
    #generate the graph randomly
    def generate_adjacent_matrix(self, choice=0):
        if choice == 0:
            for i in range(self.n):
                self.graph[i][i]=0
                for j in range(i):
                    self.graph[i][j]=random.randint(0,100)
                    self.graph[j][i]=self.graph[i][j]
        else:
            for i in range(self.n):
                for j in range(self.n):
                    self.graph[i][j]=random.randint(0,100)

    def generate_random_adjacent_matrix_numpy(self):
        import numpy as np
        self.graph=np.random.randint(0,100,(self.n,self.n))
        for i in range(self.n):
            self.graph[i][i]=0

    def is_acceptable_color_v1(self,node_index,color,possible_solution ):
        for j in range(self.n):
            if j!=node_index and self.graph[node_index][j]!=0 and possible_solution[node_index][j]==color:
                return False
        return True

    def is_acceptable_color(self,possible_solution ):
        index=len(possible_solution)-1
        for i in range(len(possible_solution)-1):
            if possible_solution[i]==possible_solution[-1] and self.graph[index][i]!=0:
                return False
        return True
    def solve(self,possible_solution):
        if len(possible_solution)==self.n:
            pass
        else:
            pass
    def print_solutions(self,):
        pass

#testing
n=int(input('Enter the number of vertices'))
m=int(input('Enter the number of colors'))
gc=GraphColoring_backtracking(n,m)
gc.generate_adjacent_matrix() # non directed graph
gc.solve()
print('There are %s possible solutions'%len(gc.result))
gc.print_solutions()
    