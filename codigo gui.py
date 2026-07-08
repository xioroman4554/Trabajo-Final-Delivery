"""
SISTEMA DE GESTIÓN DE DELIVERY
"""

import tkinter as tk
from tkinter import ttk, messagebox


class Pedido:
    def __init__(self, numero, cliente, zona, importe):
        self.numero = numero
        self.cliente = cliente
        self.zona = zona
        self.importe = importe
        self.estado = "Pendiente"


pedidos = []


# ----------------------------------------------------------------------
# VENTANA: Registrar pedido
# ----------------------------------------------------------------------
def abrir_registrar_pedido():
    ventana = tk.Toplevel()
    ventana.title("Registrar pedido")
    ventana.geometry("360x300")
    ventana.resizable(False, False)

    contenedor = ttk.Frame(ventana, padding=20)
    contenedor.pack(fill="both", expand=True)

    ttk.Label(contenedor, text="Registrar nuevo pedido", font=("Segoe UI", 12, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(0, 15)
    )

    ttk.Label(contenedor, text="Número de pedido:").grid(row=1, column=0, sticky="w", pady=5)
    entry_numero = ttk.Entry(contenedor)
    entry_numero.grid(row=1, column=1, pady=5)

    ttk.Label(contenedor, text="Cliente:").grid(row=2, column=0, sticky="w", pady=5)
    entry_cliente = ttk.Entry(contenedor)
    entry_cliente.grid(row=2, column=1, pady=5)

    ttk.Label(contenedor, text="Zona de reparto:").grid(row=3, column=0, sticky="w", pady=5)
    entry_zona = ttk.Entry(contenedor)
    entry_zona.grid(row=3, column=1, pady=5)

    ttk.Label(contenedor, text="Importe ($):").grid(row=4, column=0, sticky="w", pady=5)
    entry_importe = ttk.Entry(contenedor)
    entry_importe.grid(row=4, column=1, pady=5)

    def guardar():
        try:
            numero = int(entry_numero.get())
        except ValueError:
            messagebox.showerror("Error", "El número de pedido debe ser un entero.")
            return

        for pedido in pedidos:
            if pedido.numero == numero:
                messagebox.showerror("Error", "Ese número de pedido ya existe.")
                return

        cliente = entry_cliente.get().strip()
        zona = entry_zona.get().strip()

        try:
            importe = float(entry_importe.get())
        except ValueError:
            messagebox.showerror("Error", "El importe debe ser un número.")
            return

        if cliente == "" or zona == "" or importe <= 0:
            messagebox.showerror("Error", "Datos inválidos. Revise los campos.")
            return

        pedidos.append(Pedido(numero, cliente, zona, importe))
        messagebox.showinfo("Éxito", "Pedido registrado correctamente.")
        ventana.destroy()

    botones = ttk.Frame(contenedor)
    botones.grid(row=5, column=0, columnspan=2, pady=(20, 0))
    ttk.Button(botones, text="Guardar", command=guardar).pack(side="left", padx=5)
    ttk.Button(botones, text="Cancelar", command=ventana.destroy).pack(side="left", padx=5)


# ----------------------------------------------------------------------
# VENTANA: Listar pedidos
# ----------------------------------------------------------------------
def abrir_listar_pedidos():
    ventana = tk.Toplevel()
    ventana.title("Lista de pedidos")
    ventana.geometry("650x350")

    contenedor = ttk.Frame(ventana, padding=15)
    contenedor.pack(fill="both", expand=True)

    columnas = ("numero", "cliente", "zona", "importe", "estado")
    tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=12)

    for col, titulo, ancho in [
        ("numero", "N° Pedido", 80),
        ("cliente", "Cliente", 150),
        ("zona", "Zona", 130),
        ("importe", "Importe", 100),
        ("estado", "Estado", 120),
    ]:
        tabla.heading(col, text=titulo)
        tabla.column(col, width=ancho, anchor="center")

    tabla.pack(fill="both", expand=True)

    if not pedidos:
        messagebox.showinfo("Sin datos", "No hay pedidos registrados.")

    for pedido in pedidos:
        tabla.insert(
            "", "end",
            values=(pedido.numero, pedido.cliente, pedido.zona, f"${pedido.importe:.2f}", pedido.estado),
        )


