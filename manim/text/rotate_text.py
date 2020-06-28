from manimlib.imports import Scene, TextMobject
PI = 3.1415


class RotateText(Scene):
    def construct(self):
        name = TextMobject('Aldrey')
        self.add(name)
        self.wait()

        for index in range(8):
            name.rotate(PI/4)
            self.wait()