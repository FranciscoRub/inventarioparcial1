import bdinv
from modeloinv import Inventarios
import mysql.connector

# ---------------------------------------------------------PARCIAL 1------------------------------------------------
# FRANCICO RUBIO CEDULA 4-848-1301, UIP, PROGRAMACION IV
# PROPUESTA DE INVENTARIO DE UN SUPER (SUPER 99) CON OPCION DE REGISTRO, BUSQUEDA, EDICION Y ELIMINACION DE PRODUCTOS.
# EL PROYECTO UTILIZA UNA BASE DE DATOS, MYSQL
#--------------------------------------------------------------------------------------------------------------------
#CONSULTAR INVENTARIO 
def consultar_inventario():
    consul=bdinv.session.query(Inventarios).all()
    print(consul)

#REGISTRO NUEVO 
def registro():
    producto = input("Nuevo producto: ")
    preciouni = float(input("Precio unitario: "))
    cantidad= int(input("cantidad: "))
    codigo =input("código de producto: ")
    marca = input("Marca: ")
    x = Inventarios(None,producto,preciouni,cantidad,codigo,marca)
    bdinv.session.add(x)
    bdinv.session.commit()
    print("\n---------NUEVO PRODUCTO A INVENTARIO---------")
    print("Producto","(",x,")""guaradado con éxito.")
#SUMAR O AGREGAR PRODUCTO EXISTENTE
def agregarexisten():
    consultar_inventario()
    getid = input("\n ID de producto a adicionar: ")
    x = bdinv.session.query(Inventarios).get(getid)
    print("-----SELECCIÓN------\nProducto: ",x.Producto,"\nCódigo: ",x.Codigo,"\nPrecio unitario: ","\nMarca: ",x.Marca,x.Preciounitario,"\nCantidad: ",x.Cantidad)
    print("--------------------")
    cant = int(input("\nCantidad a ingresar: "))
    x.Cantidad = x.Cantidad + cant
    bdinv.session.commit()
    x = bdinv.session.query(Inventarios).first()
    consultar_inventario()
#ELIMINAR O RESTAR CANTIDAD DE UN PRODUCTO
def eliminarxcantidad():
    consultar_inventario()
    getid = input("\n ID de producto a descontar: ")
    x = bdinv.session.query(Inventarios).get(getid)
    print("-----SELECCIÓN------\nProducto: ",x.Producto,"\nCódigo: ",x.Codigo,"\nPrecio unitario: ","\nMarca: ",x.Marca,x.Preciounitario,"\nCantidad: ",x.Cantidad)
    print("--------------------")
    cant = int(input("\nCantidad a extraer: "))
    x.Cantidad = x.Cantidad - cant
    if (x.Cantidad <=0):
        x.Cantidad = 0
        bdinv.session.commit()
        x = bdinv.session.query(Inventarios).first()
    bdinv.session.commit()
    x = bdinv.session.query(Inventarios).first()
    consultar_inventario()
#ELIMINAR UN REGISTRO
def Eliminar():
    consultar_inventario()
    Elimreg =input("\n ID de producto a eliminar: ")
    Elimreg=bdinv.session.query(Inventarios).filter_by(ID=Elimreg).first()
    bdinv.session.delete(Elimreg)
    bdinv.session.commit()
    consultar_inventario()
#EDITAR REGISTRO
def editar_reg():
    consultar_inventario()
    Edit=input("\n ID de producto a editar: ")
    x=bdinv.session.query(Inventarios).get(Edit)
    print("-----SELECCIÓN------\nProducto: ",x.Producto,"\nCódigo: ",x.Codigo,"\nMarca: ",x.Marca,"\nPrecio unitario: ",x.Preciounitario,"\nCantidad: ",x.Cantidad)
    print("--------------------")
    print("------EDITAR--------")
    x.Producto =input("Producto: ")
    x.Codigo = input("codigo: ")
    x.Preciounitario = float(input("precio unitario: "))
    x.Cantidad = int(input("Cantidad: "))
    print("Producto editado con éxito...")
    bdinv.session.commit()
    x=bdinv.session.query(Inventarios).first()
    consultar_inventario()
