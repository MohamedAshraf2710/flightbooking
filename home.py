import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage

class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#f5f7fa")
        self.master = master

        self.build_ui()

    def build_ui(self):
        # العنوان الرئيسي
        tk.Label(
            self,
            text="✈️ Flighty ReserveMate",
            font=("Helvetica", 28, "bold"),
            bg="#f5f7fa",
            fg="#1e3a8a"
        ).pack(pady=60)

        # زر حجز الطيران
        tk.Button(
            self,
            text="➕ Book a Flight",
            command=self.open_booking,
            font=("Helvetica", 14, "bold"),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            width=25,
            height=2,
            cursor="hand2"
        ).pack(pady=15)

        # زر عرض الحجوزات
        tk.Button(
            self,
            text="📋 View Reservations",
            command=self.open_reservations,
            font=("Helvetica", 14, "bold"),
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            activeforeground="white",
            relief="flat",
            width=25,
            height=2,
            cursor="hand2"
        ).pack(pady=5)

    def open_booking(self):
        self.destroy()
        BookingPage(self.master).pack(fill="both", expand=True)

    def open_reservations(self):
        self.destroy()
        ReservationsPage(self.master).pack(fill="both", expand=True)