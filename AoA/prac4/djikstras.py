import sys

# Number of vertices
V = int(input("Enter number of vertices: "))  

# Take input cost matrix from the user
cost_matrix = []
print("Enter cost matrix row-wise:")
for i in range(V):
    row = list(map(int, input().split()))
    cost_matrix.append(row)

# Function to find vertex with min distance
def minDistance(dist, sptSet):
    min_val = sys.maxsize
    min_index = -1

    for i in range(V):
        if dist[i] < min_val and not sptSet[i]:
            min_val = dist[i]
            min_index = i

    return min_index

# Function for printing the path
def printPath(parent, j):
    if parent[j] == -1:
        print(chr(ord('A') + j), end=' ')
        return

    printPath(parent, parent[j])
    print("->", chr(ord('A') + j), end=' ')

# Driver code
src = int(input("Enter source vertex (0-indexed): "))  

dist = [sys.maxsize] * V
parent = [-1] * V
sptSet = [False] * V

dist[src] = 0

for _ in range(V):
    u = minDistance(dist, sptSet)
    sptSet[u] = True

    for v in range(V):
        if cost_matrix[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + cost_matrix[u][v]:
            dist[v] = dist[u] + cost_matrix[u][v]
            parent[v] = u

# Print shortest path
print("Vertex \t\tDistance from Source")  
for i in range(V):
    print("{} \t\t {}".format(chr(ord('A') + i), dist[i]))

# After calculating shortest paths

src = 0  # source vertex

print("\nShortest Paths from source {}:\n".format(chr(ord('A') + src)))

for i in range(V):
    print("To vertex {}:[ ".format(chr(ord('A') + i)), end='')
    printPath(parent, i)
    print("] Distance: {}".format(dist[i]))
    print() 