def consultar_producto():
    mostrar = bdinv.session.query(Inventarios).order_by(Inventarios.Producto,Inventarios.ID)
    for mostrar in mostrar:
        print(mostrar.ID,mostrar.Producto)
    mostrar= input("\n\nID de Producto que desea consultar: ")
    x=bdinv.session.query(Inventarios).get(mostrar)
    print("\nProducto: ",x.Producto,"\nCódigo: ",x.Codigo,"\nMarca: ",x.Marca,"\nPrecio unitario: ",x.Preciounitario,"\nCantidad: ",x.Cantidad)

def precio():
    consultar_inventario()
    print("-----CONSULTAR PRECIO TOTAL--------")
    getid = input("\n ID del producto que desea consultar:  ")
    x = bdinv.session.query(Inventarios).get(getid)
    print("-----SELECCIÓN------\nProducto: ",x.Producto,"\nCódigo: ",x.Codigo,"\nPrecio unitario: ","\nMarca: ",x.Marca,x.Preciounitario,"\nCantidad: ",x.Cantidad)
    print("--------------------")
    precio = float(x.Cantidad) * x.Preciounitario
    print ("Precio de ",x.Producto,"Es",precio)

def run():

    #-------------- PRODUCTOS INICIALES------------------------
    pan = Inventarios(1,"Pan blanco",2.50,120,"LF2912312","Bimbo")
    bdinv.session.add(pan) bdinv.session.commit()
    
    panint = Inventarios(2,"Pan Integral",2.50,100,"LF9281321","Bimbo")
    bdinv.session.add(panint)
    bdinv.session.commit()
    
    leche= Inventarios(3,"Leche Entera",1.58,95,"LF99321931","La Chiricana")
    bdinv.session.add(leche)
    bdinv.session.commit()
    
    huevos = Inventarios(4,"Huevos 1 docena",3.50,30,"LF12312212","Toledano")
    bdinv.session.add(huevos)
    bdinv.session.commit()
    
    Banana = Inventarios(5,"Bananos",1.20,15,"LF3039123","Chiquita")
    bdinv.session.add(Banana)
    bdinv.session.commit()
    
    gatorade = Inventarios(6,"Gatorade Rojo",1.10,50,"LF5923312","CocaCola Company")
    bdinv.session.add(gatorade)
    bdinv.session.commit()

#MENU DE INVENTARIO 
    print("---------------------------SUPER 99----------------------------")
menuprincipal = int(input("---------Sistema de inventario del Super 99 ------------ \n 1- Inventario \n 2- Agregar nuevo registro a inventario \n 3- Agregar producto existente \n 4- Extraer cantidad de producto \n 5- Ver Precio total de producto \n 6- Editar Registro \n 7- Eliminar registro \n 8- Consultar Inventario \n 9- Salir \n\n Elija una opción: "))

while menuprincipal !=9:
    if menuprincipal == 1:
        consultar_inventario()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 2:
        registro()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal == 3:
        agregarexisten()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==4:
        eliminarxcantidad()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==5:
        precio()
        menuprincipal==input("preciones Enter para seguir: ")

    elif menuprincipal ==6:
        editar_reg()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==7:
        Eliminar()
        menuprincipal==input("preciones Enter para seguir: ")
    elif menuprincipal ==8:
        consultar_producto()
        menuprincipal==input("preciones Enter para seguir: ")
    else:
        print("Por favor digite una opción válida")
    menuprincipal = int(input("--Systema de inventario del Super 99: \n 1- Inventario \n 2- Agregar nuevo registro a inventario \n 3- Agregar producto existente \n 4- Extraer cantidad de producto \n 5- Ver Precio total de producto \n 6- Editar Registro \n 7- Eliminar registro \n 8- Consultar Inventario \n 9- Salir \n\n Elija una opción: "))

    pass
if __name__ =='__main__':
    bdinv.Base.metadata.create_all(bdinv.engine)
    run()
