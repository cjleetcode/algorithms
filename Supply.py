# CS4102 Spring 2022 - Unit B Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID:
# Collaborators:
# Sources: Introduction to Algorithms, Cormen
#################################
from DisjSet import DisjSet


class Supply:

    def __init__(self):
        return

    graph = []
    rails = []
    dc = []
    stores = []
    ports = []

    # This is the method that should set off the computation
    # of the supply chain problem.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the total edge-weight sum
    # and return that value from this method
    #
    # @return the total edge-weight sum of a tree that connects nodes as described
    # in the problem statement
    def compute(self, file_data):
        self.organize(file_data)
        #print(self.rails, self.dc, self.stores, self.ports)
        self.construct(file_data)
        #print(self.graph)
        # your function to compute the result should be called here
        return self.kruskal()

    def organize(self, stream):
        s = stream[0].split(' ')
        i = 0
        for n in range(0, int(s[0])):
            s1 = stream[n + 1].split(' ')
            if s1[1] == "port":
                self.ports.append(s1[0])
            elif s1[1] == "rail-hub":
                self.rails.append(s1[0])
            elif s1[1] == "dist-center":
                self.dc.append([s1[0]])
                n += 1
                if n >= int(s[0]):
                    break
                while stream[n + 1].split(' ')[1] == "store" and n < int(s[0]):
                    self.dc[i].append(stream[n  +1].split(' ')[0])
                    n += 1
                i += 1
            elif s1[1] == "store":
                self.stores.append(s1[0])
            else:
                break

    def addNode(self, u, v):
        if v == "port":
            self.ports.append([u, v])
        elif v == "rail-hub":
            self.rails.append([u, v])
        elif v == "dist-center":
            self.dc.append([[u, v]])
        else:
            self.stores.append([u, v])

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def inspect(self, u, v, stream):
        b1 = False
        b2 = False
        u1 = ""
        v1 = ""
        for a in range(len(stream)):
            s1 = stream[a].split(' ')
            if u == s1[0]:
                u1 = s1[1]
                b1 = True
            if v == s1[0]:
                v1 = s1[1]
                b2 = True
            if b1 and b2:
                break
        if (u1 == "store" and v1 == "port") or (u1 == "port" and v1 == "store"):
            return False
        elif (u1 == "rail-hub" and v1 == "store") or (u1 == "store" and v1 == "rail-hub"):
            return False
        elif u1 == "dist-center" and v1 == "dist-center":
            return False
        elif u1 == "dist-center" and v1 == "store":
            for i in range(len(self.dc)):
                if self.dc[i][0] == u:
                    for j in range(len(self.dc[i])):
                        if self.dc[i][j] == v:
                            return True
                    break
            return False
        elif v1 == "dist-center" and u1 == "store":
            for i in range(len(self.dc)):
                if self.dc[i][0] == v:
                    for j in range(len(self.dc[i])):
                        if self.dc[i][j] == u:
                            return True
                    break
            return False
        else:
            return True


    def kruskal(self):
        edges_accepted = 0
        result = []
        ds = []
        #disjoint-data structure parent which houses all of the edges
        parent = []
        parent2 = []
        e = 0
        i = 0
        cost = 0
        s = DisjSet()
        self.graph = sorted(self.graph, key=lambda g: g[2])

        for i1 in self.ports:
            parent.append(i1)
        for i2 in self.rails:
            parent.append(i2)
        for i3 in self.stores:
            parent.append(i3)
        for a1 in self.dc:
            parent.append(a1[0])

        for index in range(len(parent)):
            parent2.append([parent[index], index])
        while e < len(parent2) - 1:
            u = self.graph[i]
            i += 1
            print(parent2)
            x = s.find(parent2, u[0])
            y = s.find(parent2, u[1])
            if not(x == y):
                e = e + 1
                cost += u[2]
                result.append(u)
                s.union(parent2, x, y)
        return cost


    def findNode(self, x):
        return 0

    def construct(self, stream):
        s = stream[0].split(' ')
        for i in range(int(s[0]) + 1, len(stream)):
            t = stream[i].split(' ')
            #check if it is a dirty node or not
            if self.inspect(t[0], t[1], stream):
                self.addEdge(t[0], t[1], int(t[2]))
            else:
                continue

