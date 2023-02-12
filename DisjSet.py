class DisjSet:

    def find(self, parent, i):
        for l in range(len(parent)):
            if parent[l][0] == i:
                if int(parent[l][1]) == l:
                    return i
                return self.find2(parent, parent[int(parent[l][1])])

    def find2(self, parent, i):
        if i[1] == parent[i[1]][1]:
            return i
        return self.find(parent, parent[i])

    def find3(self, parent, i):
        for l in range(len(parent)):
            if parent[l][0] == i:
                if int(parent[l][1]) == l:
                    return l
                return self.find2(parent, parent[int(parent[l][1])])

    def union(self, parent, x, y):
        l1 = self.find3(parent, x)
        l2 = self.find3(parent, y)
        if not(l1 is None) and not(l2 is None):
            parent[l1][1] = l2
        elif not(l1 is None) and l2 is None:
            parent[l1][1] = l1
        elif l1 is None and not(l2 is None):
            parent[l2][1] = l2
        else:
            return
