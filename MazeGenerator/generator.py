import argparse
import random

'''
def prs():
    parser = argparse.ArgumentParser(description="Maze Generator")
    parser.add_argument("rows", type=int, help="Number of rows")
    parser.add_argument("cols", type=int, help="Number of columns")
    parser.add_argument("--display", action="store_true", help="Display the maze")
    parser.add_argument("--algorithm", choices=["dfs", "mst"], default="dfs", help="Generation algorithm (dfs/mst)")
    # parser.add_argument("--save", help="Save the maze to a file")
    # parser.add_argument("--load", help="Load the maze from a file")

    args = parser.parse_args()
    if args.display:
        generate(args.cols, args.rows, args.algorithm)
'''
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
                    generate_maze(nx, ny)

        generate_maze(1, 1)

        maze[0][0] = wall
        maze[1][1] = play
        maze[rows - 2][cols - 2] = end

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
        maze[2 * rows][2 * cols] = end
        cols = 2 * cols + 1
        rows = 2 * rows + 1
    return maze
    for row in maze:
        print("".join(row))
    
    Player(maze, play, passage, wall, start, end, rows, cols)
    
def Player(maze, play, passage, wall, start, end, rows, cols):
    i = 1
    j = 1
    while (i != rows - 2 or j != cols - 2):
        shift = input("Введите команду (w - вверх, a - влево, s - вниз, d - вправо): ")
        maze[i][j] = passage
        if (shift == "w" or shift == "a" or shift == "s" or shift == "d"):
            if shift == "w" and maze[i - 1][j] != wall:
                i -= 1
                # Логика для движения вверх
            elif shift == "a" and maze[i][j - 1] != wall:
                j -= 1
                # Логика для движения влево
            elif shift == "s" and maze[i + 1][j] != wall:
                i += 1
                # Логика для движения вниз
            elif shift == "d" and maze[i][j + 1] != wall:
                j += 1
                # Логика для движения вправо
            else:
                print("Движение невозможно. На пути стена.")
        else:
            print("Неправильная команда. Введите w, a, s или d.")
        maze[1][1] = start
        maze[i][j] = play
        # Отображение обновленного лабиринта
        for row in maze:
            print("".join(row))
        print()
    print("You win")



if __name__ == "__main__":
    prs()