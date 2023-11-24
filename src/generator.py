import random
import time

def generate(cols, rows, type):
        
    wall = "1"
    passage = "0"
    start = "S"
    end = "E"
    play = "P"

    if type == "DFS": #DFS
        cols = 2 * cols + 1
        rows = 2 * rows + 1
        maze = [[wall for _ in range(cols)] for _ in range(rows)]

        for i in range(cols):
            maze[rows - 1][i] = wall

        for i in range(rows):
            maze[i][cols - 1] = wall

        def generate_maze(x, y):
            maze[y][x] = passage
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx * 2, y + dy * 2
                if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == wall:
                    maze[y + dy][x + dx] = passage
                    time.sleep(0.2)
                    generate_maze(nx, ny)

        generate_maze(1, 1)

        maze[0][0] = wall
        maze[1][1] = play

        for i in range(cols):
            maze[rows - 1][i] = wall

        for i in range(rows):
            maze[i][cols - 1] = wall
    else: #Minimum Spanning Tree
        maze = [[wall] * (2 * cols + 1) for _ in range(2 * rows + 1)]

        def is_valid(x, y):
            return 0 <= x < cols and 0 <= y < rows

        def visit(x, y):
            maze[2 * y][2 * x] = passage

        def connect(x1, y1, x2, y2):
            maze[y1 + y2][x1 + x2] = passage

        # Выбираем случайную точку начала
        stack = [(random.randint(0, cols - 1), random.randint(0, rows - 1))]

        while stack:
            x, y = stack[-1]
            visit(x, y)

            neighbors = []

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and maze[2 * ny][2 * nx] == wall:
                    neighbors.append((dx, dy))

            if neighbors:
                dx, dy = random.choice(neighbors)
                connect(2 * x, 2 * y, dx, dy)
                stack.append((x + dx, y + dy))
            else:
                stack.pop()
        for row in maze:
            row.insert(0, row.pop())
        maze.insert(0, maze.pop())
        maze[1][1] = play
        cols = 2 * cols + 1
        rows = 2 * rows + 1
    return maze
