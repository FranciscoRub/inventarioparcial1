import bdinv

from sqlalchemy import Column, Integer, String, Float

class Inventarios(bdinv.Base):
    __tablename__='inventario'

    ID = Column(Integer,primary_key=True,autoincrement=True)
    Codigo = Column(String(50),nullable=False)
    Producto= Column(String(50),nullable=False)
    Preciounitario= Column(Float,nullable=False)
    Cantidad = Column(Integer,nullable=False)
    Marca = Column(String(50),nullable=False)


    def __init__(self,ID,Producto,Preciounitario,Cantidad,Codigo,Marca):
        self.ID = ID
        self.Codigo = Codigo
        self.Producto = Producto
        self.Preciounitario = Preciounitario
        self.Cantidad = Cantidad
        self.Marca = Marca
        
    def __repr__(self):
        return f'\n ID: {self.ID} || Codigo: {self.Codigo} || Producto: {self.Producto} || Preciounitario: {self.Preciounitario}|| Marca: {self.Marca}||Cantidad: {self.Cantidad} '

    def __str__ (self):
        return self.Producto
