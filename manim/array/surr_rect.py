from manimlib.imports import *


class SurroundingRect(Scene):

    def construct(self):
        navier_stokes = TexMobject(
            '\\rho',
            '{D',
            '\\textbf{u}',
            '\\over Dt}',
            '=',
            '\\rho',
            '\\left(',
            '{\\partial',
            '\\textbf{u}',
            '\\over \\partial t}',
            '+',
            '\\textbf{u}',
            '\\cdot',
            '\\Delta',
            '\\textbf{u}',
            '\\right)'
        )
        total_derivative = VGroup(navier_stokes[1:4])
        expanded_derivative = VGroup(navier_stokes[6:])

        box1 = SurroundingRectangle(total_derivative)
        box2 = SurroundingRectangle(expanded_derivative)

        box2.set_color(BLUE)

        self.play(Write(navier_stokes))
        self.wait(2)
        self.play(ShowCreation(box1))
        self.wait()
        self.play(
            Transform(box1, box2),
            path_arc = -3.1415,
            run_time = 2
        )
        self.wait(2)
        
