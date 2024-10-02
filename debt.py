## Program to Calculate Debt Pay Off's
import matplotlib.pyplot as plt
from datetime import date
import customtkinter as ctk





# Sets the appearance mode of the application
# "System" sets the appearance same as that of the system
ctk.set_appearance_mode("System") 

# Sets the color of the widgets
# Supported themes: green, dark-blue, blue
ctk.set_default_color_theme("dark-blue")  


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = ctk.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)

from calculations import Calculations
        
        
newloan = Calculations(principal=17_893.7, interest_rate=0.078, duration_months=72)

# Create App class
class GUI(ctk.CTk):
# Layout of the GUI will be written in the init itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
# Sets the title of our window to "App"
        self.title("App")    
# Dimensions of the window will be 200x200
        self.geometry("1366x768")   
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # ------------------------------------------------------------------------------------#
        # Create a frame to hold a 1 x 3 grid
        top_frame_widget = self.top_frame()

        # ------------------------------------------------------------------------------------#
        # Create a frame to hold a 2 x 3 grid
        middle_frame_widget = self.middle_frame()

        # ------------------------------------------------------------------------------------#
        # Create a frame to hold a 1 x 3 grid
        bottom_frame_widget = self.bottom_frame()

        # ------------------------------------------------------------------------------------#
        # Create side bar that takes up 50% of the window
        self.side_bar = ctk.CTkFrame(self, width=200, fg_color="black")
        self.side_bar.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="ns")

        # Create a label for the side bar
        side_bar_frame_widget = self.create_normal_sized_label(parent=self.side_bar, text="Side Bar", row=0, column=0, total_width=200, bg_color="black", text_color="white")

        # Create a button for the side bar
        side_bar_button_widget = ctk.CTkButton(master=self.side_bar, text="Click Me", command=self.button_click)
        side_bar_button_widget.grid(row=1, column=0, padx=10, pady=10)

    def button_click(self):
        newloan.print_amortization_schedule()



    def top_frame(self):
        self.top_frame = ctk.CTkFrame(self, width=800, height=100, fg_color="green")
        self.top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        return self.top_frame
    
    def middle_frame(self):
        # Create the middle frame
        self.middle_frame = ctk.CTkFrame(self, width=800, fg_color="black")
        self.middle_frame.grid(row=1, column=0, padx=50, pady=50, sticky="")



        return self.middle_frame

    
    def bottom_frame(self):
        self.bottom_frame = ctk.CTkFrame(self, width=800, height=100, fg_color="yellow")
        self.bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        return self.bottom_frame

    def create_normal_sized_label(self, parent, text, row, column, total_width, total_height=30, bg_color="white", text_color="black"):
        label = ctk.CTkLabel(master=parent, text=text, font=("Arial", 12), width=total_width, height=total_height, fg_color=bg_color, text_color=text_color)
        label.grid(row=row, column=column, padx=10, pady=10)
        return label

    def create_large_sized_label(self, text, row, column):
        label = ctk.CTkLabel(master=self.middle_frame, text=text, font=("Arial", 18))
        label.grid(row=row, column=column, padx=10, pady=10)
        return label






    


    

def main():
   

    month_index = 6

    print(f"Total Interest at month {month_index}: {newloan.cumulative_interest(month_index)}")
    print(f"Monthly payment:  {newloan.monthly_payment()}")
    print(f"Balance at month {month_index} : {newloan.balance_at_month(month_index)}")
    
    #running_total = 0
    #test = newloan.print_amortization_schedule()
    


    print(f"Total Interest Paid: {newloan.total_interest_paid()}")
    #newloan.plot_balance()

    myGUI = GUI()
    myGUI.mainloop()




if __name__ == "__main__":
    main()