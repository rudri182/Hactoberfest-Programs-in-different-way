from tkinter import *

class app(Frame):
	def __init__(self, bg = "blue"):
		Frame.__init__(self)
		self.master.title('CALCULATOR')
		self.master.geometry("500x400")
		self.pack(expand = YES, fill =BOTH)
		
		display = StringVar()
		Entry(self, relief=RIDGE, textvariable=display,justify='right').pack(side=TOP,expand=YES, fill=BOTH)

		for clear in (["CLEAR"]):
			erase = self.Calculator(self, TOP)
			self.press(erase, LEFT, clear, lambda obj=display, q=clear: obj.set(''))

 
		for numButton in ("/*-+","()[]", "789","456", "123", "0,."):
			operator_num = self.Calculator(self, TOP)
			for equal in numButton:
				self.press(operator_num, LEFT, equal, lambda obj=display, q=equal: obj.set(obj.get() + q))
 
		EqualButton = self.Calculator(self, TOP)
		for equal in "=":
			if (equal == '='):
				bt_equal = self.press(EqualButton, LEFT, equal)
				bt_equal.bind('<ButtonRelease-1>', lambda e,s=self, obj=display: s.calculation(obj), '+')
			else:
				bt_equal = self.press(EqualButton, LEFT, equal,lambda obj=display, s=' %s ' % equal: obj.set(obj.get() + s))

	def calculation(self, display):
			try:
				display.set(eval(display.get()))
			except:
				display.set("ERROR")

	def Calculator(self,source, side):
		obj = Frame(source, borderwidth=5, bd=5)
		obj.pack(side=side, expand =YES, fill =BOTH)
		return obj

	def press(self,source, side, text, command=None):
		obj = Button(source, text=text, command=command, bg = 'light blue')
		obj.pack(side=side, expand = YES, fill=BOTH)
		return obj

if __name__=='__main__':
 app().mainloop()