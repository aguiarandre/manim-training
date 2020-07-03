from manimlib.imports import Scene, TexMobject, VGroup, Write
from manimlib.imports import BLUE, RED, GREEN, ORANGE, YELLOW, PINK


class GroupedArray(Scene):

    def construct(self):
        
        formula = TexMobject('\int_{',
                ' -\infty}',
                '^\infty', 
                'sec x', 
                'dx', 
                '=', 
                'ln(sec x + tan x)', 
                '+',
                'c')
        
        integral = VGroup(formula[0], formula[1], formula[2])
        integrand = VGroup(formula[3], formula[4])
        equal = formula[5]
        results = VGroup(formula[6], formula[7], formula[8])
        
        integral.set_color(RED)
        integrand.set_color(BLUE)
        equal.set_color(PINK)
        results.set_color(ORANGE)
        
        self.play(Write(formula))
        
