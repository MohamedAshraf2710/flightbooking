# reservations.py

import tkinter as tk
from tkinter import messagebox
import database
from edit_reservation import EditReservation

class ReservationsPage(tk.Frame):
    def __init__(self, master):  
        super().__init__(master, bg="#f0f4f8")
        self.master = master

        tk.Label(
            self,
            text="🗂️ All Reservations",
            font=("Arial", 20, "bold"),
            bg="#f0f4f8",
            fg="#007acc"
        ).pack(pady=30)

        self.table_frame = tk.Frame(self, bg="#f0f4f8")
        self.table_frame.pack()

        self.load_data()

        tk.Button(
            self,
            text="⬅️ Back",
            width=10,
            bg="#cccccc",
            fg="#333333",
            font=("Arial", 10),
            command=self.go_back
        ).pack(pady=15)

    def load_data(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        headers = ["ID", "Name", "Flight No.", "Departure", "Destination", "Date", "Seat", "", ""]
        for col, header in enumerate(headers):
            tk.Label(
                self.table_frame,
                text=header,
                bg="#007acc",
                fg="white",
                font=("Arial", 10, "bold"),
                width=12,
                relief="ridge"
            ).grid(row=0, column=col, padx=1, pady=1)

        data = database.view()
        for row_idx, row in enumerate(data, start=1):
            for col_idx, value in enumerate(row):
                tk.Label(
                    self.table_frame,
                    text=value,
                    bg="#ffffff",
                    font=("Arial", 10),
                    width=12,
                    relief="solid"
                ).grid(row=row_idx, column=col_idx, padx=1, pady=1)

            tk.Button(
                self.table_frame,
                text="✏️ Edit",
                width=8,
                bg="#12c6f8",
                fg="black",
                command=lambda r=row: self.edit_reservation(r)
            ).grid(row=row_idx, column=7, padx=1)

            tk.Button(
                self.table_frame,
                text="❌ Delete",
                width=8,
                bg="#e37f89",
                fg="white",
                command=lambda r=row: self.delete_reservation(r[0])
            ).grid(row=row_idx, column=8, padx=1)

    def delete_reservation(self, id):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?")
        if confirm:
            database.delete(id)
            self.load_data()

    def edit_reservation(self, row_data):
        self.destroy()
        EditReservation(self.master, row_data, self.back_to_this).pack(fill="both", expand=True)

    def back_to_this(self):
        self.destroy()
        ReservationsPage(self.master).pack(fill="both", expand=True)

    def go_back(self):
        from home import HomePage
        self.destroy()
        HomePage(self.master).pack(fill="both", expand=True)