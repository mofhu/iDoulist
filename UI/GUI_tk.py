# -*- coding: utf-8 -*-
# Author Frank Hu
# iDoulist Function 0 - UI module

from Tkinter import *
import ttk

root = Tk()
root.title("iDoulist")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="iDoulist").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="test grid").grid(column=1, row=2, sticky=E)

root.mainloop()
