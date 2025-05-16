class Account:
    def __init__(self,id,whatfor,name,email,password,comment=None):
        self.whatfor = whatfor
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.comment = comment

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.name}, Correo: {self.email}, Contraseña: {self.password}"