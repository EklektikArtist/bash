#!/usr/bin/python

#============================================
# author: Micah Richards
# date: 09/21/17
# class: Python/Pi
#
# purpose: demo for sliding scale
# input:  - 
#         - 
# output: - GUI with slider   
#	  - 
#
#============================================

# imports
from Tkinter import *

# define global constants and Booleans

# define functions
class SimpleApplication(Frame):
	def print_value(self, val):
		print "slider now at " + val

	def reset(self):
		self.slider.set(0)

# the constructor
	def __init__(self):
		Frame.__init__(self)
		self.pack()

		self.slider = Scale(self, {"from"    : 0,
					   "to"      : 100,
					   "orient"  : "horizontal",
					   "length"  : "3i",
					   "command" : self.print_value})

		self.reset = Button(self, {"text"    : "reset slider",
					   "command" : self.reset})

		self.done = Button(self,  {"text"    : "QUIT",
					   "fg"      : "red",
					   "command" : self.quit})

		self.slider.pack({"side" : "top"})
		self.reset.pack ({"side" : "top", "fill" : "both"})
		self.done.pack  ({"side" : "top", "fill" : "both"})

# ===== Main Program =====
app = SimpleApplication()
app.mainloop()

# End of Program
print ('\n-----End of Program-----\n')
