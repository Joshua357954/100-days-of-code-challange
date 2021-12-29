
# Learrn  about arga and kwargs i.e passing undefined arguments to a function 


def people(*args,**kw):
	name=kw.get('name')
	print(type(kw))
	print(type(args))
	print(args)


# people(22,_class="Uni",status='Good')



my_stuffs={
	"coding":"python",
	"phone":"tecno pop 4",
	"laptop":"Hp mini"
}

mas=my_stuffs.get('laptop')
# mas={doing:{'letters':len(stuff)} for doing,stuff in my_stuffs.items() if len(stuff)>6}

# print(mas)








class Label:

	def __init__(self,**kw):

		self.show_text=kw
		print(self.show_text)


lab=Label(text='This is my people of his majesty')


print(lab.show_text.get('text'))







