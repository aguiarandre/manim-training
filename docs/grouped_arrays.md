As we've seen, `TexMobject`s are represented as arrays in memory. 

One can use this to group up elements using `VGroup` and specify characteristics to each group (color, size, etc).

See the example below:

```python

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
```

After running `manim filename.py GroupedArray -pl`, you'll obtain the following result (which was converted to gif using [this bash script](https://github.com/aguiarandre/manim-training/blob/master/makegif.sh)):
<p align='left'><img src="../previews/grouped_array.gif" width="50%"/> </p>