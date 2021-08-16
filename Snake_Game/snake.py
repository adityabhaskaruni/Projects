import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint
import time

WIDTH = 100
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100


class Snake:
    REVERSE_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, window):
        self.body_list = []
        self._score = 0
        self.timeout = TIMEOUT
        self.game_over = "Game Over!!!"

        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x - i, y))

        self.body_list.append(Body(x, y, 'O'))
        self.window = window
        self.direction = KEY_RIGHT
        self.last_head_pos = (x, y)
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def score(self):
        return 'Score : {}'.format(self._score)

    def add_body(self, body_list):
        self.body_list.extend(body_list)

    def eat_Fruit(self, Fruit):
        Fruit.reset()
        body = Body(self.last_head_pos[0], self.last_head_pos[1])
        self.body_list.insert(-1, body)
        self._score += 10
        self.timeout -= 5
        self.window.timeout(self.timeout)

    @property
    def snake_break(self):
        return any([body.pos == self.dir.pos
                    for body in self.body_list[:-1]])

    def update(self):
        last_body = self.body_list.pop(0)
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)

        self.last_head_pos = (self.dir.x, self.dir.y)
        self.direction_map[self.direction]()

    def change_direction(self, direction):
        if direction != Snake.REVERSE_MAP[self.direction]:
            self.direction = direction

    def render(self):
        for body in self.body_list:
            self.window.addstr(body.y, body.x, body.char)

    @property
    def dir(self):
        return self.body_list[-1]

    @property
    def pos(self):
        return self.dir.x, self.dir.y

    def move_up(self):
        self.dir.y -= 1
        if self.dir.y < 1:
            self.dir.y = MAX_Y

    def move_down(self):
        self.dir.y += 1
        if self.dir.y > MAX_Y:
            self.dir.y = 1

    def move_left(self):
        self.dir.x -= 1
        if self.dir.x < 1:
            self.dir.x = MAX_X

    def move_right(self):
        self.dir.x += 1
        if self.dir.x > MAX_X:
            self.dir.x = 1


class Body:
    def __init__(self, x, y, char='x'):
        self.x = x
        self.y = y
        self.char = char

    @property
    def pos(self):
        return self.x, self.y


class Fruit:
    def __init__(self, window, char='x'):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)


if __name__ == '__main__':
    curses.initscr()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    snake = Snake(SNAKE_X, SNAKE_Y, window)
    Fruit = Fruit(window, '#')

    while True:
        window.clear()
        window.border(0)
        snake.render()
        Fruit.render()
        window.addstr(0, 5, snake.score)
        event = window.getch()

        if event == 27:
            break

        if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
            snake.change_direction(event)

        if snake.dir.x == Fruit.x and snake.dir.y == Fruit.y:
            snake.eat_Fruit(Fruit)

        if event == 32:
            key = -1
            while key != 32:
                key = window.getch()

        snake.update()
        if snake.snake_break:
            break

    curses.endwin()
