import os
import sys

import pygame

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "images")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = os.path.join(IMAGE_DIR, "player.png")

        if os.path.exists(image_path):
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.rect(self.image, (0, 200, 255), self.image.get_rect())

        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Demo de juego con Pygame")
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        all_sprites.update(keys)

        screen.fill((30, 30, 40))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
