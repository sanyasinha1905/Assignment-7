import tkinter as tk
from tkinter import ttk
import calendar
from tkinter import scrolledtext

class CalendarApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Calendar Application")
        
        self.year_label = tk.Label(self, text="Enter Year:")
        self.year_label.grid(row=0, column=0)
        self.year_entry = tk.Entry(self)
        self.year_entry.grid(row=0, column=1)

        self.calendar_button = tk.Button(self, text="Show Calendar", command=self.show_calendar)
        self.calendar_button.grid(row=1, column=0, columnspan=2)
        
        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.grid(row=2, column=0, columnspan=2)
        
    def show_calendar(self):
        year = int(self.year_entry.get())
        self.calendar_frame.destroy()
        self.calendar_frame = tk.Frame(self)
        self.calendar_frame.grid(row=2, column=0, columnspan=2)
        c = calendar.TextCalendar(calendar.SUNDAY)
        cal = c.formatyear(year)
        self.calendar_text = scrolledtext.ScrolledText(self.calendar_frame, wrap=tk.WORD)
        self.calendar_text.insert(tk.INSERT, cal)
        self.calendar_text.configure(state='disabled')
        self.calendar_text.pack()

app = CalendarApp()
app.mainloop()

