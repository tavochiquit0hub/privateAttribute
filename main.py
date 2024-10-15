from ClassVenta import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Octavio")
productos = [
    {"producto": "Producto A", "cantidad": 2, "precio_unitario": 50.00},
    {"producto": "Producto B", "cantidad": 1, "precio_unitario": 30.75},
    {"producto": "Producto C", "cantidad": 3, "precio_unitario": 10.00},
]

venta.set_productos(productos)
venta.mostrar_detalle()