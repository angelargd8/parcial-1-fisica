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
        self.geometry("1000x900")
        self.title("🤑 Parcial 1 🤑")
        self.config(bg="#ffafcc")

        #objetos
        self.l1=Label(text="Radio:");self.l1.place(x=10,y=10); self.l1.config(bg="#ffc2d1")
        self.e1=Entry(self);self.e1.place(x=85,y=10)

        self.l2=Label(text="Distancia x:");self.l2.place(x=10,y=50); self.l2.config(bg="#ffddd2")
        self.e2=Entry(self);self.e2.place(x=85,y=50)

        self.l3=Label(text="Carga:");self.l3.place(x=10,y=90); self.l3.config(bg="#ff8fab")
        self.e3=Entry(self);self.e3.place(x=85,y=90)
        
        btn1= Button(self, text="Anillo", width=15,command=self.Anillo, bg="#ffc2d1");btn1.place(x=350,y=10)
        btn2=Button(self, text="Disco", width=15, command=self.Disco, bg="#ffddd2");btn2.place(x=350,y=50)
        btn3=Button(self, text="Linea de carga", width=15, command=self.LineaDeCarga,bg="#ff8fab");btn3.place(x=350,y=90)

        self.l4=Label(text="integral anillo:");self.l4.place(x=10,y=130); self.l4.config(bg="#ffc2d1")
        self.l5=Label(text="");self.l5.place(x=10,y=170); self.l5.config(bg="#ff8fab")
        self.l6=Label(text="resultado anillo:");self.l6.place(x=10,y=210); self.l6.config(bg="#ffc2d1")
        self.l7=Label(text="");self.l7.place(x=10,y=250); self.l7.config(bg="#ff8fab")

        self.l8=Label(text="integral disco:");self.l8.place(x=10,y=290); self.l8.config(bg="#ffc2d1")
        self.l9=Label(text="");self.l9.place(x=10,y=320); self.l9.config(bg="#ff8fab")
        self.l10=Label(text="resultado disco:");self.l10.place(x=10,y=350); self.l10.config(bg="#ffc2d1")
        self.l11=Label(text="");self.l11.place(x=10,y=390); self.l11.config(bg="#ff8fab")

        self.l12=Label(text="integral linea de carga:");self.l12.place(x=10,y=450); self.l12.config(bg="#ffc2d1")
        self.l13=Label(text="");self.l13.place(x=10,y=480); self.l13.config(bg="#ff8fab")
        self.l14=Label(text="resultado linea de carga:");self.l14.place(x=10,y=510); self.l14.config(bg="#ffc2d1")
        self.l15=Label(text="");self.l15.place(x=10,y=550); self.l15.config(bg="#ff8fab")

        #canvas
        self.c1 = Canvas(self, width=800, height=500, bg="white")
        self.c1.place(x=190, y=150)
        self.c1.config(bg="misty rose")



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
                self.limpiar()
                self.grafica()
                self.graficarAnillo()
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
        
        self.radio = float (self.e1.get())
        self.x = float(self.e2.get()) #distancia
        self.Carga = float(self.e3.get())
        if self.radio>0 and self.x>0:
                self.graficarDisco()
                #variables a usar
                self.constanteK= 9*10**9
                #campo = E, dE= DiferencialDeCampo, dq= DiferencialDeCarga, a= radio, r= distancia de diferencial de carga al punto, x= distancia
                #self.Campo, self.DiferencialDeCampo, self.DiferencialDeCarga, self.r, self.x, self.a, self.Carga
                
                #self.R= sqrt(self.radio ** 2 + self.x ** 2)
                #self.r = symbols("r")
                #deduccion
                #derivada del campo dE
                #para que use variables, no los numeros
                self.Carga= symbols('Q')
                self.diferencialDeCarga= symbols('dq') #diferencial de carga
                self.sigma = symbols("σ") # sigma 
                self.diferencialDeRadio = symbols("dr") # diferencial de radio
                self.constanteK, self.r , self.x, self.a = symbols('K r x a', positive=True, real=True) 
                
                #calculo de dE
                self.Campo= self.constanteK * ((self.Carga*self.x)/(pow((pow(self.r,2))+(pow(self.x,2)),(3/2))))
                self.DiferencialDeCampo= diff(self.Campo, self.Carga)* self.diferencialDeCarga #dE= K/r^2 *dq
                print("dE:",self.DiferencialDeCampo)

                #reemplazar dq por (σ*2*pi*r dr)
                self.r_expresion= self.sigma * 2 * pi* self.r * self.diferencialDeRadio
                self.DiferencialDeCampo = self.DiferencialDeCampo.subs(self.diferencialDeCarga,self.r_expresion )
                print("expresion: ",self.DiferencialDeCampo )

               
                #integrar la expresion
                self.expresion_integrar = self.DiferencialDeCampo.subs(self.diferencialDeRadio, 1) # para integrar en sympy no se necesita del diferencial, solo se utiliza para la notación 
                #antes de integrar sustituir x
                #self.expresion_integrar = self.DiferencialDeCampo.subs(self.x, self.e2.get())
                #print("expresssion: ", self.expresion_integrar ) 
                self.integral = integrate(self.expresion_integrar, self.r)
                self.integralValuada = integrate(self.expresion_integrar, (self.r, 0, self.radio))
                print("integral: ", self.integral )
                print("integral: ", self.integralValuada )
                self.l4.config(text="Integral de Disco")
                self.l5.config(text=self.integral)

                #reemplazar las variables y calcular el valor
                self.valorSigma =  float(self.e3.get())/(pi*(self.radio)**2)
                print(self.valorSigma)
                self.resultadoDisco= self.integralValuada.subs({ self.x : float(self.e2.get()), self.constanteK: 9*10**9, self.sigma: self.valorSigma, self.r: self.radio})
                print("resultado: ", self.resultadoDisco,"\n" )
                #self.l7.config(text=self.resultadoAnillo)


            

        else:
            messagebox.showerror("error", "asegurese de ingresar un número validoy todos los valores") 

       


    def LineaDeCarga(self):
            #calcular el campo electrico en el punto P del eje x
            #deducir la ecuacion de E
            #ecuaciones utiles: 
            """
            E = K * q/r^2
            dE = K * dq/r^2
            Cos= adyacente/hipotenusa = x/r
            r= sqrt(a^2+x^2)
            dq = λ*dy
            λ = q/2a
            """
            self.a = float (self.e1.get())
            self.x = float(self.e2.get()) #distancia
            self.Carga = float(self.e3.get())
            if self.a>0 and self.x>0:
                self.limpiar()
                self.grafica()
                self.graficarLineaDeCarga()

                #variables a usar
                self.constanteK= 9*10**9
                #campo = E, dE= DiferencialDeCampo, dq= DiferencialDeCarga, a= radio, r= distancia de diferencial de carga al punto, x= distancia
                #self.Campo, self.DiferencialDeCampo, self.DiferencialDeCarga, self.r, self.x, self.a, self.Carga
                #self.r= sqrt(self.a ** 2 + self.x ** 2)
                #deduccion
                #derivada del campo dE
                #para que use variables, no los numeros
                self.Carga= symbols('Carga')
                self.diferencialDeCarga= symbols('dq') #diferencial de carga
                self.diferencialDeY= symbols('dy') #diferencial de carga
                self.constanteK, self.r , self.x, self.y, self.lamda = symbols('K r x y λ', positive=True, real=True) 
                
                #calculo de dE
                self.Campo= self.constanteK * (self.Carga/pow(self.r,2))
                self.DiferencialDeCampo= diff(self.Campo, self.Carga)* self.diferencialDeCarga #dE= K/r^2 *dq
                print("dE: ",self.DiferencialDeCampo)

                #sustituir r por su valor correspondiente
                self.DiferencialDeCampo = self.DiferencialDeCampo.subs({self.r: (self.x**2 + self.y**2)**(1/2), self.diferencialDeCarga: self.lamda*self.diferencialDeY})
                print("dE: ", self.DiferencialDeCampo)

                #Se sabe que dEx = dEcosα = dE(x/r)
                #Se sabe que dEy = -dEsenα = dE(y/r)

                #multiplicando para obtener dEx
                self.DiferencialDeCampo = self.DiferencialDeCampo*((self.x)/(self.x**2 + self.y**2)**(1/2)) 
                print("dE: ", self.DiferencialDeCampo)

                #integrando 
                self.expresion_integrar = self.DiferencialDeCampo.subs(self.diferencialDeY, 1)
                print("A integrar: ", self.expresion_integrar)
                self.integral =  integrate(self.expresion_integrar, self.y)
                self.integralValuada =  integrate(self.expresion_integrar, (self.y, -self.a, self.a ))
                print("Integral: ", self.integral)
                print("IntegralValuada: ", self.integralValuada)

            #self.a = float (self.e1.get())
            #self.x = float(self.e2.get()) #distancia
            #self.Carga = float(self.e3.get())
                #sustituir 
                self.integralF = self.integralValuada.subs({ self.constanteK: 9*10**9, self.lamda: float(self.e3.get())/(2*self.a), self.x :float(self.e2.get()) })
                print("Resultado: ", self.integralF)
                 
                





    def grafica(self):
        def f(x):
            return x**3 #x*tan(x), sin(x), cos(x)
        lix= -10#float(self.e1.get())
        lsx= 10 #float(self.e2.get())
        paso= (lsx-lix)/1000.0
        x = lix
        y = f(x)
        liy = lsy = y
        while (x<lsx):
            x = x+ paso
            y = f(x)
            if (y < liy):
                liy= y
            if ( y> lsy):
                lsy = y
        print(lix, lsx)
        def xp(vx):
            return int(( vx-lix) * self.c1.winfo_width() / (lsx-lix))
        def yp(vy):
            return int ((lsy - vy) * self.c1.winfo_height()/(lsy-liy))   
        self.c1.delete("all")
    
        #ejes
        self.c1.create_line(0, yp(0),self.c1.winfo_width(),yp(0), fill="red", width="2")
        self.c1.create_line(xp(0),0, xp(0), self.c1.winfo_height(), fill="red", width="2") 
        

    def graficarAnillo(self):
        #anillo
        x0 = (self.c1.winfo_width() - 140) / 2
        y0 = (self.c1.winfo_height() - 150) / 2
        x1 = x0 + 140
        y1 = y0 + 150
        self.c1.create_oval(x0,y0, x1, y1, width="3")
        #dE del anillo
        self.c1.create_line((self.c1.winfo_width() ) / 2, (self.c1.winfo_height()+ 150 )/2 , (self.c1.winfo_width()+650 ) / 2 ,(self.c1.winfo_height()- 30 )/2, fill="purple", width="2" )
        self.c1.create_line((self.c1.winfo_width() ) / 2, (self.c1.winfo_height()- 150 )/2 , (self.c1.winfo_width()+650 ) / 2 ,(self.c1.winfo_height()+ 30 )/2, fill="purple", width="2" )
        #punto del anillo
        self.c1.create_polygon([(self.c1.winfo_width()+550 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+550 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+550 ) / 2, (self.c1.winfo_height() )/2], outline='black', fill='black', width=10)

        #flechitas
        self.c1.create_polygon([(self.c1.winfo_width()+650 ) / 2, (self.c1.winfo_height()+35 )/2, (self.c1.winfo_width()+655 ) / 2, (self.c1.winfo_height() +10)/2, (self.c1.winfo_width()+665 ) / 2, (self.c1.winfo_height()+25 )/2], outline='red', fill='red', width=3)
        self.c1.create_polygon([(self.c1.winfo_width()+650 ) / 2, (self.c1.winfo_height()-35 )/2, (self.c1.winfo_width()+655 ) / 2, (self.c1.winfo_height() -10)/2, (self.c1.winfo_width()+665 ) / 2, (self.c1.winfo_height()-25 )/2], outline='red', fill='red', width=3)
        #texto 
        self.c1.create_text((self.c1.winfo_width()+550) / 2, (self.c1.winfo_height()- 40 )/2, text = "P", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+650) / 2, (self.c1.winfo_height()- 60 )/2, text = "dE", font = ("Arial", 10))
        self.c1.create_text((self.c1.winfo_width()+650) / 2, (self.c1.winfo_height()+ 60 )/2, text = "dE", font = ("Arial", 10))
        self.c1.create_text((self.c1.winfo_width()+300) / 2, (self.c1.winfo_height()+ 20 )/2, text = "x", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()-140) / 2, (self.c1.winfo_height()- 140 )/2, text = "dq", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+200) / 2, (self.c1.winfo_height()- 135 )/2, text = "r", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()-15) / 2, (self.c1.winfo_height()- 90 )/2, text = "a", font = ("Arial", 15))

    def graficarDisco(self):
        #anillo
        x0 = (self.c1.winfo_width() - 140) / 2
        y0 = (self.c1.winfo_height() - 150) / 2
        x1 = x0 + 140
        y1 = y0 + 150
        self.c1.create_oval(x0,y0, x1, y1, outline="red" ,width="3")
        #disco
        x0 = (self.c1.winfo_width() - 240) / 2
        y0 = (self.c1.winfo_height() - 250) / 2
        x1 = x0 + 240
        y1 = y0 + 250
        self.c1.create_oval(x0,y0, x1, y1, outline="purple" , width="3")
        #dE del disco
        self.c1.create_line((self.c1.winfo_width() ) / 2, (self.c1.winfo_height()+ 250 )/2 , (self.c1.winfo_width()+720 ) / 2 ,(self.c1.winfo_height()- 10 )/2, fill="purple", width="2" )
        self.c1.create_line((self.c1.winfo_width() ) / 2, (self.c1.winfo_height()- 250 )/2 , (self.c1.winfo_width()+750 ) / 2 ,(self.c1.winfo_height()+ 10 )/2, fill="purple", width="2" )
        #punto
        self.c1.create_polygon([(self.c1.winfo_width()+705 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+710 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+710 ) / 2, (self.c1.winfo_height() )/2], outline='black', fill='black', width=10)
        #flechita
        self.c1.create_polygon([(self.c1.winfo_width()+740 ) / 2, (self.c1.winfo_height()+10 )/2, (self.c1.winfo_width()+745 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+735 ) / 2, (self.c1.winfo_height()-10 )/2], outline='red', fill='red', width=3)
        #texto 
        self.c1.create_text((self.c1.winfo_width()+710) / 2, (self.c1.winfo_height()- 40 )/2, text = "P", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+750) / 2, (self.c1.winfo_height()- 50 )/2, text = "dE", font = ("Arial", 10))
        self.c1.create_text((self.c1.winfo_width()+300) / 2, (self.c1.winfo_height()+ 20 )/2, text = "x", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()-20) / 2, (self.c1.winfo_height()- 100 )/2, text = "R", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+20) / 2, (self.c1.winfo_height()- 170 )/2, text = "dR", font = ("Arial", 15))
        
    def graficarLineaDeCarga(self):
        #linea de carga
        self.c1.create_rectangle((self.c1.winfo_width()-50 ) / 2, (self.c1.winfo_height()+ 200 )/2,(self.c1.winfo_width()+50 )/2 , (self.c1.winfo_height()- 200 )/2, outline='purple', width="3")
        self.c1.create_rectangle((self.c1.winfo_width()-50 ) / 2, (self.c1.winfo_height()- 160 )/2,(self.c1.winfo_width()+50 )/2 , (self.c1.winfo_height()- 140 )/2, outline='blue', fill="blue", width="2")
        self.c1.create_line((self.c1.winfo_width() ) / 2, (self.c1.winfo_height()- 150 )/2 , (self.c1.winfo_width()+700 ) / 2 ,(self.c1.winfo_height() )/2, fill="purple", width="2" )
        #punto
        self.c1.create_polygon([(self.c1.winfo_width()+700 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+700 ) / 2, (self.c1.winfo_height() )/2, (self.c1.winfo_width()+700 ) / 2, (self.c1.winfo_height() )/2], outline='black', fill='black', width=10)
        #texto 
        self.c1.create_text((self.c1.winfo_width()-60 ) / 2, (self.c1.winfo_height()+ 220 )/2, text = "-a", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()-60 ) / 2, (self.c1.winfo_height()- 220 )/2, text = "a", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+300) / 2, (self.c1.winfo_height()+ 20 )/2, text = "x", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+560) / 2, (self.c1.winfo_height()- 20 )/2, text = "α", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+700) / 2, (self.c1.winfo_height()- 30 )/2, text = "P", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()-75) / 2, (self.c1.winfo_height()- 170 )/2, text = "dy", font = ("Arial", 15))
        self.c1.create_text((self.c1.winfo_width()+75) / 2, (self.c1.winfo_height()-170 )/2, text = "dq", font = ("Arial", 15))
        


    def limpiar(self):
        self.c1.delete("all")


            

    


app().mainloop()