import turtle as tt
import math
import random

tt.colormode(255)


class RawExpression:

    def replace_chain(self, orig: str) -> str:
        return (orig
                .replace("^", "**")
                .replace("<", "math.sqrt(")
                .replace(">", ")")
                .replace("#", "math.")
                .replace("[", "(")
                .replace("{", "(")
                .replace("]", ")")
                .replace("}", ")")
                .replace("$", "random."))

    def __init__(self, exp: str):
        self.exp = self.replace_chain(exp)
        self.valid = True

    def validate(self, x: float):
        try:
            self.eval(x)
            self.valid = True
        except BaseException:
            self.valid = False

    def is_valid(self) -> bool:
        return self.valid

    def bake(self, x: float, vldr: bool) -> float:
        if vldr:
            self.validate(x)
        if self.is_valid():
            tt.pencolor(0, 0, 0)
            return self.eval(x)
        else:
            tt.pencolor(255, 0, 0)
            return 0

    def eval(self, x) -> float:
        return eval(self.exp)


def draw_point(x: int, y: int, down: bool):
    if down:
        tt.pendown()
    tt.goto(x, y)
