import tkinter as tk
from tkinter import messagebox as MessageBox
import os
from Codigo_Fuente.Funciones import camara as cm, camara as c
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from Codigo_Fuente import variables as v
from Codigo_Fuente import vozArchivo as vo
import analizadorLexico as aL
import analizadorSintactico as aS


class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.config(bg="gray81")
        self.ventana1.geometry("900x700")

        self.agregar_menu()
        self.textEditor=st.ScrolledText(self.ventana1, width=65, height=30)
        self.textEditor.grid(column=0, row=0, padx=5, pady=5)

        self.textTokens = st.ScrolledText(self.ventana1, width=40, height=30)
        self.textTokens.grid(column=3, row=0, padx=5, pady=5)

        self.textSintaxis = st.ScrolledText(self.ventana1, width=65, height=11)
        self.textSintaxis.grid(column=0, row=4, padx=5, pady=5)

        self.textEditor.bind('<KeyPress>', self.AnalisisPalabra)

        self.ventana1.mainloop()
    def agregar_menu(self):
        menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1, tearoff=0)
        opciones1.add_command(label="Abrir archivo", command=self.abrir)
        opciones1.add_command(label="Guardar archivo", command=self.guardar)

        opciones2 = tk.Menu(menubar1, tearoff=0)
        opciones2.add_command(label="Analizador Lexico", command=self.analizadorLexico)
        opciones2.add_command(label="Analizador Sintactico", command=self.analizadorSintactico)

        opciones3 = tk.Menu(menubar1, tearoff=0)
        opciones3.add_command(label="Convertir Audio", command=self.convertirSonido)

        opciones4 = tk.Menu(menubar1, tearoff=0)
        opciones4.add_command(label="Visualizar", command=self.camara)

        menubar1.add_cascade(label="Archivo", menu=opciones1)
        menubar1.add_cascade(label="Analizador", menu=opciones2)
        menubar1.add_cascade(label="Audio", menu=opciones3)
        menubar1.add_cascade(label="Automatas", menu=opciones4)



    def camara(self):
        cm.encenderCamara()

    def pintarPalabra(self,Palabra,color):
        contenido = self.textEditor.get(1.0, 'end-1c')
        contenido = contenido.upper()
        palabras = contenido.split()
        indiceInicial = "1.0"

        i = 0

        while i < len(palabras):

            if palabras[i] == Palabra:
                # Busca la palabra
                iniFeak = self.textEditor.search(Palabra, index=indiceInicial, stopindex='end', nocase=True, count=len(Palabra))
                inxFin = iniFeak + " + " + str(len(Palabra)) + "c"
                # Crear una etiqueta para el color
                self.textEditor.tag_add(Palabra + str(i), iniFeak, inxFin)
                self.textEditor.tag_config(Palabra + str(i), foreground=color)
                indiceInicial = inxFin

                l = locals()
            i += 1
    def AnalisisPalabra(self, action):
        contenido = self.textEditor.get(1.0, 'end-1c')
        contenido = contenido.upper()
        palabras = contenido.split()
        regex = r'[a-zA-Z ]{2,254}'
        i = 0
        while i < len(palabras):
            if palabras[i] == "BGN":
                self.pintarPalabra(Palabra="BGN", color="blue")
            elif palabras[i] == "END":
                self.pintarPalabra(Palabra="END", color="blue")
            elif palabras[i] == "IF":
                self.pintarPalabra(Palabra="IF", color="blue")
            elif palabras[i] == "ELSE":
                self.pintarPalabra(Palabra="ELSE", color="blue")
            elif palabras[i] == "WHL":
                self.pintarPalabra(Palabra="WHL", color="blue")
            elif palabras[i] == "DO":
                self.pintarPalabra(Palabra="DO", color="blue")
            elif palabras[i] == "PCD":
                self.pintarPalabra(Palabra="PCD", color="blue")
            elif palabras[i] == "CALL":
                self.pintarPalabra(Palabra="CALL", color="blue")
            elif palabras[i] == "INT":
                self.pintarPalabra(Palabra="INT", color="blue")
            elif palabras[i] == "FLT":
                self.pintarPalabra(Palabra="FLT", color="blue")
            elif palabras[i] == "CHR":
                self.pintarPalabra(Palabra="CHR", color="blue")
            elif palabras[i] == "STR":
                self.pintarPalabra(Palabra="STR", color="blue")
            elif palabras[i] == "ENDL":
                self.pintarPalabra(Palabra="ENDL", color="blue")
            elif palabras[i] == "AND":
                self.pintarPalabra(Palabra="AND", color="blue")
            elif palabras[i] == "OR":
                self.pintarPalabra(Palabra="OR", color="blue")
            elif palabras[i] == "NOT":
                self.pintarPalabra(Palabra="NOT", color="blue")

            elif palabras[i] == "+=":
                self.pintarPalabra(Palabra="+=", color="orange")
            elif palabras[i] == "-=":
                self.pintarPalabra(Palabra="-=", color="orange")
            elif palabras[i] == "*=":
                self.pintarPalabra(Palabra="*=", color="orange")
            elif palabras[i] == "/=":
                self.pintarPalabra(Palabra="/=", color="orange")
            elif palabras[i] == "+":
                self.pintarPalabra(Palabra="+", color="orange")
            elif palabras[i] == "-":
                self.pintarPalabra(Palabra="-", color="orange")
            elif palabras[i] == "*":
                self.pintarPalabra(Palabra="*", color="orange")
            elif palabras[i] == "/":
                self.pintarPalabra(Palabra="/", color="orange")
            elif palabras[i] == "=":
                self.pintarPalabra(Palabra="=", color="orange")
            elif palabras[i] == ">":
                self.pintarPalabra(Palabra=">", color="orange")
            elif palabras[i] == "<":
                self.pintarPalabra(Palabra="<", color="orange")

            elif palabras[i] == "{":
                self.pintarPalabra(Palabra="{", color="green")
            elif palabras[i] == "}":
                self.pintarPalabra(Palabra="}", color="green")
            elif palabras[i] == "[":
                self.pintarPalabra(Palabra="[", color="green")
            elif palabras[i] == "]":
                self.pintarPalabra(Palabra="]", color="green")
            elif palabras[i] == "!":
                self.pintarPalabra(Palabra="!", color="green")
            elif palabras[i] == ",":
                self.pintarPalabra(Palabra=",", color="green")
            elif palabras[i] == ";":
                self.pintarPalabra(Palabra=";", color="green")
            elif palabras[i] == "(":
                self.pintarPalabra(Palabra="(", color="green")
            elif palabras[i] == ")":
                self.pintarPalabra(Palabra=")", color="green")

            i += 1
    def salir(self):
        sys.exit()


    def analizadorLexico(self):
        archivo = self.textEditor.get("1.0", tk.END)
        if len(archivo) == 1:
            #agregar audio para alertar al usuario
            MessageBox.showwarning("Alerta",
                                   "Debes redactar codigo para poder hacer un analisis lexico.")
        else:
            os.system("start C:\\LYA_SMARTCRIB-master\\codigo_fuente\\Audio\\Analisis_Lexico.mp3")
            (tokens, color) = aL.obtenerLexico(archivo)
            v.cSint = 0
            if color == 1:
                self.textTokens.delete("1.0", tk.END)
                self.textTokens.insert("1.0", tokens)
                v.cError = 0
                v.arreglo = 'Analizador Lexico\n'
            else:
                self.textTokens.delete("1.0", tk.END)
                self.textTokens.insert("1.0", tokens)
                v.cError = 0
                v.arreglo = 'Analizador Lexico\n'


    def analizadorSintactico(self):
        if v.cSint == 1:
            #agregar audio para alertar al usuario
            MessageBox.showwarning("Alerta",
                                   "Primero debes realizar el analisis lexico.")
        else:
            os.system("start C:\\LYA_SMARTCRIB-master\\codigo_fuente\\Audio\\Analisis_Sintactico.mp3")
            v.cSint = 1
            archivo = self.textEditor.get("1.0", tk.END)
            sint = aS.archivo(archivo)
            self.textSintaxis.delete("1.0", tk.END)
            self.textSintaxis.insert("1.0", sint)
            v.resultado = ''
        

    def visualizar(self):
         c.encenderCamara()
    def guardar(self):
        nombrearch=fd.asksaveasfilename(initialdir = "C:/LYA_SMARTCRIB-master/Codigo_Fuente/Toxic/",title = "Guardar como",filetypes = (("Toxic Files","*.txc"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.textEditor.get("1.0", tk.END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en el archivo.")

    def abrir(self):
        nombrearch=fd.askopenfilename(initialdir = "C:/LYA_SMARTCRIB-master/Codigo_Fuente/Toxic/",title = "Seleccione archivo",filetypes = (("Toxic Files","*.txc"),("todos los archivos","*.*")))
        if nombrearch!='':
            archi1=open(nombrearch, "r", encoding="utf-8")
            contenido=archi1.read()
            archi1.close()
            self.textEditor.delete("1.0", tk.END)
            self.textEditor.insert("1.0", contenido)
        content =nombrearch
          

    def convertirSonido(self):
        nombrearch=fd.askopenfilename(initialdir = "C:/LYA_SMARTCRIB-master/Codigo_Fuente/Audio/VozToText",title = "Seleccione archivo",filetypes = (("WAV Files","*.wav"),("todos los archivos","*.*")))
        test = nombrearch
        conv = vo.obtener(test)
        self.textEditor.insert("1.0", conv)

aplicacion1=Aplicacion()