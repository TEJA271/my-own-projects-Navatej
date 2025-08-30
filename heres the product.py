import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Product: {product}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers.")

root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

desc_label = tk.Label(root, text="This app calculates the product of two numbers using widgets in Tkinter.", wraplength=380)
desc_label.pack(pady=10)

label1 = tk.Label(root, text="Enter the first number:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter the second number:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.pack(pady=10)

result_text = tk.Text(root, height=2, width=30)
result_text.pack()

root.mainloop()
