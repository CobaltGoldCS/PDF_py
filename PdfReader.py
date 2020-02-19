from pdf2image import convert_from_path
import tkinter as tk
from PIL import Image, ImageTk
import os
class pdf:
    def __init__(self):
        self.root = tk.Tk()
    def PdfConverter(self):
        file_list = os.listdir(r'A:\Dylan\Documents\PDF files')
        for i, file in enumerate(file_list):
            print("File number "+str(i)+', '+file)

        select = int(input("Choose a file number to open: "))
        for i, file in enumerate(file_list):
            if select == i:
                print("Verified")
                folderPath = file[:-4]
                filepath = 'A:\\Dylan\\Documents\\PDF files\\' + file

        try:
            os.mkdir('ConvertedFiles/'+folderPath)
            print("Converting Files")
            os.chdir('ConvertedFiles/'+folderPath)
            images = convert_from_path(filepath)
            for i, image in enumerate(images):
                fname = str(i)+'.png'
                print(f"Creating {fname}")
                image.save(fname, 'PNG')
        except (TypeError, UnboundLocalError, FileExistsError):
            print("Invalid number")
            raise Exception(f"The number {select} is invalid, either it's been\nConverted already, or the file doesn't exist")
        
        print("PDF successfully converted")
        os.chdir('..\\..')

    def show(self):
        os.chdir("ConvertedFiles")
        allFiles = list(enumerate(os.listdir(os.path.join(os.getcwd()))))
        for i, folder in allFiles:
            print(f"Folder number {i}, {folder}")

        choice  = int(input("Number: ").strip())
        chosenFolder = [file for i, file in allFiles if i == choice]
        selected = chosenFolder[0]
        os.chdir(selected)

        basewidth = 750
        im = Image.open('0.png')
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        label = tk.Label(self.root, image=photo)
        label.image = '0.png'
        label.grid(columnspan=3)

        MoveOne = tk.Button(self.root, text = "->", command = lambda: self.move(label,label.image,1))
        MoveBack = tk.Button(self.root, text = "<-", command = lambda: self.move(label,label.image,-1))

        MoveOne.grid(column=2, row=1)
        MoveBack.grid(column=0, row=1)
        self.root.mainloop()
    
    def move(self, label, image, i):
        length = len(os.listdir(os.getcwd()))
        currentNum = int(os.path.basename(image))
        
        if currentNum + i > length:
            currentNum = 0
        elif currentNum + i < 0:
            currentNum = length
        else:
            currentNum += i
        
        basewidth = 750
        imageName = str(currentNum)+'.png'
        im = Image.open(imageName)
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        im = im.resize((basewidth,hsize), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(im)
        label.image = imageName
        label.configure(image=photo)

        
if __name__ == "__main__":
    app = pdf()
    app.show()