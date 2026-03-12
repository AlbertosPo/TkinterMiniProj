"""
    Libraries related to GUI(widget). 
"""
import tkinter as tk
from tkinter import ttk ,Canvas
from tkinter import PhotoImage
from PIL import Image,ImageTk
import customtkinter

"""
    Libraries related to Numbers and Math .
"""
import random





"""
    Changing default location of window and make it display at the center of window. 
"""
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")



class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        """
            Setting windows appearance attributes:
             1) title
             2) dimensions of window
             3) set it not resizable
        """
        self.title("BomBox")
        self.geometry("455x480")
        self.resizable(False,False) # Need window to stay static.


        """
            Program calls first labelBomb() function .
            And after labels creation and placing them to window , program calls second function buttonsBox().
            The reason for that order , is that "program" tries to put labels under the buttons.
        """        


        # Constructor automatically calls function labelBomb() to create labels with image.
        self.labelBomb()

        # Constructor automatically calls function buttonsBox() to create buttons.
        self.buttonsBox()

        # Move created window to the center of screen.
        center_window(self)

        # Start the main window loop
        # For now it's preferable to mainloop work in MainWindow . 
        self.mainloop()
        #Anything we add to main window after self.mainloop() it doesn't contained.
    
    def random12Integers(self):
        
        List_of_Random_numbers = []
        howManyBombs = random.randint(1,8) # Every line can have 1 to 8 bombs.
        for _ in range(howManyBombs):
            random_int = random.randint(0,12) # Initialize a number 0 to 11.
            List_of_Random_numbers.append(random_int) # This list have got all positions of bombs in every line.
        

        List_of_Empty_rows = []
        howManyEmptyRows = random.randint(2,6) # Pick random number from 2 to 5
        for _ in range(howManyEmptyRows):
            random_int_for_rows = random.randint(0,12)
            List_of_Empty_rows.append(random_int_for_rows)

        # Using set , make list with unique numbers and place them
        # in order. (But in this case , order doesn't matter )
        List_of_Random_numbers = list(set(List_of_Empty_rows))

        return List_of_Random_numbers,List_of_Empty_rows
        

    def LoopForButtons_Labels(self,Choice_in):

        Choice = Choice_in
        _ , EmptyRows = self.random12Integers()
        
        
        RowsAndColumns = 12
        for i in range(RowsAndColumns):
            
            
            """
                -> If statement that used only in case of label creation.
                -> As an action , it calls function for list of random numbers
            """
            if Choice == "Label":
                randIntList,_ = self.random12Integers()

                            
            for j in range(RowsAndColumns):
                
                """
                    -> If statement check if function LoopForButtons_Labels 
                    -> called for buttons or labels creation. 
                """
                if Choice=="Label" and i not in EmptyRows:
                    """
                        ***->   Write explanation of if condition   <-***
                    """

                    if  j in randIntList:
                        image = Image.open("bombIcon.png")  # Replace with your image file path

                        # Resizing the image dimansion.
                        resized_image = image.resize((34, 36))

                        img = ImageTk.PhotoImage(resized_image)

                        # Fit image to label
                        label = tk.Label(image=img)
                        label.image = img  # Required to prevent image from being garbage collected
                
                
                        # Modification of buttons location
                        label.place(x=j*38,y=i*40)
                        


                elif Choice == "Button":
                    
                    if i==j:
                        imageB = Image.open("warningIcon.png")
                        imageB = imageB.resize((22,30))
                        ctk_img = customtkinter.CTkImage(imageB,size=imageB.size)
                        #imageB = imageB.resize((30,32))

                        #imgButton = ImageTk.PhotoImage(imageB)
                        #imageToButton = imgButton
                        
                        button = customtkinter.CTkButton(master = self
                                                        ,text = ""
                                                        , image = ctk_img#imageToButton
                                                        , height=35, width=25
                                                        ,fg_color="white"
                                                        )
                    else:

                        button = tk.Button(self, text=f"{i*RowsAndColumns+j}"
                                    , height=2, width=4
                                    ) # borderwidth=2, removed
                    """
                        -> I can't give command .destroy inside of tk.Button(...) due to 
                        -> object button first have to be created.
                        -> So , after creation of button we can modify its characteristics . Such as, give to it 
                        -> the functionality that whenever someone clicked to it , it has to disappear.
                    """
                    button.configure(command=button.destroy)
                    
                    # Modification of buttons location
                    #button.grid(row=i, column=j, sticky="ew")
                    button.place(x=j*38,y=i*40)

        

    
    def labelBomb(self):
        self.LoopForButtons_Labels("Label" )
        

    def buttonsBox(self):
        self.LoopForButtons_Labels("Button")
        



mainWindow = MainWindow()






