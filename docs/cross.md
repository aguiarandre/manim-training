One can create a cross symbol onto a VGroup or Mobject using the `Cross` class. Also, you can specify `color` and `width` of the stroke via `.set_stroke(COLOR, WIDTH)` method. See the example below where we create a formula array, and apply a cross symbol on the integrand of the integral equation.


```python
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

```

After running `manim filename.py -pl`, you'll obtain the following result (which was converted to gif using [this bash script](https://github.com/aguiarandre/manim-training/blob/master/makegif.sh)):
<p align='left'><img src="../previews/cross.gif" width="50%"/> </p>