import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Blurred Background Example")

    # Load the image
    original_image = Image.open("your_image.jpg")  # Replace with your image path
    # Apply a blur filter
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(10))  # Adjust the blur radius as needed

    # Convert the image to a PhotoImage
    bg_image = ImageTk.PhotoImage(blurred_image)

    # Create a label to hold the background image
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Make the label fill the window

    # Add a sample widget (e.g., a button)
    sample_button = tk.Button(root, text="Click Me", command=lambda: print("Button clicked!"))
    sample_button.pack(pady=20)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
