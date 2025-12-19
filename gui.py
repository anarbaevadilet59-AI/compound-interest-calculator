import tkinter as tk
from logic import calculate_compound
from plotter import plot_growth

def run():
    root = tk.Tk()
    root.title("Compound Interest Calculator")

    tk.Label(root, text="Monthly contribution").pack()
    monthly_entry = tk.Entry(root)
    monthly_entry.pack()

    tk.Label(root, text="Annual rate (%)").pack()
    rate_entry = tk.Entry(root)
    rate_entry.pack()

    tk.Label(root, text="Years").pack()
    years_entry = tk.Entry(root)
    years_entry.pack()

    def calculate():
        monthly = float(monthly_entry.get())
        rate = float(rate_entry.get())
        years = int(years_entry.get())

        total, history = calculate_compound(monthly, rate, years)
        result_label.configure(text=f"Future Value: {total:,.2f}")
        plot_growth(history)

    tk.Button(root, text="Calculate", command=calculate).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
