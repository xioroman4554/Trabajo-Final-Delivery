class Pedido:
    def __init__(self, numero, cliente, zona, importe):
        self.numero = numero
        self.cliente = cliente
        self.zona = zona
        self.importe = importe
        self.estado = "Pendiente"

    def mostrar(self):
        print(f"Pedido: {self.numero} | Cliente: {self.cliente} | Zona: {self.zona} | Importe: ${self.importe} | Estado: {self.estado}")


pedidos = []

while True:
    print("\n===== SISTEMA DELIVERY =====")
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Entregar pedido")
    print("4. Estadísticas")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        numero = int(input("Número de pedido: "))
        cliente = input("Cliente: ")
        zona = input("Zona de reparto: ")
        importe = float(input("Importe: $"))

        pedido = Pedido(numero, cliente, zona, importe)
        pedidos.append(pedido)

        print("Pedido registrado correctamente.")

    elif opcion == "2":
        if len(pedidos) == 0:
            print("No hay pedidos registrados.")
        else:
            for pedido in pedidos:
                pedido.mostrar()

    elif opcion == "3":
        numero = int(input("Número del pedido a entregar: "))
        encontrado = False

        for pedido in pedidos:
            if pedido.numero == numero:
                pedido.estado = "Entregado"
                print("Pedido entregado.")
                encontrado = True
                break

        if not encontrado:
            print("Pedido no encontrado.")

    elif opcion == "4":
        total = 0
        zonas = {}

        for pedido in pedidos:
            total += pedido.importe

            if pedido.zona in zonas:
                zonas[pedido.zona] += 1
            else:
                zonas[pedido.zona] = 1

        print(f"\nImporte de ventas totales: ${total}")
        print("Pedidos por zona:")
        for zona, cantidad in zonas.items():
            print(f"{zona}: {cantidad}")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")
