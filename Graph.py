import copy
import numpy as np

# This code called directly from driver takes an input weighted directed graph and solves the min cost problem outputing "Solution" which is a list containing the maped cities

def TSP(Graph,data,n,g,p,Sol):
    for x in range(1, n):
        g[x + 1, ()] = Graph[x][0]

    get_minimum(1, tuple(data[1:]),Graph,g,p)

    #print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    #print(solution[1][0], end=', ')
    Sol.append(solution[1][0])
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                #print(solution[1][0], end=', ')
                Sol.append(solution[1][0])
                break
    #print('1}')
    return Sol


def get_minimum(k, a,Graph,g,p):
    if (k, a) in g:
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a),Graph,g,p)
        values.append(Graph[k-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


def solve(Graph):
    data = np.arange(0,len(Graph))
    data = data+1
    n = len(data)
    g = {}
    p = []
    Solution = []
    return TSP(Graph,data,n,g,p,Solution)

def test():
    matrix = [
        [0, 768, 727],
        [694, 0, 148],
        [693, 134, 0],
    ]
    solution = solve(matrix)
    solution.append(1)
    solution.insert(0,1)
    solution = np.array(solution)
    solution = solution-1
    # Solution is the unmaped path
    # print(solution)

test()
