You can use the concepts of [Transform](https://github.com/aguiarandre/manim-training/blob/master/docs/shape_motions.md) to create a replica of a `Mobject`. 

In the following example, we both set color by the name of the text and then apply a Transformation on a `.copy()` of an object. If you `self.play()` a transformation between an `object.copy()` and a `transformed_object`, the `object` will be replicated and this replica will be transformed into the `transformed_object`.

```python
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
```
After running `manim filename.py -pl`, you'll obtain the following result (which was converted to gif using [this bash script](https://github.com/aguiarandre/manim-training/blob/master/makegif.sh)):
<p align='center'><img src="../previews/dup_transf.gif" width="50%"/> </p>