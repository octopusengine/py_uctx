import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camera = pygame.camera.Camera(pygame.camera.list_cameras()[0])
camera.start()

screen = pygame.display.set_mode((640, 480))

# q to quit
while True:
    image = camera.get_image()
    screen.blit(image, (0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            exit()

camera.stop()
