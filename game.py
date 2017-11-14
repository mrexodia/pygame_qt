import sys, time

import pygame

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

# https://www.pygame.org/docs/tut/PygameIntro.html
class Game():
    def __init__(self):
        pygame.init()
        self.game_init()

    # pygame initialization
    def game_init(self):
        self.size = self.width, self.height = 320, 240
        self.speed = [2, 2]
        self.black = 0, 0, 0

        self.screen = pygame.display.set_mode(self.size)

        self.ball = pygame.image.load("ball.gif")
        self.ballrect = self.ball.get_rect()

    # pygame main loop
    def loop(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        self.ballrect = self.ballrect.move(self.speed)
        if self.ballrect.left < 0 or self.ballrect.right > self.width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 or self.ballrect.bottom > self.height:
            self.speed[1] = -self.speed[1]

        self.screen.fill(self.black)
        self.screen.blit(self.ball, self.ballrect)
        pygame.display.flip()
        return False

# https://pythonspot.com/en/pyqt5-buttons
class Window(QWidget):
    def __init__(self, game):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 200
        self.init_ui()
        self.init_pygame(game)
 
    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton('Do not click', self)
        self.button.setToolTip('Don\'t you dare!')
        self.button.move(100, 70)
        self.button.clicked.connect(self.on_click)

        self.show()

    def init_pygame(self, game):
        # https://stackoverflow.com/questions/46656634/pyqt5-qtimer-count-until-specific-seconds
        self.game = game
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(0)

    def pygame_loop(self):
        if self.game.loop(self):
            self.close()

    def on_click(self):
        self.game.speed[0] = -self.game.speed[0]
        self.game.speed[1] = -self.game.speed[1]
        print('You clicked :\'(')

def main():
    game = Game()
    app = QApplication(sys.argv)
    ex = Window(game)
    result = app.exec_()
    print("Qt finished: " + str(result))
    sys.exit(result)

if __name__ == "__main__":
    main()