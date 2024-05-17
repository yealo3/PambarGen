import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # type: ignore
from backend import pambcgen

class PamBarGen:
    def __init__(self, root):
        self.root = root
        self.root.title("PamBarGen Generator")

        #storing the vars
        self.fac_num_var = tk.StringVar()
        self.lot_var = tk.StringVar()
        self.exp_date_var = tk.StringVar()
        self.price_var = tk.StringVar()

        #intput feilds
        tk.Label(root, text="Facture Number:").grid(row=0, column=0)
        self.fac_num_entry = tk.Entry(root, textvariable=self.fac_num_var)
        self.fac_num_entry.grid(row=0, column=1)

        tk.Label(root, text="Lot Number:").grid(row=1, column=0)
        self.lot_entry = tk.Entry(root, textvariable=self.lot_var)
        self.lot_entry.grid(row=1, column=1)

        tk.Label(root, text="Expiry Date:").grid(row=2, column=0)
        self.exp_date_entry = tk.Entry(root, textvariable=self.exp_date_var)
        self.exp_date_entry.grid(row=2, column=1)

        tk.Label(root, text="Price:").grid(row=3, column=0)
        self.price_entry = tk.Entry(root, textvariable=self.price_var)
        self.price_entry.grid(row=3, column=1)

        #the button
        self.generate_button = tk.Button(root, text="Generate now :D", command=self.pambcgen)
        self.generate_button.grid(row=4, column=0, columnspan=2)

        #the display
        self.barcode_label = tk.Label(root)
        self.barcode_label.grid(row=5, column=0, columnspan=2)

    def pambcgen(self):
        #Getint the vals
        fac_num = self.fac_num_var.get()
        lot = self.lot_var.get()
        exp_date = self.exp_date_var.get()
        price = self.price_var.get()

        #is it empty?
        if not all((fac_num, lot, exp_date, price)):
            messagebox.showerror("Error", "come on fill them all")
            return


        infos = fac_num + lot + exp_date + price

        #the making of the art of thi barcode
        try:
            fish = infos
            pambcgen(infos, fish)

            # Get the full path to the generated barcode image
            thepath = os.path.dirname(os.path.abspath(__file__))
            picpath = os.path.join(thepath, f"{fish}.png")

            # Display the generated barcode image
            thebcimage = Image.open(picpath)
            thebcphoto = ImageTk.PhotoImage(thebcimage)
            self.barcode_label.config(image=thebcphoto)
            self.barcode_label.image = thebcphoto

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PamBarGen(root)
    root.mainloop()
