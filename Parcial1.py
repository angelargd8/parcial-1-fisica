# Parcial 1 fisica 3
# descripcion: Realice una interfaz grafica para obtener el valor de un campo electrico (anillo, disco, linea de carga)
# autores:  Francis Aguilar #222432
#           Angela García   #22869
# recursos: python 3.10
# sin modificaciones
# librerias:
from tkinter import * 
from tkinter import messagebox
from math import sin, cos, tan 
from sympy import *  #libreria para las integrales

class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._root = Frame() #crea el frame principal
        self.geometry("600x400")
        self.title("🤑 Parcial 1 🤑")
        self.config(bg="#ffe5ec")

        #objetos
        self.l1=Label(text="Radio:");self.l1.place(x=10,y=10); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self);self.e1.place(x=85,y=10)

        self.l2=Label(text="Largo:");self.l2.place(x=10,y=50); self.l2.config(bg="#ffb3c6")
        self.e2=Entry(self);self.e2.place(x=85,y=50)
        
        btn1= Button(self, text="Anillo", width=15,command=self.Anillo, bg="#ffc2d1");btn1.place(x=350,y=10)
        btn2=Button(self, text="Disco", width=15, command=self.Disco, bg="#ffb3c6");btn2.place(x=350,y=50)
        btn3=Button(self, text="Linea de carga", width=15, command=self.LineaDeCarga,bg="#ff8fab");btn3.place(x=350,y=90)



    def Anillo(self):
        #calcular el campo electrico en el punto P del eje x
        #deducir la ecuacion de E
        #ecuaciones utiles: 
        """
        E = K * q/r^2
        dE = K * dq/r^2
        Cos= adyacente/hipotenusa = x/r
        r= sqrt(a^2+x^2)
        """
   
        #try: 
        self.radio = float (self.e1.get())

        if self.radio>0:
            #variables a usar
            self.constanteK= 9*10**9
            #campo = E, dE= DiferencialDeCampo, dq= DiferencialDeCarga, a= radio, r= distancia de diferencial de carga al punto, x= distancia
            #self.Campo, self.DiferencialDeCampo, self.DiferencialDeCarga, self.r, self.x, self.a, self.Carga
            self.r=-1
            #deduccion
            #derivada del campo dE
            self.Carga= symbols('self.Carga')
            self.diferencialDeCarga= symbols('dq') #diferencial de carga
            self.constanteK, self.r = symbols('constanteK r', positive=True, real=True)
            self.Campo= self.constanteK * (self.Carga/pow(self.r,2))
            self.DiferencialDeCampo= diff(self.Campo, self.Carga)* self.diferencialDeCarga
           
           
            #self.r= sqrt(pow(self.radio,2)+pow(self.x,2))
            
            
            messagebox.showinfo("dE:",self.DiferencialDeCampo)

        else:
            pass    

        #except Exception as msg: 
        #    messagebox.showerror("error", "ingrese un número valido")

    def Disco(self):
        pass

    def LineaDeCarga(self):
        pass

    


app().mainloop()