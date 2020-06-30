## Shape Motions: Transform behavior

To understand the behavior of the `Transform` class, we'll use the following example:


```python
from manimlib.imports import Scene, TextMobject
from manimlib.imports import Circle, Square, Annulus
from manimlib.imports import FadeIn, FadeOut, GrowFromCenter, ShowCreation
from manimlib.imports import Transform, ReplacementTransform

class MotionShape(Scene):
    '''
    This piece of code demonstrates some morphing of MObjects.

    The most important concept discussed here is about the 
    `Transform` class. Whenever you want to morph a shape into
    another, you should be careful that `Transform` only affects 
    the shape, not the object itself. So, for example, if you 
    morph a Circle into a Square MObject, the circle will still 
    be a circle, however, it will contain the shape of a Square.

    This effectivelly means that after running a 
    `self.play(Transform(circle, square))`
    what will be on the screen will still be the `circle` 
    object, which means that if you want to morph it again, 
    or even fade it out, you should call:
    `self.play(FadeOut(circle))`

    (and not `self.play(FadeOut(square))`)
    '''
    def construct(self):
        
        # Create shapes n objects
        text = TextMobject('Andre')
        circle = Circle()
        square = Square()
        annulus = Annulus(inner_radius=3, outer_radius=3.4)

        # Simple creation of two separate objects
        self.play(GrowFromCenter(circle))
        self.play(FadeOut(circle))
        self.play(ShowCreation(square))
        
        # Morphing square into a circle
        # square will be a Square instance with the shape of a circle.
        self.play(Transform(square, target_mobject=circle))
        self.play(FadeOut(square))
        self.wait()
        
        self.play(FadeIn(circle))
        self.play(Transform(circle, annulus), run_time=2)
        # at this point, circle is still a circle, 
        # with the shape of an annulus
        self.play(Transform(circle, text), run_time=3) 
        self.wait()

``` 
After running `manim filename.py MotionShape -pl`, you'll obtain the following result (which was converted to gif using [this bash script](https://github.com/aguiarandre/manim-training/blob/master/makegif.sh)):
<p align='left'><img src="../previews/motion_shape.gif" width="50%"/> </p>