from entities.box import Box

import pygame
import sys

class Game:
    def __init__(self, refreshRate=60):
        pygame.init()
        pygame.display.set_caption("BoxBox")

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 900))
        self.display = pygame.Surface((500, 500), pygame.SRCALPHA)

        self.refreshRate = refreshRate
        self.running = True
        self.dt = 0
        self.box = Box([25], pygame.Vector2(
            self.display.get_width() / 2,
            self.display.get_height() / 2
        ), 150)

        # self.player_size = [25] * 2
        # self.player_pos = pygame.Vector2(
        #     self.display.get_width() / 2,
        #     self.display.get_height() / 2
        # )

        # self.player = pygame.Rect(0, 0, *self.player_size)
        # self.player.center = self.player_pos

        # # px per second (the 'per second' part is vaid when we multiply by dt)
        # self.player_speed = 150

    def run(self):
        while self.running:
            self.box.direction = pygame.Vector2()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.box.direction.x -= 1
            if keys[pygame.K_RIGHT]:
                self.box.direction.x += 1
            if keys[pygame.K_UP]:
                self.box.direction.y -= 1
            if keys[pygame.K_DOWN]:
                self.box.direction.y += 1

            if self.box.direction.length() > 0:
                self.box.direction.normalize_ip()

            self.box.pos += self.box.direction * self.box.speed * self.dt
            self.box.rect.topleft = self.box.pos

            self.display.fill((0, 0, 0, 100))
            pygame.draw.rect(self.display, "green", self.box.rect)

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()),
                (0, 0)
            )
            pygame.display.flip()

            self.dt = self.clock.tick(self.refreshRate) / 1000

Game().run()
