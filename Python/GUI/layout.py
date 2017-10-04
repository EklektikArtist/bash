#! /usr/bin/env python

#============================================
# author: Micah Richards
# date: 10/3/17
# class: Python/Pi
#
# purpose: Demonstrate the packing tool
# input:  - 
#         - 
# output: - Packed GUI
#	  - 
#
#============================================

# imports
from Tkinter import *

# define global constants and Booleans
window1=Tk()
window1.title('Layout Example using .pack')

window2=Tk()
window2.title('Layout Example using .grid')

window3=Tk()
window3.title('Layout Example using .place')

#   Create four colored labels
lbl_red1=Label (window1, width=30, height=15, bg='red')
lbl_grn1=Label (window1, width=12, height=5, bg='green')
lbl_blu1=Label (window1, width=12, height=5, bg='blue')
lbl_yel1=Label (window1, width=12, height=5, bg='yellow')

lbl_red2=Label (window2, width=30, height=15, bg='red')
lbl_grn2=Label (window2, width=12, height=5, bg='green')
lbl_blu2=Label (window2, width=12, height=5, bg='blue')
lbl_yel2=Label (window2, width=12, height=5, bg='yellow')

lbl_red3=Label (window3, width=30, height=15, bg='red')
lbl_grn3=Label (window3, width=12, height=5, bg='green')
lbl_blu3=Label (window3, width=12, height=5, bg='blue')
lbl_yel3=Label (window3, width=12, height=5, bg='yellow')

#   Add labels to window using 'pack'
lbl_red1.pack(side=TOP)
lbl_grn1.pack(side=BOTTOM)
lbl_blu1.pack(side=LEFT, fill=Y)
lbl_yel1.pack(side=RIGHT)

lbl_red2.grid(row=1, column=1)
lbl_grn2.grid(row=2, column=1)
lbl_blu2.grid(row=3, column=1)
lbl_yel2.grid(row=1, column=4)

lbl_red3.place(x=10, y=10)
lbl_grn3.place(x=36, y=45)
lbl_blu3.place(x=63, y=80)
lbl_yel3.place(x=90, y=115)
# define functions


# ===== Main Program =====
#   add loop to capture window's events
window1.mainloop() 
window2.mainloop()
window3.mainloop()

# End of Program
print ('\n-----End of Program-----\n')
