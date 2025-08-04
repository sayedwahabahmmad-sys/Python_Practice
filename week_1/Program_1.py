import tkinter as tk

def show_values():
    a = 10
    b = 3.14
    c = 2 + 3j

    output = (
        f"Integer:\n"
        f"  Value: {a}\n"
        f"  Type: {type(a).__name__}\n\n"
        f"Float:\n"
        f"  Value: {b}\n"
        f"  Type: {type(b).__name__}\n\n"
        f"Complex:\n"
        f"  Value: {c}\n"
        f"  Real part: {c.real}\n"
        f"  Imaginary part: {c.imag}\n"
        f"  Type: {type(c).__name__}"
    )

    result_label.config(text=output)

# Create the main window
root = tk.Tk()
root.title("Python Number Data Types")

# Create a frame for padding
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Title label
title_label = tk.Label(frame, text="Click the button to show number data types", font=("Arial", 12))
title_label.pack(pady=10)

# Button to trigger display
show_button = tk.Button(frame, text="Show Data", command=show_values, font=("Arial", 11))
show_button.pack()

# Label to display the result
result_label = tk.Label(frame, text="", font=("Courier", 11), justify="left", anchor="w")
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
