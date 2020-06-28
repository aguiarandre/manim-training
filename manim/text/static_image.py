from manimlib.imports import Scene, TextMobject


class StaticImage(Scene):
	'''
	Create a text using a Text Manin Object.
	
	Generate an image by the command:
	manin test.py StaticImage -ps
	'''
	def construct(self):
		text = TextMobject('text')
		self.add(text)