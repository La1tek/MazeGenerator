import datetime
import os

def save(maze, rows, cols):
    if not os.path.exists("src/Saves"):
        os.makedirs("src/Saves")
    current_datetime = datetime.datetime.now()
    date_time_str = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"src/Saves/Maze_{date_time_str}.txt"
    with open(file_name, "w") as file:
        s = f"{rows} {cols}\n"
        file.write(s)
        for y, row in enumerate(maze):
            s = ""
            for x, cell in enumerate(row):
                if cell == "1":
                    s += "1"
                else:
                    s += "0"
            s += "\n"
            file.write(s)

def load():
    if not os.path.exists("src/Loader"):
        os.makedirs("src/Loader")
    folder_path = os.getcwd() + "src/Loader"

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            stat = True
            with open(file_path, "r") as file:
                sizes = file.readline().split("\n")[0].split(" ")
                rows, cols = int(sizes[0]), int(sizes[1])
                
                maze = [[0] * (2 * cols + 1) for _ in range(2 * rows + 1)]

                for i in range(2 * rows + 1):
                    row_data = (file.readline().split("\n")[0].split())[0]
                    for j in range(2 * cols + 1):
                        maze[i][j] = list(row_data)[j]
            return [maze, cols, rows]
    return 0



    

