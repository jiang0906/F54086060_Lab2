import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()
# Create window surface
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (50, 50))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH,HP_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH,HP_HEIGHT))

# set the title
pygame.display.set_caption("My first game")



class Game:
    def __init__(self):
        # window
        # ...(to be done)

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            # draw background
            win.blit(background_image,(0,0))
            pygame.draw.rect(win, (0, 0, 0), [0, 0, 1024, 80])

            # draw enemy and health bar
            pygame.draw.rect(win,RED,[30,260,50,5])
            win.blit(enemy_image,(30,270))
            win.blit(hp_image,(400,0))
            win.blit(hp_image, (440, 0))
            win.blit(hp_image, (480, 0))
            win.blit(hp_image, (520, 0))
            win.blit(hp_image, (560, 0))
            win.blit(hp_image, (400, 40))
            win.blit(hp_image, (440, 40))
            win.blit(hp_gray_image, (480, 40))
            win.blit(hp_gray_image, (520, 40))
            win.blit(hp_gray_image, (560, 40))

            # draw menu (and buttons)
            win.blit(muse_image,(700,0))
            win.blit(sound_image, (780, 0))
            win.blit(continue_image, (860, 0))
            win.blit(pause_image, (940, 0))

            # draw time
            done = False
            clock = pygame.time.Clock()
            font = pygame.font.Font(None, 40)
            frame_count = 0
            frame_rate = 60

            while not done:
                # time loop
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        done = True

                pygame.draw.rect(win, (0, 0, 0), [0, 570, 70, 50])

                total_seconds = frame_count // frame_rate

                minutes = total_seconds // 60

                seconds = total_seconds % 60

                output_string = "{0:2}:{1:02}".format(minutes, seconds)

                text_surface = font.render(output_string, True, WHITE)
                win.blit(text_surface, (0, 575))

                frame_count += 1
                clock.tick(frame_rate)
                pygame.display.update()
            pygame.quit()


if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()

pygame.quit()