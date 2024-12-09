class Board:
    def __init__(self):        # Initialize the game board, robots, exit, and steps
        self.board = [[" " for _ in range(16)] for _ in range(12)]
        self.robots = []
        self.exit = None
        self.steps = 0

        try:
            map_file = open("map.txt", "r")  #create board includes walls
            lines = map_file.readlines()  #get every line on files and save at lines's list
            map_file.close()

            #replace " " to # as a wall in board
            row = 0
            for line in lines: #take every lines in the list
                col = 0
                for char in line: #compare each char in each line and add # to board if char is #
                    if char == "#":
                        self.board[row][col] = "#"
                    col = col + 1
                row = row + 1

            players_file = open("players.txt", "r") #get robot coordinate in file
            for line in players_file:
                line = line.strip()
                index = line.split() #take each value in player file and split into row and column coordinate
                r = int(index[0])
                c = int(index[1])
                self.robots.append((r, c)) #add to robot"s list
                self.alive = len(self.robots)
                self.escaped = 0
                self.initial = len(self.robots)
            players_file.close()


            exit_file = open("exit.txt", "r") #get exit coordinate in file
            for line in exit_file:
                line = line.strip()
                index = line.split() #split each value in text file
                r = int(index[0])
                c = int(index[1])
                self.exit = (r,c) #add value to parameter
            exit_file.close()

        except:
            print("Error reading files.")


    def get_board(self):

        if self.exit: #place exit in board
            self.board[self.exit[0]][self.exit[1]] = "E"

        for row, col in self.robots: #place robots in board
            self.board[row][col] = "P"

        return self.board

    def update(self, direction):
        moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1) } #Updates the positions of the robots based on the given direction

        if direction not in moves:
            return

        dx,dy = moves[direction]
        new_position = []

        for row, col in self.robots:
            new_row = dx + row
            new_col = dy + col

            if 0 <= new_row < 12 and 0<= new_col <16: # Check boundaries
                if self.board[new_row][new_col] == "#":  # Wall collision
                    self.alive -= 1
                    continue
                elif self.board[new_row][new_col] == "E":  #exit
                    self.alive -= 1
                    self.escaped += 1
                    continue
                elif (new_row,new_col) in new_position: # Robot collision
                    continue
                else:
                    new_position.append((new_row,new_col)) #if everything normal, add new position
            else:
                new_position.append((row,col)) # Stay in place if out of bounds

        new_board = [] # create new board
        for row in self.board:
            new_row = [] #create new row
            for cell in row:
                if cell in "E" or cell in "#": #if cell is exit or wall, keep the same
                    new_row.append(cell)
                else:
                    new_row.append(" ") #if not, change to " "
            new_board.append(new_row)
        self.board = new_board  #update new board and replace previous movement of robots with " "

        self.robots = new_position
        self.steps += 1

    def get_state(self):
        if self.escaped == self.initial and self.alive == 0: # if every robot escape successfully and no robot on board, return 1
            return 1
        elif self.escaped >= 0 and self.alive > 0: #if at least 1 robot on board, return 0
            return 0
        elif self.escaped > 0 and self.escaped != self.initial and self.alive == 0: # if there is no more robot on board but the
            return 3                                                              # number of robot escape difference with the total number, return 3
        else:
            return 2

    def save_map(self):
        try:
            save_file = open("save.txt", "w")
            save_file.write(f"{self.alive}\n") #save the number of robots which still on board
            save_file.write(f"{self.escaped}\n") #save the number of robots which already escape exit
            save_file.write(f"{self.initial}\n") #save the number of initial robots
            for row in self.board:
                save_file.write("".join(row) + "\n") #save the board
            for robot in self.robots:
                save_file.write(f"{robot[0]} {robot[1]}\n") #save the position of robots
            if self.exit:
                save_file.write(f"{self.exit[0]} {self.exit[1]}\n") #save the position of exit
            save_file.write(f"{self.steps}\n") #save the number of steps
            save_file.close()

        except:
            print("Error saving game state.")

    def load_map(self):
        try:
            save_file = open("save.txt", "r")
            lines = save_file.readlines()

            robots_alive = 0
            robots_escaped = 0
            robots_initial = 0
            line_row = 0

            for line in lines:
                value = line.strip()
                if line_row == 0: #take the number of robots which still on board
                    robots_alive = value
                elif line_row == 1:  #take the number of robots which already escape exit
                    robots_escaped = value
                elif line_row == 2: #take the number of initial robots
                    robots_initial = value
                line_row += 1

            self.board = [[" " for _ in range(16)] for _ in range(12)] #take the saved board
            row_index = 3
            for i in range(12):
                for j in range(16):
                    self.board[i][j] = lines[row_index][j]
                row_index += 1

            self.robots = []
            for line in lines[15:15 + robots_alive]: # take the saved robots position
                parts = line.strip().split()
                self.robots.append((int(parts[0]), int(parts[1])))
            self.alive = robots_alive
            self.escaped = robots_escaped
            self.initial = robots_initial

            exit_line = lines[-2].strip().split()
            self.exit = (int(exit_line[0]), int(exit_line[1])) #take the saved exit position
            save_file.close()
        except:
            print("Error loading game state")

    def get_steps(self):
        save_file = open("save.txt", "r")
        lines = save_file.readlines()
        self.steps = int(lines[-1]) #take the saved steps
        save_file.close()
        return self.steps











