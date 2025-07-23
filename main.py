from tkinter import Tk
from ui import Bill_App
from billing import Billing
from data_management import DataManagement

if __name__ == "__main__":
    root = Tk()
    app = Bill_App(root)
    billing = Billing(app)
    data_management = DataManagement(app)
    root.mainloop()
