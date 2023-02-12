# CS4102 Spring 2022 - Unit A Programming
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 3 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google Docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: cjl2pub
# Collaborators:
# Sources: Introduction to Algorithms, Cormen,
# https://www.w3schools.com/python/python_howto_remove_duplicates.asp for duplicate removal tool
#################################
import math
import statistics


class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list containing lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distances
    # and return those values from this method
    #
    # @return the distances between the closest pair and second closest pair
    # with closest at position 0 and second at position 1

    def compute(self, file_data):
        val = []
        cp = ClosestPair()
        file_data.sort(key=lambda x: float(x.split()[0]))
        f = []
        for f1 in file_data:
            f.append([(f1.split()[0]), (f1.split()[1])])
        for i in range(len(file_data)):
            if file_data[i][0] == '-':
                val.append(-float(file_data[i][1: file_data[i].index(" ")]))
            else:
                val.append(float(file_data[i][0: file_data[i].index(" ")]))
        m = statistics.median(val)
        c = cp.calculate(f, m)
        return c[0], c[1]

    def calculate(self, list_x, median):
        cp = ClosestPair()
        closest = 99999999
        second_closest = 99999999
        if len(list_x) < 2:
            return [99999999, 99999999]
        elif len(list_x) == 2:
            return[cp.distance(list_x[0], list_x[1]), cp.distance(list_x[0], list_x[1])]
        # direct comparison/ brute force
        elif 4 >= len(list_x) > 2:
            for x in range(len(list_x)):
                for x2 in range(len(list_x)):
                    if 0.0 < cp.distance(list_x[x], list_x[x2]) < closest:
                        closest = cp.distance(list_x[x], list_x[x2])
                    if second_closest > cp.distance(list_x[x], list_x[x2]) > closest:
                        second_closest = cp.distance(list_x[x], list_x[x2])
            return [closest, second_closest]
        # recursive call
        else:
            left_list = []
            right_list = []
            val = []
            for i in range(len(list_x)):
                val.append(float(list_x[i][0]))
            val.sort()
            m = statistics.median(val)
            # create left and right sublists
            for i in range(len(list_x)):
                if float(list_x[i][0]) < m:
                    left_list.append(list_x[i])
                elif float(list_x[i][0]) > m:
                    right_list.append(list_x[i])
            # recursive call on left and right sublists
            left_cp = cp.calculate(left_list, m)
            right_cp = cp.calculate(right_list, m)
            comb = [left_cp[0], right_cp[0], left_cp[1], right_cp[1]]
            comb.sort()
            min_dist = comb[0]
            second_closest = comb[1]
            new_p = []
            for x in range(len(list_x)):
                if m - min_dist <= float(list_x[x][0]) <= min_dist + m:
                    new_p.append(list_x[x])
            # todo: implement sort by y-coordinate
            run = cp.runway(new_p)
            new_p = []
            for x in range(len(list_x)):
                if m - second_closest <= float(list_x[x][0]) <= second_closest + m:
                    new_p.append(list_x[x])
            run2 = cp.runway(new_p)
            p = [min_dist, second_closest, run[0], run[1], run2[0], run2[1]]
            p.sort()
            p = list(dict.fromkeys(p))
            if len(p) < 2:
                if len(p) < 1:
                    return [99999999, 99999999]
                else:
                    return [p[0], 99999999]
            else:
                return [p[0], p[1]]

    def distance(self, x, y):
        sig_x = max(len(y[0]), len(x[0]))
        sig_y = max(len(y[1]), len(x[1]))
        dist_x = round(float(y[0]) - float(x[0]), sig_x)
        dist_y = round(float(y[1]) - float(x[1]), sig_y)
        return math.hypot(dist_x, dist_y)

    # for a given y list of coordinates within a margin within the smallest of the left
    # and right sublists, find the smallest pair within the runway.
    def runway(self, y_list):
        cp = ClosestPair()
        closest = 99999999
        second_closest = 99999999
        y_list.sort(key=lambda i: float(i[1]))
        if len(y_list) < 8:
            if len(y_list) < 2:
                return [999999, 999999]
            else:
                for y in range(len(y_list)):
                    for y2 in range(len(y_list)):
                        dist = cp.distance(y_list[y], y_list[y2])
                        if 0.0 < dist < closest:
                            closest = dist
                        if second_closest > dist > closest:
                            second_closest = dist
                return [closest, second_closest]
        else:
            for y in range(len(y_list) - 7):
                for y2 in range(7):
                    dist = cp.distance(y_list[y], y_list[y + y2 + 1])
                    if 0 < dist < closest:
                        closest = dist
                    if second_closest > dist > closest:
                        second_closest = dist
            return [closest, second_closest]
