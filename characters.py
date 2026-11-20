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
    def __init__(self, x, y, maze, lives):
        super().__init__(x, y, maze)

        self.score = 0
        self.lives = lives

    def add_score(self, points):
        self.score += points

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1

    # def same_position(self, ghost):
    #     return self.x == ghost.x and self.y == ghost.y
    


class Ghost(Character):
    def __init__(self, x, y, maze):
       super().__init__(x, y, maze)





 
          