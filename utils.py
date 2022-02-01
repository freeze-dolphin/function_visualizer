import turtle as tt
import math
import random

tt.colormode(255)


class RawExpression:

    def __init__(self, exp: str):
        self.exp = exp
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
        return eval(replace_chain(self.exp).replace("x", str(x)))

def draw_point(x: int, y: int, down: bool):
    if down:
        tt.pendown()
    tt.goto(x, y)


def replace_chain(orig: str) -> str:
    return orig.replace("^", "**").replace("<", "math.sqrt(").replace(">", ")").replace("#", "math.").replace("[", "(").replace("{", "(").replace("]", ")").replace("}", ")").replace("$", "random.")
