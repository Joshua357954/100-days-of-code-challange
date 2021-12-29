from kivy.app import App 
from kivymd.app import MDApp 
from kivy.core.window import Window 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,NumericProperty
from kivy.lang import Builder 

Window.size=(320,520)
kyle='''
MDBoxLayout:
	orientation:"vertical"

	MDToolbar:
		title:"Expresso"
		left_action_items:[['menu',lambda x:x]]

	
	MDLabel:
		text:app.cap
		halign:"center"
		font_style:"H5"




'''


class Name:

	def __init__(self,name):
		self.name=name
		self.surname=name.split(" ")[1]


class MyStuff(MDApp):
	# def __init__(self,*args,**kwargs):
	# 	super().__init__(**kwargs)

	# 	print("Hello")
	naka='joshua boyi'
	nam=Name(naka)
	cap=nam.surname
	
	def build(self):
		return Builder.load_string(kyle)

myapp=MyStuff()
myapp.run()










