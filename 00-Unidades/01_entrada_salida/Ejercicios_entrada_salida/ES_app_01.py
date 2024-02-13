import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Franco 
apellido: Gil
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        edad = 22 # variable del tipo entero
        # pep8: no se debe usar el + para concatenar strings 
        # snake_case: nombre de variable
        #promedio_edad_jugadores_futbol = 23.3 # variable del tipo float

        #apellido = None # variable del tipo None 
        
        #print (nombre)
        
        #nombre = 11 # variable del tipo entero

        #ingreso = True # booleano
        #ingreso = False # booleano
        
        #print(nombre)
        
        #title = "Hola PY"
        
        #message =  "Esto es una alerta para mostrar un mensaje"
        
        #alert(title,message) #muestra un mensaje en una ventana emergente 
        
        #alert("Hola PY", "Esto es una alert para mostrar un mensaje")

        #respuesta_usuario = question("Hola", "Esto no es pregunta")

        #print(respuesta_usuario)

        #Nombre_ingresado = prompt("Ingrese su nombre", "Nombre")
        
        #print(Nombre_ingresado)

        #alert("Su nombre es", Nombre_ingresado)

        dolar_blue = int(prompt("Coti blue","Numero"))
        dolar_oficial = int(prompt("Coti oficial", "Numero"))  
        diferncia_dolar = dolar_blue - dolar_oficial 
        porcentaje = diferncia_dolar * 100 / dolar_oficial
        alert("Numero", porcentaje)

       







if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
