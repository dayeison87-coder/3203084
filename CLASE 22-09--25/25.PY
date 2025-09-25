class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"Categoría: {self.nombre}, Productos: {len(self.productos)}"

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"

class Inventario:
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)

    def buscar_producto(self, nombre_producto):
        for categoria in self.categorias:
            for producto in categoria.productos:
                if producto.nombre.lower() == nombre_producto.lower():
                    return producto
        return None

    def reporte_stock(self):
        print("=== Reporte de Stock ===")
        for categoria in self.categorias:
            print(f"\n📂 {categoria.nombre}:")
            for producto in categoria.productos:
                print(f" - {producto.nombre}: {producto.stock} unidades")
        print("=========================")



if __name__ == "__main__":
  
    cat_electronica = Categoria("Electrónica")
    cat_ropa = Categoria("Ropa")

 
    p1 = Producto("Laptop", 3000, stock=10)
    p2 = Producto("Smartphone", 1200, stock=25)
    p3 = Producto("Camiseta", 50, stock=100)
    p4 = Producto("Jeans", 80, stock=60)

    cat_electronica.agregar_producto(p1)
    cat_electronica.agregar_producto(p2)
    cat_ropa.agregar_producto(p3)
    cat_ropa.agregar_producto(p4)

    inventario = Inventario()
    inventario.agregar_categoria(cat_electronica)
    inventario.agregar_categoria(cat_ropa)
    inventario.reporte_stock()

    buscado = "laptop"
    producto = inventario.buscar_producto(buscado)
    if producto:
        print(f"\nProducto encontrado: {producto}")
    else:
        print(f"\nNo se encontró el producto '{buscado}'")
