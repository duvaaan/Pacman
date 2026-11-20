
import mazegenerator

NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

class Maze:
    """Manage maze generation and maze data."""

    def __init__(self, config):
        self.width = config["width"]
        self.height = config["height"]

        self.generator = mazegenerator.MazeGenerator(
            size=(self.width, self.height),
            perfect=False,
            seed=config["seed"]
        )

        self.grid = self.generator.maze
    
    def can_move(self, x, y, direction):
        """Check if movement is possible."""
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return False
        
        if direction == NORTH:
            return not (self.grid[y][x] & NORTH)
        if direction == EAST:
            return not (self.grid[y][x] & EAST)
        if direction == SOUTH:
            return not (self.grid[y][x] & SOUTH)
        if direction == WEST:
            return not (self.grid[y][x] & WEST)
        
        return False


        

