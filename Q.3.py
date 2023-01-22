import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Calculator")
        
        self.result = tk.StringVar()
        
        self.result_entry = tk.Entry(self, textvariable=self.result)
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
        
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        
        self.create_button(".", 4, 0)
        self.create_button("0", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)
        
        self.create_button("=", 5, 0, 2)
        
    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self, text=text, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=10, pady=10)
    
    def button_click(self, text):
        if text == "C":
            self.result.set("")
        elif text == "=":
            try:
                result = eval(self.result.get())
                self.result.set(result)
            except:
                self.result.set("Error")
        else:
            current = self.result.get()
            self.result.set(current + text)

app = Calculator()
app.mainloop()
