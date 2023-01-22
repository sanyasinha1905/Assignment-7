import tkinter as tk

class GSTCalculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("GST Tax Finder Calculator")

        self.original_cost_label = tk.Label(self, text="Original Cost:")
        self.original_cost_label.grid(row=0, column=0)
        self.original_cost_entry = tk.Entry(self)
        self.original_cost_entry.grid(row=0, column=1)

        self.net_price_label = tk.Label(self, text="Net Price:")
        self.net_price_label.grid(row=1, column=0)
        self.net_price_entry = tk.Entry(self)
        self.net_price_entry.grid(row=1, column=1)

        self.calculate_button = tk.Button(self, text="Calculate GST Tax", command=self.calculate)
        self.calculate_button.grid(row=2, column=0, columnspan=2)

        self.result_label = tk.Label(self, text="GST Tax:")
        self.result_label.grid(row=3, column=0)
        self.result = tk.StringVar()
        self.result_entry = tk.Entry(self, textvariable=self.result)
        self.result_entry.grid(row=3, column=1)

    def calculate(self):
        original_cost = float(self.original_cost_entry.get())
        net_price = float(self.net_price_entry.get())
        gst_tax = (net_price - original_cost) * 100 / original_cost
        self.result.set("{:.2f}%".format(gst_tax))

app = GSTCalculator()
app.mainloop()
