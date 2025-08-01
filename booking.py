import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  
import database


class BookingPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f0f4f8")
        self.master = master


        tk.Label(
            self,
            text="✈️ Book a Flight",
            font=("Arial", 20, "bold"),
            bg="#f0f4f8",
            fg="#007acc"
        ).pack(pady=30)

        self.entries = {}

        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field in fields:
            frame = tk.Frame(self, bg="#f0f4f8")
            frame.pack(pady=7)

            tk.Label(
                frame,
                text=field + ":",
                width=15,
                anchor="w",
                bg="#f0f4f8",
                fg="#333333",
                font=("Arial", 11)
            ).pack(side="left")

            if field == "Date":
             
                date_entry = DateEntry(
                    frame,
                    width=27,
                    background="#007acc",
                    foreground="white",
                    borderwidth=2,
                    date_pattern='dd/mm/yyyy'
                )
                date_entry.pack(side="left")
                self.entries["date"] = date_entry
            else:
                entry = tk.Entry(frame, width=30, font=("Arial", 11))
                entry.pack(side="left")
                self.entries[field.lower().replace(" ", "_")] = entry

      
        tk.Button(
            self,
            text="✅ Submit",
            width=18,
            height=2,
            bg="#007acc",
            fg="white",
            activebackground="#005f99",
            font=("Arial", 11, "bold"),
            command=self.submit
        ).pack(pady=25)

       
        tk.Button(
            self,
            text="⬅️ Back",
            width=10,
            bg="#cccccc",
            fg="#333333",
            font=("Arial", 10),
            command=self.go_back
        ).pack()

    def submit(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        if all(data.values()):
            database.insert(**data)
            messagebox.showinfo("Success", "Reservation booked successfully!")
            self.go_back()
        else:
            messagebox.showwarning("Missing Data", "Please fill out all fields.")

    def go_back(self):
        from home import HomePage
        self.destroy()
        HomePage(self.master).pack(fill="both", expand=True)