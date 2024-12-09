class Board:
    def __init__(self):
        # Initialize the game board, robots, exit, and steps
        self.board = [[" " for _ in range(16)] for _ in range(12)]
        self.robots = []
        self.exit = None
        self.steps = 0



        try:
            # Read and process the map file
            map_file = open("map.txt", "r")


            # Building walls with the board
            row_index = 0
            for line in map_file:
                col_index = 0
                for char in line.strip():
                    if char == "#":
                        self.board[row_index][col_index] = "#"
                    col_index += 1
                row_index += 1
            map_file.close()

            # Read and process the players file
            players_file = open("players.txt", "r")
            for line in players_file:
                parts = line.strip().split()
                row = int(parts[0])
                col = int(parts[1])
                self.robots.append((row, col))
            self.alive = len(self.robots)
            self.escaped = 0
            self.check = len(self.robots)
            players_file.close()

            # Read and process the exit file
            exit_file = open("exit.txt", "r")
            line = exit_file.readline().strip().split()
            self.exit = (int(line[0]), int(line[1]))
            exit_file.close()
        except:
            print("Error reading files.")

    def get_board(self):
        # Create a copy of the current board
        board_copy = [[" " for _ in range(16)] for _ in range(12)]

        # Copy walls and spaces
        for i in range(12):
            for j in range(16):
                if self.board[i][j] == "#":
                    board_copy[i][j] = "#"

        # Place the exit
        if self.exit:
            exit_row, exit_col = self.exit
            board_copy[exit_row][exit_col] = "E"

        # Place the robots
        for robot in self.robots:
            robot_row, robot_col = robot
            board_copy[robot_row][robot_col] = "P"

        return board_copy

    def update(self, direction):
        dx, dy = (0, 0)  # Default movement
        # Movement directions
        if direction == "U":  # Move up
            dx, dy = (-1, 0)
        elif direction == "D":  # Move down
            dx, dy = (1, 0)
        elif direction == "L":  # Move left
            dx, dy = (0, -1)
        elif direction == "R":  # Move right
            dx, dy = (0, 1)

        # Step 1: Calculate intended moves for all robots
        intended_moves = []
        for robot in self.robots:
            x, y = robot
            new_x, new_y = x + dx, y + dy

            # Check boundaries
            if not (0 <= new_x < 12 and 0 <= new_y < 16):
                intended_moves.append((x, y))  # Stay in place
                continue

            # Check for walls
            if self.board[new_x][new_y] == "#":
                self.alive -= 1
                continue

            # Check for exit
            if self.exit == (new_x, new_y):
                self.alive -= 1
                self.escaped += 1
                continue

            # Otherwise, propose a valid move
            intended_moves.append((new_x, new_y))

        # Step 2: Resolve conflicts (robots trying to move to the same position)
        final_positions = []
        for i in range(len(intended_moves)):
            move = intended_moves[i]
            if intended_moves.count(move) > 1:  # Conflict or removal
                final_positions.append(self.robots[i])  # Stay in place
            else:
                final_positions.append(move)  # Valid move

        # Step 3: Update robots list and step count
        self.robots = final_positions
        self.steps += 1

    # Check the current state in the game after evey move
    def get_state(self):
        # There are robots alive
        if (self.escaped == 0 or self.escaped > 0) and self.alive > 0:
            return 0
        # All robots escaped
        elif self.escaped == self.check and self.alive == 0:
            return 1
        # Some died, some escaped
        elif self.escaped > 0 and self.escaped != self.check and self.alive == 0:
            return 3
        else:
            # All died
            return 2

    def save_map(self):
        try:
            with open("save.txt", "w") as save_file:
                # number of alive robots
                save_file.write(f"{self.alive}\n")

                # number of escaped robots
                save_file.write(f"{self.escaped}\n")

                # number of initial robots
                save_file.write(f"{self.check}\n")

                # Save board
                for row in self.board:
                    save_file.write("".join(row) + "\n")

                # Save robots
                for robot in self.robots:
                    save_file.write(f"{robot[0]} {robot[1]}\n")

                # Save exit
                if self.exit:
                    save_file.write(f"{self.exit[0]} {self.exit[1]}\n")

                # Save steps
                save_file.write(f"{self.steps}\n")

        except Exception:
            print("Error saving game state.")

    def load_map(self):
        try:
            save_file = open("save.txt", "r")
            lines = save_file.readlines()


            # Keep track of the number of robots in the save file
            robots_alive = int(lines[0])
            robots_escaped = int(lines[1])
            robots_initial = int(lines[2])

            # Reload board
            self.board = [[" " for _ in range(16)] for _ in range(12)]
            row_index = 3
            for i in range(12):
                for j in range(16):
                    self.board[i][j] = lines[row_index][j]
                row_index += 1

            # Reload robots
            self.robots = []
            for line in lines[15:15+robots_alive]:  # load alive robots
                parts = line.strip().split()
                self.robots.append((int(parts[0]), int(parts[1])))
            self.alive = robots_alive
            self.escaped = robots_escaped
            self.check = robots_initial

            # Reload exit
            exit_line = lines[15 + robots_alive].strip().split()
            self.exit = (int(exit_line[0]), int(exit_line[1]))


            save_file.close()

        except:
            print("Error loading game state.")

    def get_steps(self):
        save_file = open("save.txt", "r")
        lines = save_file.readlines()

        # get the steps from the save file
        robots_alive = int(lines[0])

        self.steps = int(lines[15 + robots_alive + 1])

        save_file.close()

        return self.steps