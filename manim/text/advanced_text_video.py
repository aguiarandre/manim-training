from manimlib.imports import Scene, TextMobject
from manimlib.imports import Write, GrowFromCenter, FadeOut
from manimlib.imports import Dot
from manimlib.imports import UP, DOWN, LEFT, RIGHT

class AbsolutePosition(Scene):

    def construct(self):
        dot = Dot()
        # Absolute positions:
        
        # move dot
        dot.to_corner(UP + RIGHT)
        
        # add it to screen
        self.add(dot)
        self.wait()

        dot.to_corner(DOWN + LEFT, buff=3)
        self.add(dot)
        self.wait()

        for i in range(5):
            dot.to_corner(DOWN + LEFT, buff=i)
            self.add(dot)
            text = TextMobject(f'dot.to\_corner(text, DOWN + LEFT, buff = {i})')
            self.add(text)
            self.wait()
            self.remove(text)

class RelativePosition(Scene):

    def construct(self):
        
        dot = Dot()
        
        # Create reference object
        reference_text = TextMobject('Reference Text')
        reference_text.move_to(3*LEFT + 3*UP)
        self.add(reference_text)

        reference_text_b = TextMobject('Reference Text')
        reference_text_b.move_to(3*LEFT + 3*DOWN)

        reference_text_c = TextMobject('Reference Text')
        reference_text_c.move_to(3*LEFT)
        self.add(reference_text_b)
        self.add(reference_text_c)

        b_dot = Dot()
        c_dot = Dot()
        self.add(dot)
        self.add(b_dot)
        self.add(c_dot)

        c_dot.move_to(reference_text_c.get_center())

        for i in range(5):
            dot.next_to(reference_text, RIGHT, buff=i)
            b_dot.move_to(reference_text_b.get_center() + i * RIGHT)
            c_dot.shift(RIGHT)
            text = TextMobject(f'dot.next\_to(text, RIGHT, buff = {i})')
            text.move_to(2*UP)

            text_b = TextMobject(f'dot.move\_to(text.get\_center() + {i} * RIGHT)')
            text_b.move_to(2*DOWN)

            text_c = TextMobject(f'dot.shift(RIGHT)')
            text_c.shift(DOWN)

            self.add(text)
            self.add(text_b)
            self.add(text_c)

            self.wait()
            self.remove(text)
            self.remove(text_b)
            self.remove(text_c)
