from maze import NORTH, SOUTH, EAST, WEST


class Character:
    def __init__(self, x, y, maze):
        self.x = x
        self.y = y
        self.maze = maze
    
    def move(self, direction):
        if self.maze.can_move(self.x, self.y, direction):
            
            if direction == NORTH:
                self.y -= 1
            if direction == EAST:
                self.x += 1
            if direction == SOUTH:
                self.y += 1
            if direction == WEST:
                self.x -= 1

    def position(self):
        return (self.x, self.y)


class Player(Character):
    def __init__(self, x, y, maze, lives, pacgums, super_pacgums):
        super().__init__(x, y, maze)

        self.score = 0
        self.lives = lives
        self.pacgums = pacgums
        self.super_pacgums = super_pacgums
        self.power_mode = False

    def add_score(self, points):
        self.score += points

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1

    def same_position(self, ghost):
        return self.x == ghost.x and self.y == ghost.y
    
    def reset_position(self):
        if self.maze.height < 14 or self.maze.width < 14:
            self.x = self.maze.width // 2
            self.y = self.maze.height // 2
        else:
            if self.maze.width % 2 != 0:
                self.x = self.maze.width // 2
                self.y = self.maze.height // 2
            else:
                self.x = (self.maze.width - 1) // 2
                self.y = (self.maze.height - 1) // 2

    def pacgums_collection(self, pacgums_points, super_pacgums_points):
        
        if self.position() in self.pacgums:
            self.pacgums.remove(self.position())
            self.add_score(pacgums_points)
        elif self.position() in self.super_pacgums:
            self.super_pacgums.remove(self.position())
            self.add_score(super_pacgums_points)
            self.power_mode = True

    def update_power_mode(self):

        if self.power_mode:
            count_time = time.time() - self.power_mode_start
        if count_time >= 10:
            self.power_mode = False
            self.power_mode_start = None



class Ghost(Character):
    def __init__(self, x, y, maze):
        super().__init__(x, y, maze)
        self.start_x = x
        self.start_y = y

    def reset_position(self):
        self.x = self.start_x
        self.y = self.start_y




 
          
