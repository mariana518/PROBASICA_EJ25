class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        self.productos.append({
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        })
        print(f"Producto '{nombre}' agregado exitosamente.")

    def eliminar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"] == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado exitosamente.")
                return
        print(f"Producto '{nombre}' no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto["nombre"] == nombre:
                print(f"Producto encontrado: {producto}")
                return producto
        print(f"Producto '{nombre}' no encontrado.")
        return None

    def mostrar_productos_ordenados(self):
        productos_ordenados = sorted(self.productos, key=lambda x: x["precio"])
        print("Lista de productos ordenados por precio:")
        for producto in productos_ordenados:
            print(producto)

if __name__ == "__main__":
    inventario = Inventario()
    inventario.agregar_producto("venti", "peluche", 999, 5)
    inventario.agregar_producto("almohada", "hogar", 50, 50)
    inventario.agregar_producto("Pelicula", "Entretenimiento", 65, 100)
    
    inventario.mostrar_productos_ordenados()
    inventario.buscar_producto("Venti")
    inventario.eliminar_producto("Pelicula")
    inventario.mostrar_productos_ordenados()



