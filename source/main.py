import pygame as pg
import random as rand
from config import *
from player import PivotSprite
from button import Button


class App:
    def __init__(self, resolution: tuple) -> None:
        # base configs
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.Clock()
        self.font = pg.font.Font(FONT_PATH)

        # player
        self.player = PivotSprite()

        # Buttons
        self.quit_button = Button(
            None, (WIDTH / 2, HEIGHT / 2), "Start", self.font, "#b2b2a4", "#fffd95"
        )

    def check_event(self) -> None:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                if self.quit_button.check_events(self.mouse_pos):
                    pg.quit()
                    quit()

    def update(self) -> None:
        pg.display.flip()
        self.dt = self.clock.tick(FPS) * 0.001

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.quit_button.colorwheel(self.mouse_pos)
        self.quit_button.update(self.screen)

    def run(self) -> None:
        while True:
            self.mouse_pos = pg.mouse.get_pos()
            self.check_event()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App((HEIGHT, WIDTH))
    app.run()
