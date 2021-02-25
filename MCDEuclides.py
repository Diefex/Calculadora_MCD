from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Text
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
from tkinter import Scrollbar
from tkinter import INSERT

proc = "Procedimiento: \n"
vari = [1]
cof = []

#Inicio Algoritmo Euclides -------------------------------------
def euclides2(A, B, x0, y0, x1, y1):
    global proc, vari, cof

    if(A<B):
        aux = A
        A = B
        B = aux

    proc = proc + "\nMCD("+str(A)+","+str(B)+"):\n"

    if(A==0):
        proc = proc + "\nMCD("+str(A)+","+str(B)+")="+str(B)+"\n"
        proc = proc + "\nque se puede escribir como: "+str(cof[0])+"("+str(x0)+")+ "+str(cof[1])+"("+str(y0)+")="+str(B)+"\n"
        if(len(vari)<2):
            vari = [x0, y0]
        else:
            nv = [vari.pop()*y0, vari.pop()*y0]
            nv.reverse()
            vari = vari + nv + [x0]
            proc = proc + "y juntandolo con el siguiente coeficiente multiplicamos los anteriores x, y por "+str(y0)+" y tenemos las variables:\n"
            proc = proc + str(vari) + "\n"
        return B
    
    if(B==0):
        proc = proc + "\nMCD("+str(A)+","+str(B)+")="+str(A)+"\n"
        proc = proc + "\nque se puede escribir como: "+str(cof[0])+"("+str(x0)+")+ "+str(cof[1])+"("+str(y0)+")="+str(A)+"\n"
        if(len(vari)<2):
            vari = [x0, y0]
        else:
            nv = [vari.pop()*y0, vari.pop()*y0]
            nv.reverse()
            vari = vari + nv + [x0]
            proc = proc + "y juntandolo con los anteriores coeficientes\nmultiplicamos los anteriores x, y\npor "+str(y0)+" y tenemos las variables:\n"
            proc = proc + str(vari) + "\n"
        return A

    C = int(A/B)
    R = int(A%B)

    proc = proc + "\nComo " + str(A) + " y " + str(B) + " son diferentes de 0 \n"
    proc = proc + "hacemos la division: " + str(A) + "/" + str(B) + "=" + str(C) + "\n"
    proc = proc + "y encontramos que esta tiene un residuo de " + str(R) + "\n"
    proc = proc + "y podemos escribir esto como: \n"
    proc = proc + str(A) + " = " + str(B) + "*" + str(C) + " + " + str(R) + "\n"

    x = x0 + (x1*-C)
    y = y0 + (y1*-C)

    if(R!=0):
        proc = proc + "\nPara la combinacion lineal\nusamos los dos valores anteriores de x, y\njunto con el cociente "+str(C)+":\n"
        proc = proc + "x = "+str(x0)+"+ ("+str(x1)+"*-"+str(C)+") = "+str(x)+"\n"
        proc = proc + "y = "+str(y0)+"+ ("+str(y1)+"*-"+str(C)+") = "+str(y)+"\n"

    proc = proc + "\nAhora encontramos el MCD de " + str(B) + " y " + str(R) + ":\n"

    return euclides2(B, R, x1, y1, x, y)

def euclides(nums):
    global proc, cof

    nums.sort()
    nums.reverse()

    if(len(nums)<=2):
        cof = nums.copy()
        A = int(nums.pop())
        B = int(nums.pop())
        proc = proc + "\nContinuamos con MCD("+str(A)+","+str(B)+")\n"
        proc = proc + "\nPara la combinacion lineal empezamos diciendo que:\n"
        proc = proc + "mcd = "+str(A)+"(x) +"+str(B)+"(y)\n"
        proc = proc + "Y tenemos que:\n"
        proc = proc + str(A)+" = "+str(A)+"(1) +"+str(B)+"(0)\n"
        proc = proc + str(B)+" = "+str(A)+"(0) +"+str(B)+"(1)\n"
        return euclides2(A, B, 1, 0, 0 ,1)
    else:
        proc = proc + "\nMCD("
        for n in nums:
            proc = proc + str(n) + " "
        proc = proc + ")\n"
        x = nums.pop()
        return euclides([euclides(nums), x])

#Fin Algoritmo Euclides -------------------------------------

