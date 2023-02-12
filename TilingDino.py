# CS4102 Spring 2022 -- Unit D Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: 
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
import matplotlib.pyplot
import networkx
import matplotlib.pyplot as plt

class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    dx = networkx.Graph()
    solution = []
    def compute(self, lines):
        counter = 0
        for row in range(len(lines)):
            for c in range(len(lines[0])):
                if lines[row][c] == '#':
                    counter += 1
                    self.adjacent(lines, row, c)
        s = [n for n in networkx.connected_components(self.dx)]
        #check if node count is odd or if there is a subgrph that has odd nodes, if so return impossible
        for n2 in s:
            if len(n2) % 2 == 1:
                return ["impossible"]
        if counter % 2 == 1:
            return ["impossible"]
        a = self.calculate()
        return self.solution

    def adjacent(self, lines, r, c):
        if r == len(lines) - 1:
            if c != len(lines[0]) and lines[r][c + 1] == '#':
                self.dx.add_edge(str(c) + " " + str(r), str(c + 1) + " " + str(r))
        else:
            if c == 0:
                if lines[r + 1][c] == '#':
                    self.dx.add_edge(str(c) + " " + str(r), str(c) + " " + str(r + 1))
                if lines[r][c + 1] == '#':
                    self.dx.add_edge(str(c) + " " + str(r), str(c + 1) + " " + str(r))
            elif c == len(lines[0]) - 1:
                if lines[r + 1][c] == '#':
                    self.dx.add_edge(str(c) + " " + str(r), str(c) + " " + str(r + 1))
            else:
                if lines[r + 1][c] == '#':
                    self.dx.add_edge(str(c) + " " + str(r), str(c) + " " + str(r + 1))
                if lines[r][c + 1] == '#':
                    self.dx.add_edge(str(c) + " " + str(r), str(c + 1) + " " + str(r))

    def calculate(self):
        nodes = list(networkx.nodes(self.dx))
        for n in nodes:
            graph = self.dx
            no = graph.neighbors(n)
            gen = list(no)
            for g in gen:
                s = self.subCalculate(n, g, graph)
                if s:
                    self.solution.append(n + " " + g)
                    return
                else:
                    continue
        self.solution = ['impossible']
        return

    def subCalculate(self, n, n2, g):
        g.remove_edge(n, n2)
        g.remove_node(n)
        g.remove_node(n2)
        s1 = [x for x in networkx.connected_components(g)]
        # check if node count is odd or if there is a subgrph that has odd nodes, if so return impossible
        for x in s1:
            if len(x) % 2 == 1:
                return False
        nodes = list(networkx.nodes(g))
        if len(nodes) == 0:
            return True
        for n1 in nodes:
            gen = [no for no in g.neighbors(n1)]
            graph = g
            for g1 in gen:
                s = self.subCalculate(n1, g1, graph)
                if s:
                    s1 = n1 + " " + g1
                    self.solution.append(s1)
                    return True
                else:
                    break
        return False
