import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Franco 
apellido: Gil 
---
Ejercicio: entrada_salida_09bis
---
Enunciado:
Al presionar el botón 'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        Sueldo_ingresado = self.txt_sueldo.get()
       
        Porcentaje_ingresado = self.txt_incremento.get()
       
        Sueldo_en_numero = float(Sueldo_ingresado)
       
        Porcentaje_en_numero = float(Porcentaje_ingresado)
       
        Porcentaje_solicitado = Sueldo_en_numero * Porcentaje_en_numero / 100
       
        Sueldo_con_porcentaje = Sueldo_en_numero + Porcentaje_solicitado
       
        Sueldo_y_porcentaje_aplicado = alert(title = "Su sueldo, con su porcentaje aplicado es: ",
                                             message = f"$ {Sueldo_con_porcentaje}") 

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()