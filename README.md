<h1 align='center'>:boom: manim-training :boom:</h1>

<p align='center'> Training manim-lib. An interface to develop high quality visualizations, specially for teaching.</p>
<p align='center'><img src="/preview/rotation.gif" width="50%"/> </p>


# Screenshots 


> TODO

# Usage

> TODO

# Documentation: Sample Codes

## Simple static image

To create a simple static image of a text, just create a class, inherit from the `Scene` class and define a `construct` method.

```python
from manimlib.imports import Scene, TextMobject


class StaticImage(Scene):
	'''Create a text using a Text Manin Object.'''
	def construct(self):
		text = TextMobject('text')
		self.add(text)
``` 
After running `manim filename.py StaticImage -ps`, you'll obtain the following result:
<p align='center'><img src="/preview/text." width="50%"/> </p>



# References

> TODO
