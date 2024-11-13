import pygame


def main():
    moleX = 0
    moleY = 0
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN(event.pos)
            screen.fill("light green")
            for x in range(1, 20):
                pygame.draw.line(screen, "black", (32*x, 0), (32*x, 512))
            for y in range(1, 16):
                pygame.draw.line(screen, "black", (0, 32*y), (640, 32*y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(moleX, moleY)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
