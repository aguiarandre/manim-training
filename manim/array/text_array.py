from manimlib.imports import Scene, TextMobject, TexMobject
from manimlib.imports import BLUE, RED, GREEN, ORANGE, YELLOW, PINK

class Array(Scene):

    def construct(self):
        # This syntax leads to an array
        text = TextMobject('a','b', 'c', 'd')

        self.add(text)
        self.wait(2)

        text[0].set_color(BLUE)
        text[1].set_color(BLUE)
        text[2].set_color(RED)
        text[3].set_color('#6fbf8a')

        self.add(text)
        self.wait(2)

        #NOTE that here we're using TexMobject and not TextMobject 
        # (mind the t)

        formula = TexMobject('x','=','{a', '\\over','b}')
        formula[0].set_color(RED)
        formula[1].set_color(BLUE)
        formula[2].set_color(PINK)
        formula[3].set_color(YELLOW)
        formula[4].set_color(ORANGE)

        self.remove(text)
        self.add(formula)
        self.wait(2)
        