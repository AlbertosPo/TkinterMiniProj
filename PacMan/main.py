"""
    -> Primal Pac-Man game.
"""

# Importing libraries related to display

import tkinter as tk
# from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk

"""
    Pygame library used only for load sound from folder.
"""
import pygame


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")



class MovePacMan(tk.Label):
    
    def __init__(self,master=None):
        super().__init__(master)
        # First appearance of pacman is right
        image = Image.open("pacman-art/pacman-right/1.png")
        img = image.resize((20,20))
        img = ImageTk.PhotoImage(img)
        self.image = img
        self.config(height=20,width=20,image=img,bg="black")
        self.ChangeBool_R = 1
        self.ChangeBool_L = 1
        self.ChangeBool_U = 1
        self.ChangeBool_D = 1



    
    def which_path_image(self,where,number):
            path_image = "pacman-art/pacman-"+where+number
            image = Image.open(path_image)
            img = image.resize((20,20))
            img = ImageTk.PhotoImage(img)
            self.image = img
            self.config(height=20,width=20,image=img,bg="black")

    def change_heading(self, where,dx, dy):
        
        if where == "right":

            if self.ChangeBool_R == 1:
                self.which_path_image(where,"/2.png")
                self.ChangeBool_R = 2
            elif self.ChangeBool_R == 2:

                self.which_path_image(where,"/3.png")
                self.ChangeBool_R = 3
            elif self.ChangeBool_R == 3 :

                self.which_path_image(where,"/1.png")
                self.ChangeBool_R = 1
        elif where == "left":
            
            if self.ChangeBool_L == 1:
                self.which_path_image(where,"/2.png")
                self.ChangeBool_L = 2
            elif self.ChangeBool_L == 2:
                self.which_path_image(where,"/3.png")
                self.ChangeBool_L = 3
            elif self.ChangeBool_L == 3 :
                self.which_path_image(where,"/1.png")
                self.ChangeBool_L = 1
            
        elif where == "up":

            if self.ChangeBool_U == 1:
                self.which_path_image(where,"/2.png")
                self.ChangeBool_U =2
            elif self.ChangeBool_U == 2 :
                self.which_path_image(where,"/3.png")
                self.ChangeBool_U = 3
            elif self.ChangeBool_U == 3:
                self.which_path_image(where,"/1.png")
                self.ChangeBool_U = 1

        elif where == "down":
            if self.ChangeBool_D == 1:
                self.which_path_image(where,"/2.png")
                self.ChangeBool_D =2
            elif self.ChangeBool_D == 2 :
                self.which_path_image(where,"/3.png")
                self.ChangeBool_D = 3
            elif self.ChangeBool_D == 3:
                self.which_path_image(where,"/1.png")
                self.ChangeBool_D = 1


class dotFood(tk.Label):
    def __init__(self,master=None):
        super().__init__(master)
        image = Image.open("pacman-art/other/dot.png")
        img = image.resize((50,60))
        img = ImageTk.PhotoImage(img)
        self.image = img
        self.config(height=5,width=5,image=img,bg="red")
  

        

