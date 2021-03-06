import random

from Food import Food
from Snake import Snake


class GameField():
    def __init__(self, left_edge, right_edge, top_edge, bot_edge):
        self.__left_edge = left_edge
        self.__right_edge = right_edge
        self.__top_edge = top_edge
        self.__bot_edge = bot_edge

        self.__snake = None
        self.__food = None
        self.__score = 0
    
    @property
    def left_edge(self):
        return self.__left_edge

    @property
    def right_edge(self):
        return self.__right_edge

    @property
    def top_edge(self):
        return self.__top_edge

    @property
    def bot_edge(self):
        return self.__bot_edge

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def snake(self):
        return self.__snake
    
    @property
    def food(self):
        return self.__food

    def add_snake(self):
        if self.__snake is None:
            x = self.__right_edge // 2
            y = self.__bot_edge // 2

            self.__snake = Snake(x, y, self)

        return self.__snake

    def add_food(self, score):
        if self.__food is None:
            x = y = 0
            while True:
                x = random.randint(self.__left_edge, self.__right_edge - 1)
                y = random.randint(self.__top_edge, self.__bot_edge - 1)

                if (x, y) not in self.__snake:
                    break
            
            self.__food = Food(x, y, score)

    def delete_food(self):
        del self.__food
        self.__food = None

    def delete_snake(self):
        del self.__snake
        self.__snake = None

    def lose_points(self):
        self.__score = 0

    def reset_game(self):
        self.lose_points()
        self.delete_snake()
        self.delete_food()
