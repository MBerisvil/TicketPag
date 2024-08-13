import tkinter as tk
from reportlab.pdfgen import canvas
from os import system
import datetime
import time



class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("700x500")# tamaño de la ventana
        self.title("TicketPag" + " / " + str(datetime.date.today()))  # título de la ventana
        self.iconbitmap("img/logo.ico")  # icono de la ventana
        label = tk.Label(self, text=" Sistema de Ticket de Alquiler", pady=8, font=("Arial", 14))
        label.pack()
        #button = tk.Button(self, text="Cerrar", command=self.destroy)
        #button.pack()

        
        if datetime.date.today().weekday() == 0 or datetime.date.today().weekday() == 6:
            label = tk.Label(self, text="Hoy es fin de semana, \n no se puede generar ticket", font=("Arial", 14, "bold"), fg="#Df1313")
            label.place(x=300, y=210)

        else:
        #Datos de transferencias
            label = tk.Label(self, text=" Datos de Transferencia: ", pady=8, font=("Arial", 12, "bold"), fg="#298B09")
            label.place(x=360, y=180)
            cbu = tk.Label(self, text="CBU:  ", fg="#298B09")
            cbu.place(x=368, y=220)
            alias = tk.Label(self, text="Alias:  ", fg="#298B09")
            alias.place(x=368, y=240)
            banco = tk.Label(self, text="Banco:  ", fg="#298B09")
            banco.place(x=368, y=260)
            titular = tk.Label(self, text="Titular:  ", fg="#298B09")
            titular.place(x=368, y=280)

            ticket = tk.Label(self, text="Ticket N°:000", font=("Arial", 10, "italic"))
            ticket.place(x=520, y=50)





        def generar_pdf():
            #Generar ticket en pdf
            pdf_file = canvas.Canvas((str(edificio.get())) + " - TicketPag.pdf", pagesize="A7")
            # Agrega texto al PDF
            pdf_file.drawImage("img/logo1.jpg", 540, 710, width=60, height=60)
            pdf_file.drawString(50, 735, "Fecha: " + str(datetime.date.today()))
            pdf_file.drawString(50, 710, "ALQUILER - " + str(edificio.get()))
            pdf_file.drawString(50, 660, "Cliente: " + str(cliente.get()))
            pdf_file.drawString(50, 630, "DNI: " + str(dni.get()))
            pdf_file.drawString(50, 600, "Alquiler: $" + str(alquiler.get()))
            pdf_file.drawString(50, 570, "Expensas: $" + str(expensas.get()))
            pdf_file.drawString(50, 540, "Servicios de electricidad: $" + str(epec.get()))
            pdf_file.drawString(50, 510, "Servicios de agua: $" + str(agua.get()))
            pdf_file.drawString(50, 480, "Servicios de gas: $" + str(servgas.get()))
            pdf_file.drawString(50, 440, "Total a pagar: $ " + str(total.get()))
            pdf_file.drawString(50, 400, "============================================================")
            pdf_file.drawString(50, 380, "Datos de transferencia: ")
            pdf_file.drawString(50, 360, "============================================================")
            pdf_file.drawString(50, 340, "Titular:  " )
            pdf_file.drawString(50, 310, "CBU:  " )
            pdf_file.drawString(50, 280, "Alias:  " )
            pdf_file.drawString(50, 250 ,"Entidad bancaria:  " )
            # Guardar y cierra el archivo PDF
            pdf_file.save()
            pdf_file.showPage()
        
        def suma():
            suma = int(alquiler.get()) + int(expensas.get()) + int(epec.get()) + int(agua.get()) + int(servgas.get())
            return total.set(suma)


        #declaro variable de suma
        total = tk.StringVar()


        label = tk.Label(self, text=" Datos de cliente y edificio.", pady=8, font=("Arial", 12, "italic"))
        label.place(x=10, y=50)
        #registro de variable nombre edificio
        nedificio = tk.Label(self, text="Edificio: ", font=("Arial", 10,))
        nedificio.place(x=15, y=100)
        edificio = tk.Entry(self)
        edificio.place(x=115, y=100)

        ncliente = tk.Label(self, text="Cliente: ", font=("Arial", 10,))
        ncliente.place(x=15, y=135)
        cliente= tk.Entry(self)
        cliente.place(x=115,y=135)       

        ndni = tk.Label(self, text="Dni del cliente: ", font=("Arial", 10,))
        ndni.place(x=15, y=175)
        dni = tk.Entry(self)
        dni.place(x=115, y=177)

        #registro de variable servicios
        label = tk.Label(self, text=" Datos de servicios.", pady=8, font=("Arial", 12, "italic"))
        label.place(x=10, y=210)

        nalquiler = tk.Label(self, text="Alquiler $")
        nalquiler.place(x=15, y=260)
        alquiler= tk.Entry(self)
        alquiler.place(x=115, y=260)

        nexpensas = tk.Label(self, text="Expensas $")
        nexpensas.place(x=15, y=296)
    
        expensas = tk.Entry(self,)
        expensas.place(x=115, y=296)

        nepec = tk.Label(self, text="Serv. de luz $")
        nepec.place(x=15, y=329)
        epec = tk.Entry(self)
        epec.place(x=115, y=329)

        nagua = tk.Label(self, text="Serv. de agua $")
        nagua.place(x=15, y=365)
        agua = tk.Entry(self)
        agua.place(x=115, y=365)

        nservgas = tk.Label(self, text="Serv. de gas $")
        nservgas.place(x=15, y=398)
        servgas = tk.Entry(self)
        servgas.place(x=115, y=398)


        #Boton de generar ticket
        label = tk.Label(self, text="Total a pagar $ :  ", pady=8, font=("Arial", 12, "italic"))
        label.place(x=10, y=440)
        total_sum = tk.Label(self, textvariable= total, font=("Arial", 12, "bold"),fg="#Df1313")
        total_sum.place(x=140, y=448)


        #boton de generar sumar
        generar = tk.Button(self, text="Calcular", command=suma, background="#3188f0", font=("Arial", 8, "bold"))
        generar.place(x=492, y=440)
        #boton de generar ticket
        generar = tk.Button(self, text="Generar PDF", command=generar_pdf, background="#298B09", font=("Arial", 8, "bold"))
        generar.place(x=550, y=440)
        #boton de salir
        salir = tk.Button(self, text="Salir", command=self.destroy, background="#DE0001", font=("Arial", 8, "bold"))
        salir.place(x=632, y=440)


if __name__ == "__main__":
    app = App()
    app.mainloop()