class PlayWindow(tk.Toplevel):

    def __init__(self,master=None):
        super().__init__(master)
        self.title("Play Pac-Man")
        self.geometry("455x480")
        self.configure(bg='black')

        self.moveX = 5
        self.moveY = 0
        self._list =[]
        self.listOut = []
        self.DictCoord = {}
        

        # Coordinates of pacman dots
        self.coord_dots = {}

        self.createDotsFood()
        self.createPacMan()

        geometry_info = self.winfo_width()
        print(f"Geometry info : {geometry_info} ")
        

        center_window(self)

        self.HereTest()

    def HereTest(self):
        print("Here-Test")
    
    def createPacMan(self):
        cvs = MovePacMan(self)
        self.inputFromButton(cvs)
        cvs.place(x=5,y=0)
        

    def createDotsFood(self):
        
        for i in range(3):
            _list = []
            y_coordinates = []
            for j in range(3):
                dots = dotFood(self)
                dots.place(x=(i*10+1)*10,y=(j+1)*40)

                """
                    -> S.O.S <-
                    Replace it with 2-D Array .
                    Or Find other way to order this mess below
                """

                self.listOut.append(dots) 
                _list.append(dots)
                y_coordinates.append( (j+1)*40 )
            self.DictCoord.update({(i*10+1)*10 : _list.append(dots)})
            self.coord_dots.update( {  (i*10+1)*10 : y_coordinates})
         
        # for i in list_obj:
        #     print(i.destroy())

    def deletePosition(self,x_in,y_in):
        """
            -> S.O.S <-
            Ugly Code need change.
        """
        if x_in == 10 and y_in == 40:
            return  0
        elif x_in == 10 and y_in == 80:
            return 1
        elif x_in == 10 and y_in == 120:
            return 2
        elif x_in == 110 and y_in == 40:
            return  3
        elif x_in == 110 and y_in == 80:
            return 4
        elif x_in == 110 and y_in == 120:
            return 5
        if x_in == 210 and y_in == 40:
            return  6
        elif x_in == 210 and y_in == 80:
            return 7
        elif x_in == 210 and y_in == 120:
            return 8
        
            
        
    def eatDot(self,x_in,y_in):
        for x,y in zip(self.coord_dots.keys(),self.coord_dots.values()):
            # print(f"x : {x} , y : {y}")
            # print(f"x_in : {x_in} , y_in : {y_in}")
            if x_in == x and y_in in y:
                
                for x_iter in self.coord_dots.keys():
                    for y_iter in self.coord_dots.values():
                        
                        for y_iter_of_iter in y_iter:
                            if x_in == x_iter and y_in == y_iter_of_iter:
                                pos = self.deletePosition(x_in,y_in)                              
                                self.listOut[pos].destroy()


                
            

        

    def replacePacman(self,where,pacman):

        if where == "right" and self.moveX<430:
            self.moveX = self.moveX + 5
            pacman.place(x=self.moveX,y=self.moveY)
        elif where == "left" and 0<self.moveX:
            self.moveX = self.moveX - 5
            pacman.place(x=self.moveX,y=self.moveY)
        elif where == "up" and 0<self.moveY:
            self.moveY = self.moveY - 5
            pacman.place(x=self.moveX,y=self.moveY)
        elif where == "down" and self.moveY<455:
            self.moveY = self.moveY + 5
            pacman.place(x=self.moveX,y=self.moveY)
        
        self.eatDot(self.moveX,self.moveY)
            
        


    
    def inputFromButton(self,cvs):
        ds = 3
        self.bind("<KeyPress-Left>", lambda _: [cvs.change_heading("left",-ds, 0),self.replacePacman("left",cvs)])
        self.bind("<KeyPress-Right>", lambda _: [cvs.change_heading("right",ds, 0),self.replacePacman("right",cvs)])
        self.bind("<KeyPress-Up>", lambda _: [cvs.change_heading("up",0, -ds),self.replacePacman("up",cvs)])
        self.bind("<KeyPress-Down>", lambda _: [cvs.change_heading("down",0, ds),self.replacePacman("down",cvs)])
        







class MainWindow(tk.Tk):
    def __init__(self,master=None):
        super().__init__(master)

        self.title("Pac-Man")
        self.geometry("455x480")
        self.resizable(False,False) 
        self.Access = False

        self.creatingArea()

        # Is it necessery ?? (Not sure)
        pygame.mixer.init()

        # geometry_info = self.geometry()
        # print(f"Geometry info : {geometry_info} ")

        center_window(self) 

        self.mainloop()
    
    def creatingArea(self):
        image = Image.open("PacPaper.jpg")
        img = image.resize((480,550))
        img = ImageTk.PhotoImage(img)

        label = tk.Label(image= img)
        label.image = img # Required to prevent image from being garbage collected

        label.place(x=-10,y=-40)
        

        Button = tk.Button(self,text="Start Game",height=3,width=20)
        Button.bind("<Button>",lambda e : [self.HalloWorld() ,self.Sounds() ])
            
        Button.place(x=160,y=30)
                

        SecondButton = tk.Button(self,text="Exit",height=3,width=20,command=self.destroy)
        SecondButton.place(x=160,y=120)
    
    def HalloWorld(self):
        """
            ->This if statement prevent to open second PlayWindow() if someone click second time on "Start Game" button
        """
        if self.Access == False:
            PlayWindow()
            self.Access = True
    

    def Sounds(self):
        pygame.mixer.music.load("GameSound/freesound.mp3")
        pygame.mixer.music.play(loops=0)
       




menuOfGame = MainWindow()




























