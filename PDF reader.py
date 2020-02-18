import tkinter as tk
from PIL import Image, ImageTk
import os
root = tk.Tk()
allFiles = list(enumerate(os.listdir(os.getcwd())))
for i, file in allFiles:
    print(f"File number {i}, {file}")


choice  = int(input("Number: ").strip())
chosenFile = [file for i, file in allFiles if i == choice]
selected = chosenFile[0]
im = Image.open(selected)
im = im.resize((750, 750), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(im)
label = tk.Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()

root.mainloop()
