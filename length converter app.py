import tkinter as tk

def convert():
    try:
        value = float(entry.get())
        conversion = conversion_type.get()
        
        if conversion == "Meters to Feet":
            result = value * 3.28084
            result_label.config(text=f"{result:.2f} feet")
        elif conversion == "Feet to Meters":
            result = value / 3.28084
            result_label.config(text=f"{result:.2f} meters")
        elif conversion == "Meters to Centimeters":
            result = value * 100
            result_label.config(text=f"{result:.2f} cm")
        elif conversion == "Centimeters to Meters":
            result = value / 100
            result_label.config(text=f"{result:.2f} meters")
        else:
            result_label.config(text="Select a conversion type")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

conversion_type = tk.StringVar(value="Meters to Feet")

entry_label = tk.Label(root, text="Enter value:")
entry_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

options = [
    "Meters to Feet",
    "Feet to Meters",
    "Meters to Centimeters",
    "Centimeters to Meters"
]

option_menu = tk.OptionMenu(root, conversion_type, *options)
option_menu.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()
