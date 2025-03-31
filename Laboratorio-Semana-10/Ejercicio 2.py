productos={}

def agregar_products(nombre, categoria, precio, cantidad):
    #producto = { 'nombre': str(input("ingresa el nombre del producto:")), 'categoria': str(input("ingresa la categoría del producto:" )), 'precio': float(input("ingrese el precio del producto:")), 'cantidad': int(input("ingrese la cantidad de productos existentes:"))}
    producto = {'nombre': nombre, 'categoria': categoria, 'precio': precio, 'cantidad': cantidad}
    productos[nombre.lower()]=producto
    print("Producto", nombre, "agregado al inventario")

def eliminar_producto(nombre):
    if nombre.lower() in productos: 
        del productos[nombre.lower()]
        print("Producto", nombre , "eliminado del archivo")


def buscar_producto(nombre):
    if nombre.lower() in productos:
        print(productos[nombre.lower()])

def productos_ordenados_por_precio():
    if not productos:
        print("El inventario está vacio.")
        



