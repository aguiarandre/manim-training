from manimlib.imports import *


class DuplicateTransform(Scene):
    
    def construct(self):
        
        formula = TexMobject(
            '(', 'a', '+', 'b', ')^2','=', 
            'a^2', '+ 2 \\times', 'a', 'b', '+', 'b^2'
        )
        formula.set_color_by_tex('a', RED)

        self.play(Write(formula[:6]))

        self.play(
            Transform(formula[1].copy(), formula[6]),
            Transform(formula[3].copy(), formula[-1]),
        )
        self.play(
            Write(formula[7]),
            Write(formula[10]))
        
        self.play(
            Transform(formula[1].copy(), formula[8]),
            Transform(formula[3].copy(), formula[9]),
        )
