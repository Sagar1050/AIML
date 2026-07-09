from collections import deque

# Social Network Graph
graph = {
    "Alice": ["Charlie", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Alice", "Emma", "Fred"],
    "Emma": ["Bob", "Charlie", "David"],
    "Fred": ["Bob", "David"],
    "Bob": ["Emma", "Fred"]
}


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    print("\n===== BFS Traversal =====")

    while queue:
        print("Queue :", list(queue))
        node = queue.popleft()

        if node == goal:
            break

        for neighbor in sorted(graph[node]):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

        print("Visited:", visited)

    # Construct Path
    path = []
    current = goal
    while current:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nBFS Path:")
    print(" -> ".join(path))


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    print("\n===== DFS Traversal =====")

    while stack:
        print("Stack :", stack)

        node = stack.pop()

        if node not in visited:
            visited.add(node)
            print("Visited:", visited)

            if node == goal:
                break

            # Reverse alphabetical because stack is LIFO
            for neighbor in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    parent[neighbor] = node
                    stack.append(neighbor)

    # Construct Path
    path = []
    current = goal

    while current:
        path.append(current)
        current = parent[current]

    path.reverse()

    print("\nDFS Path:")
    print(" -> ".join(path))


# Driver Code
source = "Alice"
goal = "Bob"

bfs(graph, source, goal)
dfs(graph, source, goal)
