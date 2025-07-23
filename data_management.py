import os
from tkinter import messagebox

class DataManagement:
    def __init__(self, app):
        self.app = app

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.app.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.app.txtarea.delete("1.0", END)
                for d in f1:
                    self.app.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.app.sanitizer.set(0)
            self.app.mask.set(0)
            self.app.hand_gloves.set(0)
            self.app.dettol.set(0)
            self.app.newsprin.set(0)
            self.app.thermal_gun.set(0)
            # ============grocery==============================
            self.app.rice.set(0)
            self.app.food_oil.set(0)
            self.app.wheat.set(0)
            self.app.daal.set(0)
            self.app.flour.set(0)
            self.app.maggi.set(0)
            # =============coldDrinks=============================
            self.app.sprite.set(0)
            self.app.limka.set(0)
            self.app.mazza.set(0)
            self.app.coke.set(0)
            self.app.fanta.set(0)
            self.app.mountain_duo.set(0)
            # ====================taxes================================
            self.app.medical_price.set("")
            self.app.grocery_price.set("")
            self.app.cold_drinks_price.set("")

            self.app.medical_tax.set("")
            self.app.grocery_tax.set("")
            self.app.cold_drinks_tax.set("")

            self.app.c_name.set("")
            self.app.c_phone.set("")

            self.app.bill_no.set("")
            x = random.randint(1000, 9999)
            self.app.bill_no.set(str(x))

            self.app.search_bill.set("")
            self.app.welcome_bill()
