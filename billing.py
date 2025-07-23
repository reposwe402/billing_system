from utils import app_helper

class Billing:

    def __init__(self, app):
        self.app = app

    def total(self):
        self.app.m_h_g_p = self.app.hand_gloves.get() * 12
        self.app.m_s_p = self.app.sanitizer.get() * 2
        self.app.m_m_p = self.app.mask.get() * 5
        self.app.m_d_p = self.app.dettol.get() * 30
        self.app.m_n_p = self.app.newsprin.get() * 5
        self.app.m_t_g_p = self.app.thermal_gun.get() * 15
        self.app.total_medical_price = float(self.app.m_m_p + self.app.m_h_g_p + self.app.m_d_p + self.app.m_n_p + self.app.m_t_g_p + self.app.m_s_p)

        self.app.medical_price.set("Rs. " + str(self.app.total_medical_price))
        self.app.c_tax = round((self.app.total_medical_price * 0.05), 2)
        self.app.medical_tax.set("Rs. " + str(self.app.c_tax))

        self.app.g_r_p = self.app.rice.get() * 10
        self.app.g_f_o_p = self.app.food_oil.get() * 10
        self.app.g_w_p = self.app.wheat.get() * 10
        self.app.g_d_p = self.app.daal.get() * 6
        self.app.g_f_p = self.app.flour.get() * 8
        self.app.g_m_p = self.app.maggi.get() * 5
        self.app.total_grocery_price = float(self.app.g_r_p + self.app.g_f_o_p + self.app.g_w_p + self.app.g_d_p + self.app.g_f_p + self.app.g_m_p)

        self.app.grocery_price.set("Rs. " + str(self.app.total_grocery_price))
        self.app.g_tax = round((self.app.total_grocery_price * 5), 2)
        self.app.grocery_tax.set("Rs. " + str(self.app.g_tax))

        self.app.c_d_s_p = self.app.sprite.get() * 10
        self.app.c_d_l_p = self.app.limka.get() * 10
        self.app.c_d_m_p = self.app.mazza.get() * 10
        self.app.c_d_c_p = self.app.coke.get() * 10
        self.app.c_d_f_p = self.app.fanta.get() * 10
        self.app.c_m_d = self.app.mountain_duo.get() * 10
        self.app.total_cold_drinks_price = float(self.app.c_d_s_p + self.app.c_d_l_p + self.app.c_d_m_p + self.app.c_d_c_p + self.app.c_d_f_p + self.app.c_m_d)

        self.app.cold_drinks_price.set("Rs. " + str(self.app.total_cold_drinks_price))
        self.app.c_d_tax = round((self.app.total_cold_drinks_price * 0.1), 2)
        self.app.cold_drinks_tax.set("Rs. " + str(self.app.c_d_tax))

        self.app.total_bill = float(self.app.total_medical_price + self.app.total_grocery_price + self.app.total_cold_drinks_price + self.app.c_tax + self.app.g_tax + self.app.c_d_tax)
