import pygame
import os

colors = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'blue': (0, 0, 255)
}

class Game:

    SCREEN_SIZE = 600
    IMAGE_SIZE = SCREEN_SIZE / 3 - 50
    X_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('imagens', 'x.png')), (IMAGE_SIZE, IMAGE_SIZE))
    O_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('imagens', 'o.png')), (IMAGE_SIZE, IMAGE_SIZE))

    def _draw_background(self):

        pygame.draw.rect(
            self.screen,
            colors['blue'],
            ((0, 0), (self.SCREEN_SIZE, self.SCREEN_SIZE))
        )

    def __init__(self):
        self.screen = pygame.display.set_mode((
            self.SCREEN_SIZE,
            self.SCREEN_SIZE
        ))

        self.buttons = ()
        self.player_time = 'X'
        self.positions = [
            '', '', '',
            '', '', '',
            '', '', ''
        ]

    def _draw_buttons(self):
        rect_dimensions = (
            self.SCREEN_SIZE / 3,
            self.SCREEN_SIZE / 3
        )
        rect_width = self.SCREEN_SIZE / 3

        #-------------------------------------------------------- 1 linha

        btn_01 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((0, 0), rect_dimensions),
            10
        )

        btn_02 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((rect_width , 0), rect_dimensions),
            10
        )

        btn_03 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((rect_width * 2, 0), rect_dimensions),
            10
        )

        #-------------------------------------------------------- 2 linha

        btn_04 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((0, rect_width), rect_dimensions),
            10
        )

        btn_05 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((rect_width , rect_width), rect_dimensions),
            10
        )

        btn_06 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((rect_width * 2, rect_width), rect_dimensions),
            10
        )

        #-------------------------------------------------------- 3 linha

        btn_07 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((rect_width, rect_width * 2), rect_dimensions),
            10
        )

        btn_08 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((rect_width * 2, rect_width * 2), rect_dimensions),
            10
        )

        btn_09 = pygame.draw.rect(
            self.screen,
            colors['black'],
            ((0, rect_width * 2), rect_dimensions),
            10
        )

        self.buttons = (
            btn_01,
            btn_02,
            btn_03,
            btn_04,
            btn_05,
            btn_06,
            btn_09,
            btn_07,
            btn_08,
        )
    
    @property
    def _images_coordinates(self):

        rect_width = self.SCREEN_SIZE / 3

        return (
            #Linha 1
            (25, 25),
            (rect_width + 25, 25),
            (rect_width * 2 + 25, 25),
            #Linha 2
            (25, rect_width + 25),
            (rect_width + 25, rect_width + 25),
            (rect_width * 2 + 25, rect_width + 25),
            #Linha 3
            (25, rect_width * 2 + 25),
            (rect_width + 25, rect_width * 2 + 25),
            (rect_width * 2 + 25, rect_width * 2 + 25)
        )

    def _draw_positions(self):
        for index, position in enumerate(self.positions):
            if position == 'X':
                self.screen.blit(self.X_IMAGE, self._images_coordinates[index])
            elif position == 'O':
                self.screen.blit(self.O_IMAGE, self._images_coordinates[index])


    def main(self):
        executing = True
        frames_per_seconds = pygame.time.Clock()

        while executing:

            frames_per_seconds.tick(30)
            self._draw_background()
            self._draw_buttons()
            self._draw_positions()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for index, button in enumerate(self.buttons):
                        if button.collidepoint(pygame.mouse.get_pos()):
                            print(f"Teve colisão com o botão: {index}")
                            if self.positions[index] == '':
                                self.positions[index] = self.player_time
                                self.player_time = 'O' if self.player_time == 'X' else 'X'

                                print(self.positions)




tic_tac_toe = Game()

tic_tac_toe.main()