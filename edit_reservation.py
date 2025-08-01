# edit_reservation.py

import tkinter as tk
from tkinter import messagebox
import database

class EditReservation(tk.Frame):
    def __init__(self, master, reservation, refresh_callback):
        super().__init__(master, bg="#f0f4f8")
        self.master = master
        self.reservation = reservation
        self.refresh_callback = refresh_callback

        tk.Label(
            self,
            text="✏️ Edit Reservation",
            font=("Arial", 20, "bold"),
            bg="#f0f4f8",
            fg="#007acc"
        ).pack(pady=30)

        self.entries = {}
        labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]

        for i, label in enumerate(labels):
            frame = tk.Frame(self, bg="#f0f4f8")
            frame.pack(pady=7)

            tk.Label(
                frame,
                text=label + ":",
                width=15,
                anchor="w",
                bg="#f0f4f8",
                fg="#333333",
                font=("Arial", 11)
            ).pack(side="left")

            entry = tk.Entry(frame, width=30, font=("Arial", 11))
            entry.insert(0, reservation[i + 1]) 
            entry.pack(side="left")
            self.entries[label.lower().replace(" ", "_")] = entry

        tk.Button(
            self,
            text="💾 Save",
            width=15,
            height=2,
            bg="#28a745",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.save_changes
        ).pack(pady=20)

    
        tk.Button(
            self,
            text="⬅️ Cancel",
            width=10,
            bg="#cccccc",
            fg="#333333",
            font=("Arial", 10),
            command=self.back
        ).pack()

    def save_changes(self):
        new_data = [entry.get() for entry in self.entries.values()]

        if not all(new_data):
            messagebox.showwarning("Missing Data", "Please fill in all fields.")
            return

        database.update(self.reservation[0], *new_data)
        messagebox.showinfo("Success", "Reservation updated.")
        self.refresh_callback()
        self.back()

    def back(self):
        self.destroy()