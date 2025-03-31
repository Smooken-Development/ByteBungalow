import customtkinter as ctk
from tkinter import messagebox

class ByteBungalowUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ByteBungalow")

                                                         # main windowframes
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.top_frame = ctk.CTkFrame(self.main_frame)
        self.top_frame.pack(fill="x")
        self.middle_frame = ctk.CTkFrame(self.main_frame)
        self.middle_frame.pack(fill="both", expand=True)
        self.bottom_frame = ctk.CTkFrame(self.main_frame)
        self.bottom_frame.pack(fill="x")

                                                                            # top widgets
        self.search_label = ctk.CTkLabel(self.top_frame, text="Search by:")
        self.search_label.pack(side="left")

        self.search_entry = ctk.CTkEntry(self.top_frame)
        self.search_entry.pack(side="left")

        self.search_button = ctk.CTkButton(self.top_frame, text="Search")
        self.search_button.pack(side="left")

                                                                                    # middle widgets
        self.listings_label = ctk.CTkLabel(self.middle_frame, text="Rental Listings:")

        self.listings_label.pack(side="top")

        self.listings_tab = ctk.CTkTabview(self.middle_frame)
        self.listings_tab.pack(side="top", fill="both", expand=True)

                                                                                #  bottom  widgets
        self.stats_label = ctk.CTkLabel(self.bottom_frame, text="Statistics:")
        self.stats_label.pack(side="left")

        self.stats_button = ctk.CTkButton(self.bottom_frame, text="View Statistics")
        self.stats_button.pack(side="left")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()
    ui = ByteBungalowUI(root)
    ui.run()
