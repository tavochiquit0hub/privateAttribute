class Venta:

    __id_venta = None

    __fecha = None

    __cliente = None

    __productos = None  # Lista de productos vendidos

    __total = None


    # Getters para acceder a los atributos privados

    def get_id_venta(self):
        return self.__id_venta


    def get_fecha(self):
        return self.__fecha


    def get_cliente(self):
        return self.__cliente


    def get_productos(self):
        return self.__productos


    def get_total(self):
        return self.__total


    # Setters para modificar los atributos privados

    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta


    def set_fecha(self, fecha):
        self.__fecha = fecha


    def set_cliente(self, cliente):
        self.__cliente = cliente


    def set_productos(self, productos):
        for producto in productos:
            if producto["producto"] not in ["Producto A", "Producto B", "Producto C", "Producto D"]:
                raise ValueError(f"Prodcuto {producto['producto']} no esta permitido")

        self.__productos = productos
        #Calcular el total automaticamente

        self.__total = sum(p["cantidad"]*p["precio_unitario"] for p in productos)


    # Método para mostrar los detalles de la venta

    def mostrar_detalle(self):

        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos:")

        # Asegúrate de que sea una lista de diccionarios
        if isinstance(self.__productos, list) and all(isinstance(p, dict) for p in self.__productos):
            for producto in self.__productos:
                print(
                    f"- {producto['producto']} (Cantidad: {producto['cantidad']}, Precio Unitario: ${producto['precio_unitario']:.2f})")
        print(f"Total: ${self.__total:.2f}")