#Inicio Eliminacion de ceros -------------------------------------
def elim_ceros(co, va, d):
    k = 3

    while(va[len(va)-1]==0):
        j = 0
        while(va[j]!=0):
            j+=1

        for i in range(0,j):
            va[i] = int(va[i]*(1-(k*(co[j]/d))))

        va[j] = k

    return va
    
#Fin Eliminacion de ceros -------------------------------------

#Inicio Interfaz de Usuario ---------------------------------------
def mostrar_resultado():
    global output, vari, proc

    for w in output.winfo_children():
        w.destroy()

    resultado = Frame(output, bg="#2d3e52")
    resultado.pack()

    '''if(not(inputs.get().isdecimal()) or not(input_B.get().isdecimal())):
        Label(resultado, text="Por favor introduzca dos numeros enteros \nen los campos de arriba", bg="#2d3e52", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w")
        return'''

    Label(resultado, text="El MCD de "+str(inputs.get())+" es:", bg="#2d3e52", fg="white", font=("Arial", 16, "bold")).grid(row=0, column=0, sticky="w")
    coef = inputs.get().split(",")
    nms = []
    for c in coef:
        nms.append(int(c))
    coef = nms.copy()
    coef.sort()
    coef.reverse()
    nums = coef.copy()
    res = euclides(nums)
    
    proc_frm = Frame(resultado, bg="#2d3e52")
    proc_frm.grid(row=2, column=0, pady=10)
    proc_txt = Text(proc_frm, bg="#2d3e52", fg="white", font=("Arial", 12), width="65", height="20")
    
    proc = proc + "\nCombinacion Lineal:\n"

    comb = ""
    
    vari = elim_ceros(coef, vari, res)
    
    while(len(coef)>1):
        comb = comb + str(coef.pop())+"("+str(vari.pop())+") + "
    comb = comb + str(coef.pop())+"("+str(vari.pop())+")"

    Label(resultado, text=str(res)+" = "+comb, bg="#2d3e52", fg="white", font=("Arial", 20, "bold")).grid(row=1, column=0, sticky="w")
    proc = proc + comb

    proc_txt.insert(INSERT, proc)
    proc_txt.grid(row=0, column=0, sticky="w")

    scroll = Scrollbar(proc_frm, command=proc_txt.yview)
    scroll.grid(row=0, column=1, sticky="nsew")
    proc_txt.config(yscrollcommand=scroll.set)

    proc = "Procedimiento: \n"

ventana = Tk()
ventana.geometry("700x800")
ventana.config(bg="#2d3e52")
ventana.resizable(1,1)

fondo = Frame(ventana)
fondo.config(bg="#2d3e52")
fondo.pack(fill="both", expand="true", padx=20, pady=30)

Label(fondo, text="Calculadora MCD", bg="#2d3e52", fg="white", font=("Arial", 36, "bold")).grid(row=0, column=0, sticky="w")
Label(fondo, text="con algoritmo de Euclides", bg="#2d3e52", fg="white", font=("Arial", 16, "bold")).grid(row=1, column=0, sticky="w")

Label(fondo, text="Ingrese a continuación los numeros\nseparados por comas\npara calcular su MCD", bg="#2d3e52", fg="white", font=("Arial", 12), justify="left").grid(row=2, column=0, pady="20", sticky="w")

entrada = Frame(fondo, bg="#2d3e52")
entrada.grid(row=3, column=0, pady=2, sticky="w")

inputs = StringVar()
Label(entrada, text="MCD(", bg="#2d3e52", fg="white", font=("Arial", 14)).grid(row=0, column=0, sticky="e")
Entry(entrada, textvariable=inputs, highlightcolor="red", font=("Arial", 12), width=20).grid(row=0, column=1)
Label(entrada, text=")", bg="#2d3e52", fg="white", font=("Arial", 14)).grid(row=0, column=2, sticky="w")

Button(entrada, text="Calcular MCD", command=mostrar_resultado, relief="flat", bg="#e67f22", fg="white", font=("Arial", 14, "bold")).grid(row=2, column=0, columnspan=2, pady=10)
output = Frame(fondo, bg="#2d3e52")
output.grid(row=4, column=0, pady=10, sticky="w")
x = 1
y = 0

ventana.mainloop()
#Fin Interfaz de Usuario ---------------------------------------60,132,156,204