import pygame
import sys

from ball import Ball
from bricks import Bricks
from paddle import Paddle

CANVAS = 700, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MichalBricks")
        a = pygame.image.load('icon.ico')
        pygame.display.set_icon(a)

        self.canvas = pygame.display.set_mode(CANVAS)
        self.frame = pygame.time.Clock()
        self.font = pygame.time.Clock()
        self.paddle = Paddle(CANVAS)
        self.ball = Ball(CANVAS)
        self.new_game()
    
    def new_game(self):
        self.paddle_draw = pygame.Rect(self.paddle.position_x, self.paddle.position_y, self.paddle.width,
                                       self.paddle.height)
        self.draw_ball = pygame.Rect(self.ball.position_x, self.paddle.position_y - self.ball.diameter,
                                     self.ball.diameter, self.ball.diameter)
        self.brick = Bricks()
        self.bricks = []
        self.create_brick()
        self.score = 0
        self.lives = 3
        self.LOST = False
        self.WON = False
        self.PLAYING = False

    def create_brick(self):
        row = 40
        for i in range(8):
            column = CANVAS[0] % 2 + 50
            for j in range(10):
                self.bricks.append(pygame.Rect(column, row, self.brick.width, self.brick.height))
                column += self.brick.width + 10
            row += self.brick.height + 10

    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.canvas, self.brick.color, brick)

    def user_input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.paddle_draw.left += 4
            if self.paddle_draw.left > CANVAS[0] - self.paddle.width:
                self.paddle_draw.left = CANVAS[0] - self.paddle.width

        if key[pygame.K_LEFT]:
            self.paddle_draw.left -= 4
            if self.paddle_draw.left < 0:
                self.paddle_draw.left = 0
        if key[pygame.K_SPACE]:
            self.PLAYING = True
        if key[pygame.K_RETURN] and (self.LOST or self.WON):
            self.new_game()

    def move_ball(self):
        self.draw_ball.left += self.ball.velocity[0]
        self.draw_ball.top += self.ball.velocity[1]

        if self.draw_ball.left <= 0:
            self.draw_ball.left = 0
            self.ball.velocity[0] = -self.ball.velocity[0]
        elif self.draw_ball.left >= CANVAS[0] - self.ball.diameter:
            self.draw_ball.left = CANVAS[0] - self.ball.diameter
            self.ball.velocity[0] = -self.ball.velocity[0]

        if self.draw_ball.top <= 0:
            self.draw_ball.top = 0
            self.ball.velocity[1] = - self.ball.velocity[1]
        elif self.draw_ball.top >= CANVAS[1] - self.ball.diameter:
            self.draw_ball.top = CANVAS[1] - self.ball.diameter
            self.ball.velocity[1] = -self.ball.velocity[1]

    def does_it_hit(self):
        for brick in self.bricks:
            if self.draw_ball.colliderect(brick):
                self.ball.velocity[1] = - self.ball.velocity[1]
                self.score += 1
                self.bricks.remove(brick)
        if len(self.bricks) == 0:
            self.WON = True
        if self.draw_ball.colliderect(self.paddle_draw):
            self.ball.velocity[1] = - self.ball.velocity[1]
        elif self.draw_ball.top >= CANVAS[1] - self.ball.diameter:
            self.lives -= 1
            self.PLAYING = False
            if self.lives == 0:
                pygame.mixer.music.stop()
                self.LOST = True

    def game_info(self):
        self.canvas.blit(self.font.render("Points: " + str(self.score) + "  Lives: " + str(self.lives), False, BLACK),
                         (CANVAS[0] / 2 - 100, 8))

    def message(self, text):
        self.canvas.blit(self.font.render(text, False, BLACK),
                         (CANVAS[0] / len(text), CANVAS[1] / 2))

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(-1)
            self.canvas.fill(WHITE)

            # Draw paddle
            pygame.draw.rect(self.canvas, self.paddle.color, self.paddle_draw)

            # Draw ball
            pygame.draw.circle(self.canvas, self.ball.color, (
                self.draw_ball.left + int(self.ball.radius),
                self.draw_ball.top + int(self.ball.radius)),
                               int(self.ball.radius))
            if not self.PLAYING and self.lives != 0:
                self.message("Press space to start the game")
                self.draw_ball.left = self.paddle_draw.left + self.paddle.width / 2
                self.draw_ball.top = self.paddle_draw.top - self.ball.diameter
            if self.PLAYING:
                self.does_it_hit()
                self.move_ball()
            if self.LOST:
                self.message("You lost the Game - Press Enter to start again")
            elif self.WON:
                self.message("You won the Game - Press Enter to start again")

            self.game_info()
            self.user_input()
            self.draw_bricks()
            pygame.display.flip()
            self.frame.tick(40)

if __name__ == "__main__":
    Game().play()