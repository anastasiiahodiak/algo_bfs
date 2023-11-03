from collections import deque, defaultdict

def read_input():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        root = int(lines[0].strip())
        edges = [line.strip() for line in lines[1:]]
    return root, edges

def find_min_depth(root, edges):
    graph = defaultdict(list)
    for edge in edges:
        parent, child = map(int, edge.split(','))
        graph[parent].append(child)

    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not graph[node]:
            return depth
        queue.extend((child, depth + 1) for child in graph[node])

def main():
    root, edges = read_input()

    min_depth = find_min_depth(root, edges)

    with open('output.txt', 'w') as file:
        file.write(str(min_depth))

if __name__ == "__main__":
    main()