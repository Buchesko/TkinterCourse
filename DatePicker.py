from tkinter import *
from tkcalendar import Calendar

# creating an object of tkinter

tkobj = Tk()

# setting up the geomentry

tkobj.geometry("400x400")
tkobj.title("Calendar picker")
#creating a calender object
hour_string=StringVar()
min_string=StringVar()
last_value_sec = ""
last_value = ""
f = ('Times', 20)
tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)

#display on main window
tkc.pack(pady=40)

# getting date from the calendar

def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())
    Time_label.config(text = "Selected Time is:" +str(min_sb) + str(sec_hour) + str(sec) )


#add button to load the date clicked on calendar

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
#displaying button on the main display
but.pack()
#Label for showing date on main display
date = Label(tkobj,text="",bg='black',fg='white')
date.pack(pady=20)
Time_label = Label(tkobj,text="")
Time_label.pack()
min_sb = Spinbox(
    tkobj,
    from_=0,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=2,
    state="readonly",
    font=f,
    justify=CENTER
    )
sec_hour = Spinbox(
    tkobj,
    from_=0,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    width=2,
    justify=CENTER
    )

sec = Spinbox(
    tkobj,
    from_=0,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=2,
    font=f,
    justify=CENTER
    )

min_sb.pack(side=LEFT, fill=X, expand=True)
sec_hour.pack(side=LEFT, fill=X, expand=True)
sec.pack(side=LEFT, fill=X, expand=True)
#starting the object
tkobj.mainloop()