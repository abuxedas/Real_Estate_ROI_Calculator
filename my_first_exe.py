import tkinter as tk
from tkinter import messagebox

def realizar_calculo():

    try:
        # Obtener los valores de las casillas
        price_ = float(price.get())
        valor_catastral_ = 0.5 * price_
        tax_ = float(tax.get()) / 100
        gastos_gestio_ = float(gastos_gestio.get())
        gastos_anual_desgr_ = float(gastos_desgr.get())
        gastos_anual_no_desgr_ = float(gastos_no_desgr.get())
        gastos_anual_ = gastos_anual_desgr_ + gastos_anual_no_desgr_
        ibi_prctg_ = float(ibi_prctg.get()) / 100
        ibi_ = valor_catastral_ * ibi_prctg_
        rent_ = float(rent.get())
        anual_rent_ = rent_ * 12
        cantitat_desgravar_ = gastos_anual_desgr_ + ibi_ + (0.03 * 0.5 * price_)
        tram_irpf_ = 0.41 # Pendent de fer input
        irpf_ = 0.5 * tram_irpf_ * ((anual_rent_) - cantitat_desgravar_) # 0.5 = reducció del irpf


        # Pendent incluir reforma (el cost es suma al cost d'adquisicio per amortitzar el 3%)
        # Realizar el cálculo
        retorno_bruto_sin_revalor = ((anual_rent_ - gastos_anual_ - ibi_) / (price_ + tax_ + gastos_gestio_)) * 100
        retorno_neto_sin_revalor = ((anual_rent_ - gastos_anual_ - ibi_ - irpf_) / (price_ + tax_ + gastos_gestio_)) * 100
        prueba = price_ / anual_rent_

        # Mostrar el resultado
        etiqueta_retorno_bruto_sin_revalor.config(text=f"Retorno Bruto sin revalorización: {retorno_bruto_sin_revalor}")
        etiqueta_retorno_neto_sin_revalor.config(text=f"Retorno Neto sin revalorización: {retorno_neto_sin_revalor}")
        etiqueta_prueba.config(text=f"prueba: {prueba}")


    except ValueError:
        # Manejar errores si no se ingresan números válidos
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora ROI inmobiliario")
window.geometry("1400x1000")

#-----------------------------------------------------------------------
#   v  CASILLAS DE ENTRADA  v
#-----------------------------------------------------------------------

tk.Label(window, text="Preu de venta").pack(pady=5)
price = tk.Entry(window)
price.pack(pady=5)

tk.Label(window, text="prctg impost de traspas (normalment 10)").pack(pady=5)
tax = tk.Entry(window)
tax.pack(pady=5)

tk.Label(window, text="Gastos de gestió de compra (sobre los 3500)").pack(pady=5)
gastos_gestio = tk.Entry(window)
gastos_gestio.pack(pady=5)

tk.Label(window, text="Gastos anuals desgravable").pack(pady=5)
gastos_desgr = tk.Entry(window)
gastos_desgr.pack(pady=5)

tk.Label(window, text="Gastos anuals NO desgravable").pack(pady=5)
gastos_no_desgr = tk.Entry(window)
gastos_no_desgr.pack(pady=5)

tk.Label(window, text="% IBI (a catalunya = 0.75 %)").pack(pady=5)
ibi_prctg = tk.Entry(window)
ibi_prctg.pack(pady=5)

tk.Label(window, text="Lloguer mensual").pack(pady=5)
rent = tk.Entry(window)
rent.pack(pady=5)

tk.Label(window, text="% interes hipoteca").pack(pady=5)
prctg_hipoteca = tk.Entry(window)
prctg_hipoteca.pack(pady=5)


#-----------------------------------------------------------------------
# Botón para realizar el cálculo
#-----------------------------------------------------------------------

boton_calcular = tk.Button(window, text="Calcular", command=realizar_calculo)
boton_calcular.pack(pady=10)

#-----------------------------------------------------------------------
# Etiqueta para mostrar el resultado
#-----------------------------------------------------------------------

etiqueta_retorno_bruto_sin_revalor = tk.Label(window, text="Retorno Bruto sin revalorización: ")
etiqueta_retorno_bruto_sin_revalor.pack(pady=10)

etiqueta_retorno_neto_sin_revalor = tk.Label(window, text="Retorno Con sin revalorización: ")
etiqueta_retorno_neto_sin_revalor.pack(pady=10)

etiqueta_prueba = tk.Label(window, text="Prueba")
etiqueta_prueba.pack(pady=10)

#-----------------------------------------------------------------------
# Iniciar el bucle de la aplicación
#-----------------------------------------------------------------------

window.mainloop()