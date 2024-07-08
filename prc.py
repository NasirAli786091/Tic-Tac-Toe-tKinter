import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe Board")
root.geometry("300x300")  # Set the size of the window

# Function to handle button clicks
def on_button_click(row, col):
    print(f"Button clicked: Row {row}, Col {col}")

# Create a 3x3 grid of buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="x", width=10, height=5, command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col, padx=2, pady=2)  # Add some padding around the buttons

# Run the application
root.mainloop()
