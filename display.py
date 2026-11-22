
import pygame

# Colors
CYAN = (0, 255, 255)
GRAY = (50, 50, 50)
BLACK = (0, 0, 0)

# Wall constants
NORTH = 1
EAST = 2
SOUTH = 4
WEST = 8

CELL_SIZE = 100
WALL_SIZE = 5
CHARACTER_SIZE = 50


def display_maze(maze, player, ghosts, pacgums, super_pacgums):
    """Display the maze, Pacman, ghosts and Pac-Gums using Pygame."""
    pygame.init()

    rows = len(maze)
    cols = len(maze[0])

    screen = pygame.display.set_mode(
        (cols * CELL_SIZE, rows * CELL_SIZE)
    )
    pygame.display.set_caption("42 - Pacman Maze")

    # Load Pacman
    pacman_image = pygame.image.load(
        "pacman.png"
    ).convert_alpha()

    pacman_image = pygame.transform.scale(
        pacman_image,
        (CHARACTER_SIZE, CHARACTER_SIZE)
    )

    # Load ghost images
    ghost1_image = pygame.image.load(
        "assets/ghosts/blinky.png"
    ).convert_alpha()

    ghost2_image = pygame.image.load(
        "assets/ghosts/clyde.png"
    ).convert_alpha()

    ghost3_image = pygame.image.load(
        "assets/ghosts/inky.png"
    ).convert_alpha()

    ghost4_image = pygame.image.load(
        "assets/ghosts/pinky.png"
    ).convert_alpha()

    ghost_images = [
        pygame.transform.scale(ghost1_image, (CHARACTER_SIZE, CHARACTER_SIZE)),
        pygame.transform.scale(ghost2_image, (CHARACTER_SIZE, CHARACTER_SIZE)),
        pygame.transform.scale(ghost3_image, (CHARACTER_SIZE, CHARACTER_SIZE)),
        pygame.transform.scale(ghost4_image, (CHARACTER_SIZE, CHARACTER_SIZE))
    ]

    # Load normal Pac-Gum image
    dot_image = pygame.image.load(
        "assets/other/dot.png"
    ).convert_alpha()

    dot_image = pygame.transform.scale(
        dot_image,
        (40, 40)
    )

 # Load Super Pac-Gum image
    super_dot_image = pygame.image.load(
        "assets/other/strawberry.png"
    ).convert_alpha()

    super_dot_image = pygame.transform.scale(
        super_dot_image,
        (40, 40)
    )

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        # Draw maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):

                left = x * CELL_SIZE
                top = y * CELL_SIZE
                right = left + CELL_SIZE
                bottom = top + CELL_SIZE

                # Draw 42 pattern cells
                if cell == 15:
                    pygame.draw.rect(
                        screen,
                        GRAY,
                        (left, top, CELL_SIZE, CELL_SIZE)
                    )

                # Draw walls
                if cell & NORTH:
                    pygame.draw.line(
                        screen, CYAN,
                        (left, top), (right, top), WALL_SIZE
                    )

                if cell & EAST:
                    pygame.draw.line(
                        screen, CYAN,
                        (right, top), (right, bottom), WALL_SIZE
                    )

                if cell & SOUTH:
                    pygame.draw.line(
                        screen, CYAN,
                        (left, bottom), (right, bottom), WALL_SIZE
                    )

                if cell & WEST:
                    pygame.draw.line(
                        screen, CYAN,
                        (left, top), (left, bottom), WALL_SIZE
                    )

        # Draw normal Pac-Gums
        for x, y in pacgums:
            dot_x = x * CELL_SIZE + (CELL_SIZE - dot_image.get_width()) // 2
            dot_y = y * CELL_SIZE + (CELL_SIZE - dot_image.get_height()) // 2

            screen.blit(dot_image, (dot_x, dot_y))

        # Draw Super Pac-Gums
        for x, y in super_pacgums:
            dot_x = x * CELL_SIZE + (CELL_SIZE - super_dot_image.get_width()) // 2
            dot_y = y * CELL_SIZE + (CELL_SIZE - super_dot_image.get_height()) // 2

            screen.blit(super_dot_image, (dot_x, dot_y))

        # Draw Pacman
        pacman_x = player.x * CELL_SIZE
        pacman_y = player.y * CELL_SIZE

        image_x = pacman_x + (CELL_SIZE - CHARACTER_SIZE) // 2
        image_y = pacman_y + (CELL_SIZE - CHARACTER_SIZE) // 2

        screen.blit(pacman_image, (image_x, image_y))

        # Draw ghosts
        for ghost, ghost_image in zip(ghosts, ghost_images):
            ghost_x = ghost.x * CELL_SIZE
            ghost_y = ghost.y * CELL_SIZE

            image_x = ghost_x + (CELL_SIZE - CHARACTER_SIZE) // 2
            image_y = ghost_y + (CELL_SIZE - CHARACTER_SIZE) // 2

            screen.blit(ghost_image, (image_x, image_y))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
