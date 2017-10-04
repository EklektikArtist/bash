#!/usr/bin/python

#============================================
# author: Micah Richards
# date: 9/26/17
# class: Python/Pi
#
# purpose: Test button options
# input:  - 
#         - 
# output: - GUI
#	  - 
#
#============================================

# imports
from Tkinter import *     			#Interface to TK widgets

# define global constants and Booleans

# define functions
class Application (Frame):
	def __init__ (self, master=None):
		Frame.__init__(self, master)	# Call parent's class constructor
		self.grid()			# Place self in parent
		self.createWidgets()		# Create all widgets

	def __ck3Handler(self):
		print "ceckbox3 =", self.ck3Var.get()
		self.ck3.flash()

	def createWidgets(self):
		Button(self, bitmap="error").grid(
					 row    	 = 0, 
					 column 	 = 0, 
					 padx   	 = 5
						 )
		Button(self, bitmap="gray75").grid(
					 row   		 = 0, 
					 column		 = 1, 
					 padx   	 = 5
						  )
		Button(self, bitmap="gray50").grid(
					 row   		 = 0, 
					 column		 = 2, 
					 padx  		 = 5
						  )
		self.quitButton= Button (
					 self, 
					 text    	  = "Quit", 
					 bd      	  = 10, 
					 padx    	  = 10, 
					 pady    	  = 20, 
					 activeforeground ='green',
					 activebackground ='white',
					 command  	  = self.quit, 
					 underline	  = 2
					)
		self.quitButton.grid(
				     	 row      	  = 0, 
				    	 column   	  = 20, 
				     	 padx     	  = 5
				    )
		self.ck3LabelVar = StringVar()
		self.ck3LabelVar.set("This is a checkbox")
		self.ck3Var = IntVar()
		self.ck3 = Checkbutton ( self, 
					textvariable	  = self.ck3LabelVar,
					width 		  = 50,
#					font		  = times36,
#					command		  = self.ck3Handler,
					anchor		  = SW,
					activeforeground  = "red",
					activebackground  = "blue",
					indicatoron	  = 0,
					selectcolor	  = "magenta",
					justify		  = RIGHT,
					padx		  = "0.2i",
					pady		  = "0.2i",
					relief		  = SOLID,
					bd		  = 10,
					fg		  = "yellow", 
					bg		  = "cyan",
#					curspr		  = "box_spiral",
					borderwidth	  = 4,
					variable	  = self.ck3Var
				       )
		self.ck3.grid(		
					row 		  = 5, sticky=N+E+S+W
			     )

# ===== Button Main =====

app=Application()				#Instantiate the Application class
app.top = app.winfo_toplevel()
app.top.title("This is my first GUI!")
app.top.geometry("300x200-0-0")
app.top.minsize(350,250)
app.top.maxsize(350,250)
app.mainloop()					# Wait for events

# End of Program
print ('\n-----End of Program-----\n')
