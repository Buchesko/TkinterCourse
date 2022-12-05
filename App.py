import tkinter
from tkinter import *
import datetime as dt
import time
from tkcalendar import Calendar
class Clock(tkinter.Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        tkinter.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%H:%M:%S')
        else:
            self.time     = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)

# class Habits:
#
#     def __init__(self, habits_top):
#         myFrame = Frame(habits_top)
#         myFrame.pack()
#
#         self.myButton = Button(habits_top, text="Click me", command=self.clicker)
#         self.myButton.pack()
#
#     def clicker(self):
#         habits_top = Toplevel()
#         habits_top.title('Tkinter 5 Hours Coures, TopLevel')
#         habits_top.iconbitmap('C:\Python Projects\images\miecze.ico')
#         habits_top.geometry("600x400")
#         """Miejsce na dodatkowe ustawienia związane z ustawieniami geometry() habits_top"""
#         frame_habits = LabelFrame(habits_top,text='Habits')
#         frame_habits.pack()
#
#
#         clock1 = Clock(frame_habits)
#         clock1.pack()
#         # Miejsce na classy i ich funkcje
#         # Można zbudować nową classe i spróbuj ją utworzyć
#         # w nowym pliku i testuj ją potem wywołaj ją w tej funkcji
#         button_exit = Button(frame_habits, text="Exit", padx=50, pady=20, command=habits_top.destroy)
#         button_exit.pack()
#         # print("look at you... You click a button")




root = Tk()
root.title("Life Balance")
root.iconbitmap('C:\Python Projects\images\miecze.ico')



# top = Toplevel()
# top.title('Tkinter 5 Hours Coures, TopLevel')
# top.iconbitmap('C:\Python Projects\images\miecze.ico')


frame1 = LabelFrame(root, text="Witam Serdecznie")
frame1.pack(fill="both", expand="yes")
frame2 = LabelFrame(root,text="Life Indicators",)
frame2.pack(fill="both", expand="yes")
# frame_habits = LabelFrame(top,text='Habits')

date = dt.datetime.now()

today = Label(frame1, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20")
today.pack()

clock1 = Clock(frame1)
clock1.pack()
# habits = habit(frame_habits)
# habits.pack()

def Habits_clicked():
    """Zbudowany nowy konstructor top"""
    habits_top = Toplevel()
    tkc = Calendar(habits_top, selectmode="day", year=2022, month=1, date=1)

    # display on main window
    tkc.pack(pady=40)

    # getting date from the calendar

    def fetch_date():
        date.config(text="Selected Date is: " + tkc.get_date())

    # add button to load the date clicked on calendar

    but = Button(habits_top, text="Select Date", command=fetch_date, bg="black", fg='white')
    # displaying button on the main display
    but.pack()
    # Label for showing date on main display
    date = Label(habits_top, text="", bg='black', fg='white')

    date.pack(pady=20)

    # habits_top.title('Tkinter 5 Hours Coures, TopLevel')
    # habits_top.iconbitmap('C:\Python Projects\images\miecze.ico')
    # habits_top.geometry("600x400")
    # """Miejsce na dodatkowe ustawienia związane z ustawieniami geometry() habits_top"""
    # frame_habits = LabelFrame(habits_top,text='Habits')
    # frame_habits.pack()
    #
    # clock1 = Clock(frame_habits)
    # clock1.pack()
    # # Miejsce na classy i ich funkcje
    # # Można zbudować nową classe i spróbuj ją utworzyć
    # # w nowym pliku i testuj ją potem wywołaj ją w tej funkcji
    # button_exit = Button(frame_habits, text="Exit", padx=50, pady=20, command=habits_top.destroy)
    # button_exit.pack()
def Budget():
    return

# Front Panel atachet to
Habits = Button(frame2,text="Habits",padx=50, pady=20,command=lambda:Habits_clicked()).grid(row=1,column=0)
Budget= Button(frame2,text="Budget",padx=50, pady=20).grid(row=1,column=1)
Diet= Button(frame2,text="Dieta",padx=50, pady=20).grid(row=1,column=2)
Workouts= Button(frame2,text="Workouts",padx=40, pady=20).grid(row=2,column=0)
Paswords= Button(frame2,text="Password",padx=50, pady=20).grid(row=2,column=1)
Exit = Button(frame2,text="Exit",padx=50,pady=20, command= root.quit).grid(row=2,column=2)



root.mainloop()
