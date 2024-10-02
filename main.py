import tkinter as tk
root = tk.Tk()
root.title("My App Gui")
root.geometry("500x500")


def on_click():
    print("Button Clicked")
    
    #Use config to change a parameter.
    myLabel.config(text="Button Clicked")





myFrame = tk.Frame(root, width=500, height=500, bg="blue")


#Used as a label.
myLabel = tk.Label(root, text="Hello World")
myLabel.grid(row=0, column=0)

#This gives you a list of all the Keys. as a it is a dictionary.
#print(myLabel.config())

#Create a Button
btn = tk.Button(root, text="My Button", command=on_click)
#Call Geometry Manager
btn.grid(row=1, column=0)

root.mainloop()