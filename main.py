from display import display_maze
from parsing import config_parser
from maze import Maze, NORTH, SOUTH, EAST, WEST
from characters import Player, Ghost
import random


def main():
    """Generate and display the maze."""

    config = config_parser("config.json")
    maze = Maze(config)
    print(maze.grid)

    def generate_pacgum(maze, pacgums, pacman):
        available_cells = []
        corners = [(0, 0),(maze.width - 1, 0),(0,maze.height - 1),(maze.width - 1, maze.height - 1)]

        for y, row in enumerate(maze.grid):
            for x, cell in enumerate(row):
                if cell == 15:
                    continue
                if (x,y) in corners:
                    continue
                if (x,y) == pacman.position():
                    continue
                    
                available_cells.append((x,y))

        if pacgums > len(available_cells):
            number_to_place = len(available_cells)
        else:
            number_to_place = pacgums

        return random.sample(available_cells, number_to_place)

    pacman = Player(0, 0, maze, config["lives"], [], [])
    pacman.reset_position()

    pacgums = generate_pacgum(maze, config["pacgum"], pacman)

    super_pacgums = [
        (0, 0),
        (maze.width - 1, 0),
        (0, maze.height - 1),
        (maze.width - 1, maze.height - 1)
    ]

    pacman.pacgums = pacgums
    pacman.super_pacgums = super_pacgums

    ghost1 = Ghost(0,0, maze)
    ghost2 = Ghost(maze.width - 1, 0, maze)
    ghost3 = Ghost(0,maze.height - 1, maze)
    ghost4 = Ghost(maze.width - 1,maze.height - 1, maze)

    #pacman.move(EAST)

    print()

    print(pacman.position())
    print(ghost1.position())
    print()

    pacman.add_score(20)
    pacman.add_score(15)
    print(pacman.score)

    pacman.lose_life()
    pacman.lose_life()
    print(pacman.lives)

    print(pacman.same_position(ghost1))

    print(pacman.position())

    ghosts = [ghost1, ghost2, ghost3, ghost4]

    #display_maze(maze.grid, pacman, ghosts, pacgums, super_pacgums)

main()
