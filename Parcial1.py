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
from sympy import *  #libreria para las derivadas e integrales

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

        self.l3=Label(text="Carga:");self.l3.place(x=10,y=90); self.l3.config(bg="#ff8fab")
        self.e3=Entry(self);self.e3.place(x=85,y=90)
        
        btn1= Button(self, text="Anillo", width=15,command=self.Anillo, bg="#ffc2d1");btn1.place(x=350,y=10)
        btn2=Button(self, text="Disco", width=15, command=self.Disco, bg="#ffb3c6");btn2.place(x=350,y=50)
        btn3=Button(self, text="Linea de carga", width=15, command=self.LineaDeCarga,bg="#ff8fab");btn3.place(x=350,y=90)

        self.l4=Label(text="integral anillo:");self.l4.place(x=10,y=130); self.l4.config(bg="#ffc2d1")
        self.l5=Label(text="");self.l5.place(x=10,y=170); self.l5.config(bg="#ff8fab")
        self.l6=Label(text="resultado anillo:");self.l6.place(x=10,y=210); self.l6.config(bg="#ffc2d1")
        self.l7=Label(text="");self.l7.place(x=10,y=250); self.l7.config(bg="#ff8fab")


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
   
        try: 
            self.radio = float (self.e1.get())
            self.x = float(self.e2.get()) #distancia
            self.Carga = float(self.e3.get())
            if self.radio>0 and self.x>0:
                #variables a usar
                self.constanteK= 9*10**9
                #campo = E, dE= DiferencialDeCampo, dq= DiferencialDeCarga, a= radio, r= distancia de diferencial de carga al punto, x= distancia
                #self.Campo, self.DiferencialDeCampo, self.DiferencialDeCarga, self.r, self.x, self.a, self.Carga
                self.r= sqrt(self.radio ** 2 + self.x ** 2)
                #deduccion
                #derivada del campo dE
                #para que use variables, no los numeros
                self.Carga= symbols('Carga')
                self.diferencialDeCarga= symbols('dq') #diferencial de carga
                self.constanteK, self.r , self.x, self.radio = symbols('K r x a', positive=True, real=True) 
                
                #calculo de dE
                self.Campo= self.constanteK * (self.Carga/pow(self.r,2))
                self.DiferencialDeCampo= diff(self.Campo, self.Carga)* self.diferencialDeCarga #dE= K/r^2 *dq
                print("dE:",self.DiferencialDeCampo)

                #debido a la geometria se puede decir que dE=2dEx, además que --> Cos= adyacente/hipotenusa = x/r
                self.DiferencialDeCampo = 2 * self.DiferencialDeCampo * (self.x/ self.r) 
                print("expresion ",self.DiferencialDeCampo )

                #reemplazar r por sqrt(a**2+x**2)
                self.r_expresion= sqrt(pow(self.radio,2)+pow(self.x,2))
                self.DiferencialDeCampo = self.DiferencialDeCampo.subs(self.r,self.r_expresion )
                print("expresion 2: ",self.DiferencialDeCampo )
                
                #integrar la expresion
                self.q=symbols('q')
                self.expresion_integrar = self.DiferencialDeCampo.subs(self.diferencialDeCarga,1) # 1 por la diferencial 
                self.integral = integrate(self.expresion_integrar, (self.diferencialDeCarga, 0, (self.q/2) ))

                print("integral: ", self.integral )
                self.l3.config(text="Integral de Anillo")
                self.l5.config(text=self.integral)

                #reemplazar las variables y calcular el valor
                self.resultadoAnillo= self.integral.subs({self.radio: float (self.e1.get()), self.q: float(self.e3.get()), self.x : float(self.e2.get()), self.constanteK: 9*10**9 })
                print("resultado: ", self.resultadoAnillo ,"\n")
                self.l7.config(text=self.resultadoAnillo)

            

            else:
                messagebox.showerror("error", "asegurese de ingresar un número validoy todos los valores") 

        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número validoy todos los valores")

    def Disco(self):
        #calcular el campo electrico en el punto P del eje x
        #deducir la ecuacion de E
        #ecuaciones utiles: 
        """
        Campo electrico de un anillo 
        E = K*q*x/(a**2 + x**2)**(3/2) 
        dE = K*dq*x/(a**2 + x**2)**(3/2)
        Cos= adyacente/hipotenusa = x/r
        r= sqrt(a^2+x^2)
        dq = σdA
        """
        try: 
            self.radio = float (self.e1.get())
            self.x = float(self.e2.get()) #distancia
            self.Carga = float(self.e3.get())
            if True:#self.radio>0 and self.x>0:
                
                #variables a usar
                self.constanteK= 9*10**9
                #campo = E, dE= DiferencialDeCampo, dq= DiferencialDeCarga, a= radio, r= distancia de diferencial de carga al punto, x= distancia
                #self.Campo, self.DiferencialDeCampo, self.DiferencialDeCarga, self.r, self.x, self.a, self.Carga
                
                self.R= sqrt(self.radio ** 2 + self.x ** 2)
                self.r = symbols("r")
                #deduccion
                #derivada del campo dE
                #para que use variables, no los numeros
                self.Carga= symbols('Carga')
                self.diferencialDeCarga= symbols('dq') #diferencial de carga
                self.sigma = symbols("σ") # sigma 
                self.diferencialDeRadio = symbols("dr") # diferencial de radio
                self.constanteK, self.r , self.x, self.radio = symbols('K r x a', positive=True, real=True) 
                
                #calculo de dE
                self.Campo= self.constanteK * ((self.Carga*self.x)/(pow(pow(self.r,2)+pow(self.x,2),(3/2))))
                self.DiferencialDeCampo= diff(self.Campo, self.Carga)* self.diferencialDeCarga #dE= K/r^2 *dq
                print("dE:",self.DiferencialDeCampo)

                #reemplazar dq por (σ*2*pi*r dr)
                self.r_expresion= self.sigma * 2 * pi* self.r * self.diferencialDeRadio
                self.DiferencialDeCampo = self.DiferencialDeCampo.subs(self.diferencialDeCarga,self.r_expresion )
                print("expresion: ",self.DiferencialDeCampo )
                
                #integrar la expresion
                self.expresion_integrar = self.DiferencialDeCampo.subs(self.diferencialDeRadio, 1) # para integrar en sympy no se necesita del diferencial, solo se utiliza para la notación 
                self.integral = integrate(self.expresion_integrar, self.r)
                self.integralValuada = integrate(self.expresion_integrar, (self.r, 0, self.R))
                print("integral: ", self.integral )
                print("integral: ", self.integralValuada )
                self.l3.config(text="Integral de Disco")
                self.l5.config(text=self.integral)

                #reemplazar las variables y calcular el valor
                #self.integralValuada = integralValuada.subs()
                self.resultadoDisco= self.integral.subs({ self.x : float(self.e2.get()), self.constanteK: 9*10**9, self.sigma : float(self.e3.get()/(2*float(self.e1.get()),))})
                print("resultado: ", self.resultadoDisco )
                #self.l7.config(text=self.resultadoAnillo)

            

            else:
                messagebox.showerror("error", "asegurese de ingresar un número validoy todos los valores") 

        except Exception as msg: 
            messagebox.showerror("error", "asegurese de ingresar un número valido todos los valores")



    def LineaDeCarga(self):
        pass

    


app().mainloop()