import argparse

def main():
    parser = argparse.ArgumentParser(description="Maze Generator")
    parser.add_argument("rows", type=int, help="Number of rows")
    parser.add_argument("cols", type=int, help="Number of columns")
    parser.add_argument("--display", action="store_true", help="Display the maze")
    # parser.add_argument("--save", help="Save the maze to a file")
    # parser.add_argument("--load", help="Load the maze from a file")

    args = parser.parse_args()
    
    if args.display:
        print(args.rows, args.cols)

    


if __name__ == "__main__":
    main()