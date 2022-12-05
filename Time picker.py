from tkinter import *

from tktimepicker import AnalogPicker, AnalogThemes, constants


def updateTime(time):
    time_lbl.configure(text="{}:{} {}".format(*time))  # remove 3rd flower bracket in case of 24 hrs time


root = Tk()

time = ()
time_picker = AnalogPicker(root, type=constants.HOURS12)
time_picker.pack(expand=True, fill="both")

theme = AnalogThemes(time_picker)
# theme.setDracula()
theme.setNavyBlue()
# theme.setPurple()
ok_btn = Button(root, text="ok", command=lambda: updateTime(time_picker.time()))
ok_btn.pack()

time_lbl = Label(root, text="Time:")
time_lbl.pack()

root.mainloop()
