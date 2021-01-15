from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Text
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from tkinter import Scrollbar
from tkinter import INSERT

#Inicio Algoritmo Euclides -------------------------------------
def euclides(A, B):
    global proc

    if (A == 0):
        proc = proc + "\nEl MCD de " + str(A) + " y " + str(B) + " es simplemente " + str(B) + "\n"
        proc = proc + "\nEs decir que nuestro resultado es " + str(B)
        return B
    
    if (B == 0):
        proc = proc + "\nEl MCD de " + str(A) + " y " + str(B) + " es simplemente " + str(A) + "\n"
        proc = proc + "\nEs decir que nuestro resultado es " + str(A)
        return A

    R = int(A%B)

    proc = proc + "\nComo " + str(A) + " y " + str(B) + " son diferentes de 0 \n"
    proc = proc + "hacemos la division: " + str(A) + "/" + str(B) + "=" + str(int(A/B)) + "\n"
    proc = proc + "y encontramos que esta tiene un residuo de " + str(R) + "\n"
    proc = proc + "y podemos escribir esto como: \n"
    proc = proc + str(A) + " = " + str(B) + "*" + str(int(A/B)) + " + " + str(R) + "\n"
    proc = proc + "\nAhora encontramos el MCD de " + str(B) + " y " + str(R) + ":\n"

    return euclides(B, R)

#Fin Algoritmo Euclides -------------------------------------

#Inicio Interfaz de Usuario ---------------------------------------
def mostrar_resultado():
    global output
    global proc
    for w in output.winfo_children():
        w.destroy()

    resultado = Frame(output, bg="#2d3e52")
    resultado.pack()

    if(not(input_A.get().isdecimal()) or not(input_B.get().isdecimal())):
        Label(resultado, text="Por favor introduzca dos numeros enteros \nen los campos de arriba", bg="#2d3e52", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w")
        return
    
    Label(resultado, text="El MCD de "+str(input_A.get())+" y "+str(input_B.get())+" es:", bg="#2d3e52", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w")
    Label(resultado, text=euclides(int(input_A.get()), int(input_B.get())), bg="#2d3e52", fg="white", font=("Arial", 24, "bold")).grid(row=1, column=0, sticky="w")
    
    proc_frm = Frame(resultado, bg="#2d3e52")
    proc_frm.grid(row=2, column=0, pady=10)
    proc_txt = Text(proc_frm, bg="#2d3e52", fg="white", font=("Arial", 12), width="49", height="10")
    proc_txt.insert(INSERT, proc)
    proc_txt.grid(row=0, column=0, sticky="w")

    scroll = Scrollbar(proc_frm, command=proc_txt.yview)
    scroll.grid(row=0, column=1, sticky="nsew")
    proc_txt.config(yscrollcommand=scroll.set)

    proc = "Procedimiento: \n"

ventana = Tk()
ventana.geometry("500x650")
ventana.config(bg="#2d3e52")
ventana.resizable(1,1)

fondo = Frame(ventana)
fondo.config(bg="#2d3e52")
fondo.pack(fill="both", expand="true", padx=20, pady=30)

Label(fondo, text="Calculadora MCD", bg="#2d3e52", fg="white", font=("Arial", 36, "bold")).grid(row=0, column=0, sticky="w")
Label(fondo, text="con algoritmo de Euclides", bg="#2d3e52", fg="white", font=("Arial", 16, "bold")).grid(row=1, column=0, sticky="w")

entrada = Frame(fondo, bg="#2d3e52")
entrada.grid(row=2, column=0, pady=50, sticky="w")

input_A = StringVar()
Label(entrada, text="Ingrese el numero A", bg="#2d3e52", fg="white", font=("Arial", 14)).grid(row=0, column=0, sticky="w")
Entry(entrada, textvariable=input_A, highlightcolor="red", font=("Arial", 12), width=5).grid(row=0, column=1, padx=20)

input_B = StringVar()
Label(entrada, text="Ingrese el numero B", bg="#2d3e52", fg="white", font=("Arial", 14)).grid(row=1, column=0, sticky="w")
Entry(entrada, textvariable=input_B, highlightcolor="red", font=("Arial", 12), width=5).grid(row=1, column=1, padx=20)

Button(entrada, text="Calcular MCD", command=mostrar_resultado, relief="flat", bg="#e67f22", fg="white", font=("Arial", 14, "bold")).grid(row=2, column=0, columnspan=2, pady=10)
output = Frame(fondo, bg="#2d3e52")
output.grid(row=3, column=0, pady=10, sticky="w")

proc = "Procedimiento: \n"

ventana.mainloop()
#Fin Interfaz de Usuario ---------------------------------------