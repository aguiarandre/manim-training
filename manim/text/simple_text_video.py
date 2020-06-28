from manimlib.imports import Scene, TextMobject
from manimlib.imports import Write, GrowFromCenter, FadeOut


class SimpleTextVideo(Scene):
	"""
	https://github.com/3b1b/manim/tree/master/manimlib/animation
	"""
	def construct(self):

		# create a Text Manim Object to write texts
		text = TextMobject('Aldrey')
		
		# create animation and specify its duration 
		# `Write` just simply writes the text, letter by letter, on screen
		self.play(Write(text), run_time=3)
		
		# pause video for N seconds (default=1)
		self.wait(3)

		# FadeOut is an animation to remove the object from screen smoothly
		# check link above to see more animation types
		self.play(FadeOut(text))
		
		text = TextMobject('I love you ')
		self.play(GrowFromCenter(text))
		
		self.wait()
		# remove object text from screen 
		# detail: you have to .wait() after .remove()
		self.remove(text) 
		self.wait()
