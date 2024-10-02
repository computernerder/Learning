import tkinter as tk

root = tk.Tk() 
root.title("My App Gui")
#root.geometry("800x800")



def add_to_list(Event=None):
    text = entry.get()  #Get the text from the entry widget.
    if text:
        myListbox.insert(tk.END, text)   #Add's the text the the list box
        entry.delete(0, tk.END) #Clear the entry widget.
    





frame = tk.Frame(root, width=500, height=500, bg="blue")
frame.grid(row=0, column=0)


#Pass in the fram as the parent item.
entry = tk.Entry(frame)
entry.grid(row=0, column=0)


#This will bind the enter key to the entry widget, calling add_to_list every time return is pressed.
entry.bind("<Return>", add_to_list)

#Button
entry_btn = tk.Button(frame, text="Add", command=add_to_list)
entry_btn.grid(row=0, column=1)

myListbox = tk.Listbox(frame)
myListbox.grid(row=1, column=0, columnspan=2)

root.mainloop()