import random
import networkx as nx
import matplotlib.pyplot as mpl

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# class PlotApp:
#     def __init__(self, master):
#         self.master = master
#         self.fig, self.ax = plt.subplots()
#         self.canvas = plt.gcf().canvas
#         self.canvas.mpl_connect('button_press_event', self.on_click)
#         self.btn = tk.Button(master, text='Show Plot', command=self.show_graph)
#         self.btn.pack()

#     def on_click(self, event):
#         print(f'You clicked at ({event.xdata}, {event.ydata})')

#     def show_graph(self):
#         n=int(input('Enter the number of vertices'))
#         m=int(input('Enter the number of colors'))
#         gc=GraphColoring_backtracking(n,m)
#         gc.generate_adjacent_matrix() # non directed graph
#         gc.show_graph()

#         gc.fill_colors()
#         print(gc.colors)
#         gc.solve()
#         if len(gc.result)==0:
#             print('There is no solution')
#         else:
#             print('There are %s possible solutions'%len(gc.result))
#             gc.print_solutions()
#             gc.draw_graph()





class GraphColoring_backtracking:
    def __init__(self,n,m):
        self.n=n #number of vertices
        self.m=m #number of colors
        self.graph=[[0 for i in range(n)] for j in range(n)] #adjacent matrcice
        self.result=[] # list of list of all faisable solution
        self.colors=[]
    def get_edges(self):
        lst_edges=[] # list of edges
        print('n = ',self.n)
        for i in range(self.n):
            for j in range(i):
                if self.graph[i][j]!=0:
                    lst_edges.append((i+1,j+1))
        return lst_edges
    
    def draw_graph(self):
        G = nx.Graph()
        lst_nodes=[i for i in range(1,self.n+1)]
        # Add some nodes
        G.add_nodes_from(lst_nodes)
        edges_list=self.get_edges()
        print('edges list',edges_list)
        # Add some edges
        G.add_edges_from(edges_list)

        # Set the positions of the nodes
        pos = nx.circular_layout(G)

        # Draw the graph
        nx.draw_networkx(G, pos=pos)

        # Color some vertices
        node_colors = self.result[0]
        print('node_colors = ',node_colors)

        nx.draw_networkx_nodes(G, pos=pos, nodelist=lst_nodes, node_color=node_colors)
        
        # Show the plot
        mpl.show()

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
            for i in range(1,self.n):
                nbColumns=random.randint(0,i-1)
                for k in range(nbColumns):
                    j=random.randint(0,i-1)
                    self.graph[i][j]=0
                    self.graph[j][i]=0
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
    def solve(self,possible_solution=[]):
        if len(possible_solution)==self.n:
            self.result.append(possible_solution[:])
        else:
            for i in range(self.m):
                possible_solution.append(self.colors[i])
                if self.is_acceptable_color(possible_solution):
                    self.solve(possible_solution)
                possible_solution.pop()
    def print_solutions(self,):
        for i in range(self.n):
            print(self.result[i],end='\n')
            
    def show_graph(self):
        print ('n =',self.n)
        for i in range(self.n):
            print(self.graph[i],end='\n')
    def int_to_rgba(self,color):
        return tuple(c / 255.0 for c in color)
    #fill the self.Color list, randomly by colors using RGBA
    def fill_colors(self):
        i=0
        while i < self.m:
            rc=random.randint(0,255)
            gc=random.randint(0,255)
            bc=random.randint(0,255)
            color_code = "#" + hex(rc)[2:].zfill(2) + hex(gc)[2:].zfill(2) + hex(bc)[2:].zfill(2)

            
            if color_code not in self.colors:
                self.colors.append(color_code)
                i+=1

#testing
n=int(input('Enter the number of vertices'))
m=int(input('Enter the number of colors'))
gc=GraphColoring_backtracking(n,m)
gc.generate_adjacent_matrix() # non directed graph
gc.show_graph()

gc.fill_colors()
print(gc.colors)
gc.solve()
if len(gc.result)==0:
    print('There is no solution')
else:
    print('There are %s possible solutions'%len(gc.result))
    gc.print_solutions()
    # root = tk.Tk()
    # app = PlotApp(root)
    # root.mainloop()
    gc.draw_graph()

    