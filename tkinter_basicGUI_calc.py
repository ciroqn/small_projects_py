try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
# add x padding
mainWindow['padx'] = 8

# loop through to create Button keys
keys = [[('C', 1), ('CE', 2)],
        [('7', 1), ('8', 2), ('9', 3), ('+', 4)],
        [('4', 1), ('5', 2), ('6', 3), ('-', 4)],
        [('1', 1), ('2', 2), ('3', 3), ('*', 4)],
        [('0', 1), ('=', 2), ('/', 3)],
        ]

headerFrame = tkinter.Frame(mainWindow)
headerFrame.grid(row=0, column=0, columnspan=5, sticky='n')
label = tkinter.Label(headerFrame, text='Calculator')
# columnspan is only effective when we give columns 'weights'
label.grid(row=0, column=0, sticky='n')

# Result window frame
resultWindow = tkinter.Entry(mainWindow)
resultWindow.grid(row=0, column=0, sticky='nsew')
resultWindow.config(border=2, relief='sunken')

# key pad frame
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# add keys to key pad frame
row = 0
for keyRow in keys:
    for key, index in keyRow:
        # start new row when we get to a '1' as an index (see format above)
        if index == 1:
            row += 1
        button = tkinter.Button(keyPad, text=key)
        # Can use sticky=tkinter.E + tkinter.W
        button.grid(row=row, column=index, sticky='ew')

tkinter.mainloop()
