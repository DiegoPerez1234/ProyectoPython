class Supplier:
    name = ""
    rut = 0
    adress = ""
    comercial_activity = ""
    mail = ""
    phone = 0
    type_of_product = ""
    
    def _init_(self, name, rut, adress, comercial_activity, mail, phone, type_of_product):
        self.name = name
        self.rut = rut
        self.adress = adress
        self.comercial_activity = comercial_activity
        self.mail = mail
        self.phone = phone
        self.type_of_product = type_of_product
        # 

print("Bienvenido al inventario de la empresa")
print("Ingrese los datos del proveedor")

suplier_1 = Supplier("Juan", 12345678, "Av. La Tirana 123", "Venta de productos","toro@gmail.com", 123456789, "Alimentos")
print(suplier_1.name + "/ " + str(suplier_1.rut) + " /" + suplier_1.adress + "/ " + suplier_1.comercial_activity + "/ " + suplier_1.mail + "/ " + str(suplier_1.phone) + " /" + suplier_1.type_of_product)