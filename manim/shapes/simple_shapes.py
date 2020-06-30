from manimlib.imports import Scene
from manimlib.imports import Circle, Polygon, Square, Rectangle, Annulus


class SimpleShapes(Scene):

    def construct(self):
        
        circle = Circle()
        square = Square()
        triangle = Polygon([-1,0,0], [1,0,0], [0,1,0])
        annulus = Annulus(inner_radius=2.5, outer_radius=3, color='blue')
        rect = Rectangle(height=3, width=8, color='red')

        self.add(circle)
        self.wait()
        self.remove(circle)

        self.add(square)
        self.wait()
        self.remove(square)

        self.add(triangle)
        self.wait()
        self.remove(triangle)

        self.add(rect)
        self.wait()
        self.remove(rect)

        self.add(annulus)
        self.wait()
        self.remove(annulus)

