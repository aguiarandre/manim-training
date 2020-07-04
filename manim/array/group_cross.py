from manimlib.imports import *


class GroupCross(Scene):

    def construct(self):

        formula = TexMobject('\\frac{x^2}{2}',
                             '=',
                             '\\int_{-\\infty}^\\infty', 
                             'x',
                             'dx')
        integrand = VGroup(formula[-1], formula[-2])
        cross = Cross(integrand)
        cross.set_stroke(RED, 6)

        self.play(Write(formula))
        self.wait(2)
        self.play(ShowCreation(cross))
        self.wait(2)