# ----------------------------------------------------------------------
# VENTANA: Cambiar estado del pedido
# ----------------------------------------------------------------------
def abrir_cambiar_estado():
    if not pedidos:
        messagebox.showinfo("Sin datos", "No hay pedidos registrados.")
        return

    ventana = tk.Toplevel()
    ventana.title("Cambiar estado del pedido")
    ventana.geometry("360x220")
    ventana.resizable(False, False)

    contenedor = ttk.Frame(ventana, padding=20)
    contenedor.pack(fill="both", expand=True)

    ttk.Label(contenedor, text="Cambiar estado de pedido", font=("Segoe UI", 12, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(0, 15)
    )

    ttk.Label(contenedor, text="Pedido:").grid(row=1, column=0, sticky="w", pady=5)
    opciones_pedidos = [f"{p.numero} - {p.cliente}" for p in pedidos]
    combo_pedido = ttk.Combobox(contenedor, values=opciones_pedidos, state="readonly", width=20)
    combo_pedido.grid(row=1, column=1, pady=5)
    combo_pedido.current(0)

    ttk.Label(contenedor, text="Nuevo estado:").grid(row=2, column=0, sticky="w", pady=5)
    combo_estado = ttk.Combobox(
        contenedor, values=["Pendiente", "En reparto", "Entregado"], state="readonly", width=20
    )
    combo_estado.grid(row=2, column=1, pady=5)
    combo_estado.current(0)

    def guardar():
        indice = combo_pedido.current()
        nuevo_estado = combo_estado.get()
        pedidos[indice].estado = nuevo_estado
        messagebox.showinfo("Éxito", "Estado actualizado.")
        ventana.destroy()

    botones = ttk.Frame(contenedor)
    botones.grid(row=3, column=0, columnspan=2, pady=(20, 0))
    ttk.Button(botones, text="Guardar", command=guardar).pack(side="left", padx=5)
    ttk.Button(botones, text="Cancelar", command=ventana.destroy).pack(side="left", padx=5)


# ----------------------------------------------------------------------
# VENTANA: Estadísticas
# ----------------------------------------------------------------------
def abrir_estadisticas():
    if not pedidos:
        messagebox.showinfo("Sin datos", "No hay datos para mostrar.")
        return

    importe_total = 0
    entregados = 0
    zonas = {}

    for pedido in pedidos:
        importe_total += pedido.importe
        if pedido.estado == "Entregado":
            entregados += 1
        zonas[pedido.zona] = zonas.get(pedido.zona, 0) + 1

    ventana = tk.Toplevel()
    ventana.title("Estadísticas")
    ventana.geometry("360x400")

    contenedor = ttk.Frame(ventana, padding=20)
    contenedor.pack(fill="both", expand=True)

    ttk.Label(contenedor, text="Estadísticas", font=("Segoe UI", 12, "bold")).pack(pady=(0, 15))

    ttk.Label(contenedor, text=f"Cantidad de pedidos: {len(pedidos)}").pack(anchor="w", pady=3)
    ttk.Label(contenedor, text=f"Pedidos entregados: {entregados}").pack(anchor="w", pady=3)
    ttk.Label(contenedor, text=f"Importe de ventas totales: ${importe_total:.2f}").pack(anchor="w", pady=3)

    ttk.Separator(contenedor).pack(fill="x", pady=10)
    ttk.Label(contenedor, text="Pedidos por zona:", font=("Segoe UI", 10, "bold")).pack(anchor="w")

    for zona, cantidad in zonas.items():
        ttk.Label(contenedor, text=f"  {zona}: {cantidad}").pack(anchor="w", pady=2)


# ----------------------------------------------------------------------
# VENTANA PRINCIPAL (menú tipo instalador)
# ----------------------------------------------------------------------
def iniciar_app():
    raiz = tk.Tk()
    raiz.title("Sistema de Gestión de Delivery")
    raiz.geometry("400x350")
    raiz.resizable(False, False)

    estilo = ttk.Style()
    estilo.theme_use("clam")

    contenedor = ttk.Frame(raiz, padding=25)
    contenedor.pack(fill="both", expand=True)

    ttk.Label(
        contenedor, text="SISTEMA DE GESTIÓN\nDE DELIVERY",
        font=("Segoe UI", 14, "bold"), justify="center"
    ).pack(pady=(0, 25))

    ttk.Button(contenedor, text="1. Registrar pedido", command=abrir_registrar_pedido, width=30).pack(pady=6)
    ttk.Button(contenedor, text="2. Listar pedidos", command=abrir_listar_pedidos, width=30).pack(pady=6)
    ttk.Button(contenedor, text="3. Cambiar estado del pedido", command=abrir_cambiar_estado, width=30).pack(pady=6)
    ttk.Button(contenedor, text="4. Ver estadísticas", command=abrir_estadisticas, width=30).pack(pady=6)
    ttk.Button(contenedor, text="5. Salir", command=raiz.destroy, width=30).pack(pady=6)

    raiz.mainloop()


if __name__ == "__main__":
    iniciar_app()
