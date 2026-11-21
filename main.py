from display import display_maze
from parsing import config_parser
from maze import Maze, NORTH, SOUTH, EAST, WEST
from characters import Player, Ghost


def main():
    """Generate and display the maze."""

    config = config_parser("config.json")
    maze = Maze(config)
    print(maze.grid)

    print(maze.can_move(0,0,WEST))

    pacman = Player(0,0, maze, config["lives"])

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
    pacman.reset_position()

    print(pacman.same_position(ghost1))

    print(pacman.position())

    ghosts = [ghost1, ghost2, ghost3, ghost4]

    display_maze(maze.grid, pacman, ghosts)

main()
