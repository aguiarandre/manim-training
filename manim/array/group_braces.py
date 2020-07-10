from manimlib.imports import *


class BraceGroup(Scene):
    def construct(self):
        formula = TexMobject('\\lim_{x \\to \\infty}',
                             '{1 \\over',
                             'x}')

        fraction = VGroup(formula[1], formula[2])
        
        # denominator tends to infinity.
        
        braces = Brace(formula, direction=DOWN)
        text_bottom = braces.get_text('When $x \\to \\infty$')

        braces_top = Brace(fraction, direction=UP)
        text_top = braces_top.get_text('$1/x \\to 0$')

        self.play(Write(formula))
        self.wait()
        self.play(ShowCreation(braces))
        self.play(Write(text_bottom))
        self.wait()
        self.play(ShowCreation(braces_top))
        self.play(Write(text_top))
        
        
