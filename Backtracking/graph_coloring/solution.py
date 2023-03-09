class GraphColoring_backtracking:
    def __init__(self, colors,n):
        self.n = n
        self.MA = []
        self.colors = colors
        self.result = []
    #self.MA.append(list(map(int, input().split())))

    def get_adjancent_matrix(self,graph_type=0):
        #the graph is non directed
        if graph_type == 0:
            born_sup=i
        else: #the graph is directed
            born_sup=self.n
        for i in range(self.n):
                self.MA[i][i]=0
                for j in range(i+1,born_sup):
                    self.MA[i][j]=input(f'Enter the value of the edge between {i+1} and {j+1} : ')
    def generate_adjancent_matrix(self):
        pass
    def is_acceptable_color
    def solve(self):
        pass