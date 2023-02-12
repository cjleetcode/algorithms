# CS4102 Spring 2022 -- Unit C Programming
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
# Your Computing ID: cjl2pub
# Collaborators: N/A
# Sources: Introduction to Algorithms, Cormen
#################################
import math


class SeamCarving:
    def __init__(self):
        return
    seam = []
    weight = 0.0
    dist = []
    shortest = []
    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    def run(self, image):
        index = 99999999
        self.dist = [[None for j in range(len(image[0]))] for i in range(len(image))]
        self.shortest = [[None for j in range(len(image[0]))] for i in range(len(image))]
        #for j in range(0, len(image)):
            #for i in range(0, len(image[0])):
                #self.dist[j][i] = self.distance(image, j, i)
        for i in range(0, len(image[0])):
            s = self.subSeam(image, len(image) - 1, i)
            #print(s)
            if s[0] < index:
                index = s[0]
                self.seam = s[1]
                self.weight = s[0]
        #for row in self.dist:
            #print(row)
        #for row in self.shortest:
            #print(row)
        return self.weight

    def subSeam(self, image, j, i):
        if j == 0:
            if 0 <= i < len(image[0]):
                if self.dist[j][i] is None:
                    self.dist[j][i] = self.distance(image, j, i)
                if self.shortest[j][i] is None:
                    self.shortest[j][i] = [self.dist[j][i], [i]]
                return [self.dist[j][i], [i]]
            elif i < 0 or i >= len(image[0]):
                return [9999, [i]]
        else:
            if j < 0:
                return [9999, [i]]
            if i < 0:
                return [9999, [i]]
            elif i > len(image[0]) - 1:
                return [9999, [i]]
            else:
                if self.dist[j][i] is None:
                    self.dist[j][i] = self.distance(image, j, i)
                #if j > 0 and i > 0 and self.dist[j - 1][i - 1] is None:
                    #self.dist[j - 1][i - 1] = self.distance(image, j - 1, i - 1)
                #if j > 0 and i < len(image[0]) - 1 and self.dist[j - 1][i + 1] is None:
                    #self.dist[j - 1][i + 1] = self.distance(image, j - 1, i + 1)
                #if 0 <= i < len(image[0]) and j > 0 and self.dist[j - 1][i] is None:
                    #self.dist[j - 1][i] = self.distance(image, j - 1, i)
                if j > 0 and i > 0:
                    if self.shortest[j][i] is not None:
                        left = self.shortest[j - 1][i - 1]
                    else:
                        left = self.subSeam(image, j - 1, i - 1)
                else:
                    left = self.subSeam(image, j - 1, i - 1)
                if j > 0 and i < len(image[0]) - 1:
                    if self.shortest[j][i] is not None:
                        right = self.shortest[j - 1][i + 1]
                    else:
                        right = self.subSeam(image, j - 1, i + 1)
                else:
                    right = self.subSeam(image, j - 1, i + 1)
                if self.shortest[j][i] is not None:
                    middle = self.shortest[j - 1][i]
                else:
                    middle = self.subSeam(image, j - 1, i)
                #if j == 5:
                    #print(left, right, middle, "index", j, i)
                m = min(left[0], right[0], middle[0])
                if m == left[0] and middle[0] != m and right[0] != m:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [left[0] + self.dist[j][i], left[1] + [i]]
                    return [left[0] + self.dist[j][i], left[1] + [i]]
                elif m == right[0] and middle[0] != m and left[0] != m:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [right[0] + self.dist[j][i], right[1] + [i]]
                    return [right[0] + self.dist[j][i], right[1] + [i]]
                elif m == middle[0] and right[0] != m and m != left[0]:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [middle[0] + self.dist[j][i], middle[1] + [i]]
                    return [middle[0] + self.dist[j][i], middle[1] + [i]]
                elif m == left[0] and middle[0] == m and right[0] != m:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [left[0] + self.dist[j][i], left[1] + [i]]
                    return [left[0] + self.dist[j][i], left[1] + [i]]
                elif m == left[0] and right[0] != m and middle[0] == m:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [left[0] + self.dist[j][i], left[1] + [i]]
                    return [left[0] + self.dist[j][i], left[1] + [i]]
                elif m != left[0] and middle[0] == m and right[0] == m:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [middle[0] + self.dist[j][i], middle[1] + [i]]
                    return [middle[0] + self.dist[j][i], middle[1] + [i]]
                else:
                    if self.shortest[j][i] is None:
                        self.shortest[j][i] = [left[0] + self.dist[j][i], left[1] + [i]]
                    return [left[0] + self.dist[j][i], [i] + left[1]]

    def distance(self, image, j, i):
        sumTotal = 0.0
        sums = 0.0
        n = 0
        for y in range(max(j - 1, 0), min(j + 1, len(image) - 1) + 1):
            for x in range(max(i - 1, 0), min(i + 1, len(image[0]) - 1) + 1):
                sums += pow(abs(image[j][i][0] - image[y][x][0]), 2)
                sums += pow(abs(image[j][i][1] - image[y][x][1]), 2)
                sums += pow(abs(image[j][i][2] - image[y][x][2]), 2)
                sumTotal += math.sqrt(sums)
                #print("iteration", y, x, "at", round(sumTotal/math.sqrt(3*pow(255, 2))))
                sums = 0.0
                n += 1
        return sumTotal/(n - 1)
    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.seam

