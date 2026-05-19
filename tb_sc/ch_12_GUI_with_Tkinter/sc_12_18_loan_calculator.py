# file: sc_12_18_loan_calculator.py
# Demonstrates xxxVar and trace in a simple loan calculator.
# uses ttk for nicer widgets
import tkinter as tk
from tkinter import ttk

def calculate(*args):
    """Called automatically when a variable changes."""
    try:
        amount  = var_amount.get()
        rate  = var_rate.get() / 100 / 12   # monthly rate
        months    = var_months.get()
        if months <= 0:
            var_result.set("Invalid repayment period")
            return
        if rate == 0:
            monthly_payment = amount / months
        else:
            monthly_payment = (
                amount * rate
                / (1 - (1 + rate) ** -months)
            )
        var_result.set(f"${monthly_payment:,.0f} / month")
    except (tk.TclError, ZeroDivisionError):
        var_result.set("Invalid input")

root = tk.Tk()
root.title("Loan Calculator")

# Tkinter variables
var_amount    = tk.IntVar(value=20_000)
var_rate    = tk.DoubleVar(value=3.5)
var_months      = tk.IntVar(value=300)
var_result = tk.StringVar()

# Connect calculate() to all input variables
var_amount.trace_add("write", calculate)
var_rate.trace_add("write", calculate)
var_months.trace_add("write", calculate)

# Layout
fr = ttk.Frame(root, padding=20)
fr.pack()

ttk.Label(fr, text="Loan amount ($):").grid(
    row=0, column=0, sticky="w", pady=4)
ttk.Entry(fr, textvariable=var_amount, width=15).grid(
    row=0, column=1, pady=4)

ttk.Label(fr, text="Interest rate (%):").grid(
    row=1, column=0, sticky="w", pady=4)
ttk.Entry(fr, textvariable=var_rate, width=15).grid(
    row=1, column=1, pady=4)

ttk.Label(fr, text="Repayment period (months):").grid(
    row=2, column=0, sticky="w", pady=4)
ttk.Entry(fr, textvariable=var_months, width=15).grid(
    row=2, column=1, pady=4)

ttk.Separator(fr, orient="horizontal").grid(
    row=3, column=0, columnspan=2, sticky="ew", pady=10)

ttk.Label(fr, text="Monthly payment:").grid(
    row=4, column=0, sticky="w")
ttk.Label(fr, textvariable=var_result,
          font=("", 12, "bold")).grid(
              row=4, column=1, sticky="w")

# Calculate on startup
calculate()
root.mainloop()
