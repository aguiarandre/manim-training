`Braces` are another object from what are called `shape matchers`. 
You can specify `width_multiplier`, `background_stroke_width`.

```python
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
        
```

After running `manim filename.py -pl`, you'll obtain the following result (which was converted to gif using [this bash script](https://github.com/aguiarandre/manim-training/blob/master/makegif.sh)):
<p align='center'><img src="../previews/braces.gif" width="50%"/> </p>