import pygame

pygame.init()
main_window = pygame.display.set_mode((800, 600))


def mirror_vertical(surface):
    width = surface.get_width()
    height = surface.get_height()
    mirror_point = int(height / 2)
    for x in range(width):
        for y in range(mirror_point):
            top_pixel = surface.get_at((x, y))
            bottom_pixel = surface.get_at((x, height - y - 1))
            surface.set_at((x, y), bottom_pixel)


image = pygame.image.load('images.jfif')
mirror_vertical(image)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        main_window.fill((255, 255, 255))
        main_window.blit(image, (0, 0))
        pygame.display.update()

pygame.quit()
