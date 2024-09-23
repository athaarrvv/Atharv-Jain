from tkinter import *
from PIL import Image, ImageTk, ImageFilter

root = Tk()

root.geometry("700x500")

root.minsize(400, 300)
root.maxsize(1920, 1080)

root.iconbitmap('img/logo.ico')
root.title("Makhanlal Chaturvedi National University of Journalism and Communication, Bhopal")

bg_image_filter = Image.open("img/bg_img.jpg")
blurred_bg_image = bg_image_filter.filter(ImageFilter.GaussianBlur(10))

bg_image = ImageTk.PhotoImage(blurred_bg_image)




root.mainloop()