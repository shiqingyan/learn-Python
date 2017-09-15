#!/usr/bin/env python
import tkinter
top = tkinter.Tk()

hello = tkinter.Label(top, text = 'Hello world!')
hello.pack()

quit = tkinter.Button(top, text = 'Quit', command = top.quit, bg = 'red', fg = 'white')
quit.pack()

tkinter.mainloop()