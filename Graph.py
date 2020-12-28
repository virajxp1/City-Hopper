import sys
import copy

matrix = [
    [0, 768,727],
    [694, 0, 148],
    [693, 134, 0],
]

# 1,3,4,2,1
data = [1, 2, 3]

n = len(data)
all_sets = []
g = {}
p = []

def main():
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]

    get_minimum(1, tuple(data[1:]))

    print('\n\nSolution to TSP: {1, ', end='')
    solution = p.pop()
    print(solution[1][0], end=', ')
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0], end=', ')
                break
    print('1}')
    return


def get_minimum(k, a):
    if (k, a) in g:
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()