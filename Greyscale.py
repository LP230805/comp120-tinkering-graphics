import pygame
pygame.init()

main_window = pygame.display.set_mode((800, 600))

my_surface = pygame.image.load('images.jfif').convert()


def make_surface_less_red(surface=pygame.Surface((10, 10))):
    pixel = pygame.Color(255,255,255)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))
            surface.set_at(
                (x, y),
                pygame.Color(int(pixel.b * 0.5) ,pixel.r, pixel.g)
            )


def make_surface_greyscale(surface=pygame.Surface((10, 10))):
    pixel = pygame.Color(255,255,255)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            pixel = surface.get_at((x, y))

            current_red = pixel.r
            current_green = pixel.g
            current_blue = pixel.b

            new_colour_value = (current_red+current_green+current_blue)/3

            surface.set_at(
                (x, y),
                pygame.Color(int(new_colour_value), int(new_colour_value), int(new_colour_value))
            )


make_surface_greyscale(my_surface)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_window.fill((255, 255, 255))
    main_window.blit(my_surface, (0,0))
    pygame.display.update()

pygame.quit()