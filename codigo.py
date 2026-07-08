class Pedido:
    def __init__(self, numero, cliente, zona, importe):
        self.numero = numero
        self.cliente = cliente
        self.zona = zona
        self.importe = importe
        self.estado = "Pendiente"


pedidos = []


def registrar_pedido():
    try:
        numero = int(input("Número de pedido: "))

        for pedido in pedidos:
            if pedido.numero == numero:
                print("Ese número de pedido ya existe.")
                return

        cliente = input("Cliente: ").strip()
        zona = input("Zona de reparto: ").strip()
        importe = float(input("Importe: $"))

        if cliente == "" or zona == "" or importe <= 0:
            print("Datos inválidos.")
            return

        nuevo = Pedido(numero, cliente, zona, importe)
        pedidos.append(nuevo)

        print("Pedido registrado correctamente.")

    except ValueError:
        print("Error: ingresó un dato incorrecto.")


def listar_pedidos():
    if len(pedidos) == 0:
        print("No hay pedidos registrados.")
        return

    print("\n----- LISTA DE PEDIDOS -----")

    for pedido in pedidos:
        print(f"""
Pedido N°: {pedido.numero}
Cliente: {pedido.cliente}
Zona: {pedido.zona}
Importe: ${pedido.importe}
Estado: {pedido.estado}
-----------------------------
""")


def cambiar_estado():
    try:
        numero = int(input("Ingrese el número del pedido: "))

        for pedido in pedidos:
            if pedido.numero == numero:

                print("\n1. Pendiente")
                print("2. En reparto")
                print("3. Entregado")

                opcion = input("Nuevo estado: ")

                if opcion == "1":
                    pedido.estado = "Pendiente"
                elif opcion == "2":
                    pedido.estado = "En reparto"
                elif opcion == "3":
                    pedido.estado = "Entregado"
                else:
                    print("Opción inválida.")
                    return

                print("Estado actualizado.")
                return

        print("Pedido no encontrado.")

    except ValueError:
        print("Debe ingresar un número válido.")


def estadisticas():
    if len(pedidos) == 0:
        print("No hay datos para mostrar.")
        return

    importe_total = 0
    entregados = 0
    zonas = {}

    for pedido in pedidos:
        importe_total += pedido.importe

        if pedido.estado == "Entregado":
            entregados += 1

        if pedido.zona in zonas:
            zonas[pedido.zona] += 1
        else:
            zonas[pedido.zona] = 1

    print("\n----- ESTADÍSTICAS -----")
    print("Cantidad de pedidos:", len(pedidos))
    print("Pedidos entregados:", entregados)
    print(f"Importe de Ventas Totales: ${importe_total}")

    print("\nPedidos por zona:")
    for zona, cantidad in zonas.items():
        print(f"{zona}: {cantidad}")


def menu():
    while True:

        print("\n===== SISTEMA DE DELIVERY =====")
        print("1. Registrar pedido")
        print("2. Listar pedidos")
        print("3. Cambiar estado del pedido")
        print("4. Ver estadísticas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_pedido()

        elif opcion == "2":
            listar_pedidos()

        elif opcion == "3":
            cambiar_estado()

        elif opcion == "4":
            estadisticas()

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()
