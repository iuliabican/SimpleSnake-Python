from texttable import Texttable
import unittest
from unittest import TestCase
from random import randint

class HitWallException(Exception):
    pass

class OneEightyException(Exception):
    pass

class SnakeError(Exception):
    pass

class Snake:
    def __init__(self, apple_count, dir):
        self._dir = dir
        self._apple_count = apple_count
        self._snake = []

    def init_snake(self):
        self._snake = ["*", "+", "+"]

    def update_dir(self, dir):
        self._dir = dir

    def update_apples(self, new_apple):
        if self._apple_count < new_apple:
            for i in range(new_apple - self._apple_count):
                self._snake.append("+")
            self._apple_count = new_apple


class Board:

    def __init__(self, dim, apple_count):
        self._dim = dim
        self._apple_count = apple_count
        self._data = [[" " for i in range(dim)] for j in range(dim)]
        self._snake = []
        self._dir = "up"
        self.init_snake()
        self.place_apples()

    def __str__(self):
        self.table = Texttable()
        self.table.add_rows(self._data, [])
        return self.table.draw()

    def init_snake(self):
        middle = self._dim // 2
        self._data[middle - 1][middle] = "*"
        self._data[middle][middle] = "+"
        self._data[middle + 1][middle] = "+"
        self._snake = [[middle - 1, middle], [middle, middle], [middle + 1, middle]]
        # self._snake.init_snake()
        # self._snake.update_dir("up")

    def check_valid(self, x, y):
        if x < 0 or y < 0 or x > self._dim - 1 or y > self._dim - 1:
            return False
        return True

    def is_free(self, x, y):
        return self._data[x][y] == " "

    def place_apples(self):
        for i in range(self._apple_count):
            ok = False
            while ok is False:
                a = randint(0, self._dim-1)
                b = randint(0, self._dim-1)
                if self.is_free(a, b):
                    if ok is False and self.check_valid(a+1, b) and self.check_valid(a-1, b) and self.check_valid(a, b+1) and\
                            self.check_valid(a, b-1) and self._data[a + 1][b] != "." and self._data[a - 1][b] != "." \
                            and self._data[a][b + 1] != "." and self._data[a][b - 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a+1, b) and self.check_valid(a-1, b) and self.check_valid(a, b+1) and\
                            self._data[a + 1][b] != "." and self._data[a - 1][b] != "." and self._data[a][b + 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a+1, b) and self.check_valid(a-1, b) and self.check_valid(a, b-1) and \
                            self._data[a + 1][b] != "." and self._data[a - 1][b] != "." and self._data[a][b - 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a+1, b) and self.check_valid(a, b+1) and self.check_valid(a, b-1) and \
                            self._data[a + 1][b] != "." and self._data[a][b + 1] != "." and self._data[a][b - 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a-1, b) and self.check_valid(a, b+1) and self.check_valid(a, b-1) and \
                            self._data[a - 1][b] != "." and self._data[a][b + 1] != "." and self._data[a][b - 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a-1, b) and self.check_valid(a, b-1) and \
                            self._data[a - 1][b] != "." and self._data[a][b - 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a-1, b) and self.check_valid(a, b+1) and \
                            self._data[a - 1][b] != "." and self._data[a][b + 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a+1, b) and self.check_valid(a, b-1) and \
                            self._data[a + 1][b] != "." and self._data[a][b - 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                    elif ok is False and self.check_valid(a+1, b) and self.check_valid(a, b+1) and \
                            self._data[a + 1][b] != "." and self._data[a][b + 1] != ".":
                        self._data[a][b] = "."
                        ok = True
                # print(self)
                # print("\n")

    def place_one_apple(self):
        ok = False
        while ok is False:
            a = randint(0, self._dim-1)
            b = randint(0, self._dim-1)
            if self.is_free(a, b):
                if ok is False and self.check_valid(a + 1, b) and self.check_valid(a - 1, b) and self.check_valid(a,
                                                                                                                  b + 1) and \
                        self.check_valid(a, b - 1) and self._data[a + 1][b] != "." and self._data[a - 1][b] != "." \
                        and self._data[a][b + 1] != "." and self._data[a][b - 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a + 1, b) and self.check_valid(a - 1, b) and self.check_valid(a,
                                                                                                                  b + 1) and \
                        self._data[a + 1][b] != "." and self._data[a - 1][b] != "." and self._data[a][b + 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a + 1, b) and self.check_valid(a - 1, b) and self.check_valid(a,
                                                                                                                  b - 1) and \
                        self._data[a + 1][b] != "." and self._data[a - 1][b] != "." and self._data[a][b - 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a + 1, b) and self.check_valid(a, b + 1) and self.check_valid(a,
                                                                                                                  b - 1) and \
                        self._data[a + 1][b] != "." and self._data[a][b + 1] != "." and self._data[a][b - 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a - 1, b) and self.check_valid(a, b + 1) and self.check_valid(a,
                                                                                                                  b - 1) and \
                        self._data[a - 1][b] != "." and self._data[a][b + 1] != "." and self._data[a][b - 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a - 1, b) and self.check_valid(a, b - 1) and \
                        self._data[a - 1][b] != "." and self._data[a][b - 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a - 1, b) and self.check_valid(a, b + 1) and \
                        self._data[a - 1][b] != "." and self._data[a][b + 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a + 1, b) and self.check_valid(a, b - 1) and \
                        self._data[a + 1][b] != "." and self._data[a][b - 1] != ".":
                    self._data[a][b] = "."
                    ok = True
                elif ok is False and self.check_valid(a + 1, b) and self.check_valid(a, b + 1) and \
                        self._data[a + 1][b] != "." and self._data[a][b + 1] != ".":
                    self._data[a][b] = "."
                    ok = True

    def is_apple(self, x, y):
        return self._data[x][y] == "."

    def get_direction(self):
        return self._dir

    def set_direction(self, newdir):
        self._dir = newdir

    def get_head_snake(self):
        return self._snake[0]

    def check_snake(self, x, y):
        return self._data[x][y] == "+"

    def move(self, n):
        direction = self.get_direction()
        head = self.get_head_snake()
        row = head[0]
        column = head[1]
        if direction == "up":
            for i in range(n):
                row = row - 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row + 1][column] = "+"
                else:
                    raise HitWallException("You hit a wall. Game Over!")
        elif direction == "right":
            for i in range(n):
                column = column + 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row][column - 1] = "+"
                else:
                    raise HitWallException("You hit a wall. Game Over!")
        elif direction == "down":
            for i in range(n):
                row = row + 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row - 1][column] = "+"
                else:
                    raise HitWallException("You hit a wall. Game Over!")
        elif direction == "left":
            for i in range(n):
                column = column - 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row][column + 1] = "+"
                else:
                    raise HitWallException("You hit a wall. Game Over!")

    def change_direction(self, dir):
        direction = self.get_direction()
        head = self.get_head_snake()
        row = head[0]
        column = head[1]
        if direction == "up" and dir == "down":
            raise OneEightyException("Can't go 180 back!")
        elif direction == "down" and dir == "up":
            raise OneEightyException("Can't go 180 back!")
        elif direction == "left" and dir == "right":
            raise OneEightyException("Can't go 180 back!")
        elif direction == "right" and dir == "left":
            raise OneEightyException("Can't go 180 back!")
        elif direction == dir:
            pass
        else:
            if dir == "up":
                row = row - 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row + 1][column] = "+"
                        self._dir = dir
                else:
                    raise HitWallException("You hit a wall. Game Over!")
            elif dir == "right":
                column = column + 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row][column - 1] = "+"
                        self._dir = dir
                else:
                    raise HitWallException("You hit a wall. Game Over!")
            elif dir == "down":
                row = row + 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row - 1][column] = "+"
                        self._dir = dir
                else:
                    raise HitWallException("You hit a wall. Game Over!")
            elif dir == "left":
                column = column - 1
                if self.check_valid(row, column):
                    if self.check_snake(row, column):
                        raise SnakeError("Hit snake! Game over!")
                    else:
                        if self.is_apple(row, column) is False:
                            last = self._snake.pop()
                            self._data[last[0]][last[1]] = " "
                        elif self.is_apple(row, column):
                            self.place_one_apple()
                        self._snake.insert(0, [row, column])
                        self._data[row][column] = "*"
                        self._data[row][column + 1] = "+"
                        self._dir = dir
                else:
                    raise HitWallException("You hit a wall. Game Over!")

    def check_apple(self, row, column):
        pass
