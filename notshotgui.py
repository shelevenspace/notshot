# notShot (c) 2025 by shelevenspace
# This source code is licensed under the CC BY-NC-SA 4.0 with Source Code Clarifications. Review the LICENSE.txt for details.

from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont

def guiver():
    return "1.0.0"

def nscheck():
    try:
        global notshot
        import notshot
        headless = False # notShot is the "head"
    except Exception:
        headless = True
    return headless

def argsprep(v, s, n, q, a, dry, oldname, f, o): # drop all the args into an array to relay to notShot
    passedargs[0] = v
    passedargs[1] = s
    passedargs[2] = n
    passedargs[3] = q
    passedargs[4] = a
    passedargs[5] = dry
    passedargs[6] = oldname
    passedargs[7] = f
    passedargs[8] = o
    notshot.capture(passedargs)

def mainwindow():
    global passedargs
    passedargs = [False] * 9 # python is zero-inclusive

    # prepare core window
    mw = Tk() # main window
    mw.resizable(width=False, height=False)
    ttk.Style().theme_use("alt")
    defaultfont = tkFont.nametofont("TkDefaultFont")
    defaultfont.configure(size=11)
    mw.option_add("*Font", defaultfont)
    mw.title(f"notShot-gui")

    # inner frame that elements attach to
    mf = ttk.Frame(mw, padding=3) # main frame
    mf.grid(column=0, row=0, sticky=(N, W, E, S))

    # initialize variables
    varverbose = BooleanVar()
    varnostruct = BooleanVar()
    varseeimage = BooleanVar()
    varquiet = BooleanVar()
    varactive = BooleanVar()
    vardry = BooleanVar()
    varoldname = BooleanVar()
    optformat = ["png", "dds", "eps", "gif", "jpeg", "jpeg2000", "pdf", "ppm", "sgi", "tga", "tiff", "webp", "icns"]
    optoutput = ["~/Pictures/", "~/Desktop/", "~/Documents/", "~/"]

    # contents of gui aligned on a grid
    ttk.Label(mf, text=f"notShot GUI {guiver()}").grid(column=1, row=1, columnspan=2)
    
    ttk.Label(mf, text=f" ").grid(column=1, row=2, columnspan=2) # blank space
    
    ctrlverbose = ttk.Checkbutton(mf, text="Verbose (unavailable in gui)", variable=varverbose, onvalue=True, offvalue=False, state=DISABLED)
    ctrlverbose.grid(column=1, row=4, columnspan=2, sticky="e, w")
        
    ctrlseeimage = ttk.Checkbutton(mf, text="See Image", variable=varseeimage, onvalue=True, offvalue=False)
    ctrlseeimage.grid(column=1, row=5, columnspan=2, sticky="e, w")

    ctrlnostruct = ttk.Checkbutton(mf, text="No Structure", variable=varnostruct, onvalue=True, offvalue=False)
    ctrlnostruct.grid(column=1, row=6, columnspan=2, sticky="e, w")

    ctrlquiet = ttk.Checkbutton(mf, text="Quiet", variable=varquiet, onvalue=True, offvalue=False)
    ctrlquiet.grid(column=1, row=7, columnspan=2, sticky="e, w")
    
    ctrlactive = ttk.Checkbutton(mf, text="Active (unavailable in gui)", variable=varactive, onvalue=True, offvalue=False, state=DISABLED)
    ctrlactive.grid(column=1, row=8, columnspan=2, sticky="e, w")
    
    ctrldry = ttk.Checkbutton(mf, text="Dry Run", variable=vardry, onvalue=True, offvalue=False)
    ctrldry.grid(column=1, row=9, columnspan=2, sticky="e, w")
    
    ctrloldname = ttk.Checkbutton(mf, text="v1.2 naming scheme", variable=varoldname, onvalue=True, offvalue=False)
    ctrloldname.grid(column=1, row=10, columnspan=2, sticky="e, w")
    
    ttk.Label(mf, text="Format:").grid(column=1, row=11, sticky="w")
    ctrlformat = ttk.Combobox(mf, height=6, values=optformat)
    ctrlformat.grid(column=2, row=11, sticky="e")
    ctrlformat.set(optformat[0]) # put "png" into the dropdown
    # ctrlformat.bind("<<ComboboxSelected>>", )
    
    ttk.Label(mf, text="Output dir:").grid(column=1, row=12, sticky="w")
    ctrloutput = ttk.Combobox(mf, height=6, values=optoutput)
    ctrloutput.grid(column=2, row=12, sticky="e")
    ctrloutput.set(optoutput[0]) # put "~/Pictures/" into the textbox
    # ctrloutput.bind("<<ComboboxSelected>>", )
    
    # ttk.Label(mf, text="Arguments: ").grid(column=1, row=13, sticky="w") # sticky=w is freaky justify=left
    # ctrlargs = ttk.Label(mf, text="test") # justify=left not necessary due to sticky=w
    # ctrlargs.grid(column=2, row=13, sticky="e")
    
    ttk.Label(mf, text=f" ").grid(column=1, row=14, columnspan=2) # blank space
    
    # ctrlconsole = ttk.Label(mf, text=varconsole)
    # ctrlconsole.grid(column=1, row=15, columnspan=2, sticky="e, w")
    
    capturebutton = ttk.Button(mf, text="Capture", command=lambda: argsprep(varverbose.get(), varnostruct.get(), varseeimage.get(), varquiet.get(), varactive.get(), vardry.get(), varoldname.get(), ctrlformat.get(), ctrloutput.get())) # collect all the settings and pass them
    capturebutton.grid(column=1, row=16, columnspan=2, sticky="n, e, s, w")
    # mw.bind("<Key-Return>", capturebutton) # doesn't work - TypeError: 'Button' object is not callable

    if nscheck():
        capturebutton.config(state=DISABLED, text="notShot is missing!")

    mw.mainloop()

if __name__ == "__main__": # this is True if you're running notshotgui directly, which should always be the case...
    mainwindow()