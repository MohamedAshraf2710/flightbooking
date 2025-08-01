#main.py

import tkinter as tk 
from home import HomePage 
import database

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.state("zoomed") 

        database.create_table()

        HomePage(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()