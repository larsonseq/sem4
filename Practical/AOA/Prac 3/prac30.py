import sys


def min_distance_initialize(distance, sptset, size):
    """This is the Extract min function that returns the smallest nearest vertex u."""
    min_val = sys.maxsize

    min_index = -1
    for i in range(size):
        if distance[i] < min_val and not sptset[i]:
            min_val = distance[i]
            min_index = i 

    return min_index




if __name__ == '__main__':
    """This is the driver code. Stuff starts from here"""
    size = int(input("Enter number of vertices: "))
    cost_matrix = []

    for i in range(size):
        temp = input(f'Enter {i+1} row:')
        cost_matrix.append(list(map(int, temp.split())))

    src = int(input("Enter source Vertes"))
    """Distance is d, pie is the pie and aptset is used to check if a vertex is visited or not"""
    distance = [sys.maxsize] * size
    pie = [-1] * size
    sptset = [False] * size
    distance[src] = 0

    for i in range(size):
        u = min_distance_initialize(distance, sptset, size)
        sptset[u] = True

        for v in range(size):
            if cost_matrix[u][v] > 0 and not sptset[v]:
                if distance[v] > distance[u] + cost_matrix[u][v]:
                    distance[v] = distance[u] + cost_matrix[u][v]
                    pie[v] = u

    print(f"{distance}\n{pie}")

    print("Vertex\t\tDistance from source:")
    for i in range(size):
        print("{}\t\t{}".format(chr(ord('A')+i), distance[i]))