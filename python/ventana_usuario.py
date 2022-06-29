from doctest import master
import math
from gestor_aplicacion.gestion.catalogo import Catalogo
from gestor_aplicacion.gestion.Desarrollador import Desarrollador
from gestor_aplicacion.gestion.Dian import Dian
from gestor_aplicacion.gestion.Empresa import Empresa
from gestor_aplicacion.gestion.Gobierno import Gobierno
from gestor_aplicacion.gestion.Rango import Rango
from gestor_aplicacion.gestion.tarjeta import Tarjeta
from gestor_aplicacion.gestion.Videojuego import Videojuego
#########################
from gestor_aplicacion.personas.cliente import Cliente
from gestor_aplicacion.personas.Persona import Persona
from gestor_aplicacion.personas.Empleado import Empleado
from uiMain.inicio import Inicio
from uiMain.ventana_exception import ExceptionPopUp
from uiMain.error_aplicacion import ErrorAplicacion
from uiMain.ciente_nf_exception import ClienteException
from baseDatos.serializador import Serializador
'''
t1=Tarjeta(1001,5000)
t2=Tarjeta(2378,1233)
t3=Tarjeta(7410,2344)
t4=Tarjeta(8806,3007)
t5=Tarjeta(6960,990)
tc1=Tarjeta(9944,5200)
tc2=Tarjeta(6960,990)
tc3=Tarjeta(3390,1556)
tc4=Tarjeta(2012,2000)
tc5=Tarjeta(4467,10050)
td1=Tarjeta(4400,10000)
td2=Tarjeta(5003,25000)
td3=Tarjeta(7791,20700)


dian=Tarjeta(7891,0)
Dian.tarjetal2([dian])

te=Tarjeta(1709,10000)
Empresa.setTarjeta([te])


e1= Empleado("Juan Carlos Zapata",10101000,30,t1,100,"Vendedor",25)
e2= Empleado("Tatiana Perea",12101509,22,t2,100,"Vendedor",40)
e3= Empleado("Oscar suarez",10351022,37,t3,100,"  Vendedor",0)
e4= Empleado("Pablo Rodriguez",10257622,40,t4,100,"  Vendedor",50)
e5= Empleado("Gustavo Fring",66078005,28,t5,100,"  Vendedor",100)

D1=Desarrollador("ubisoft",td1,0.3)
D2=Desarrollador("ubisoft",td2,0.45)
D3=Desarrollador("ubisoft",td3,0.1)


v1=  Videojuego("Terror","silent hill" ,50.35, 10, D1, "+18",1)
v2=  Videojuego("Aventura","uncharted" ,60.15, 10, D1, "+12",1)
v3=  Videojuego("Carreras","forza horizon" ,35.70, 10, D3, "+7",1)
v4=  Videojuego("Aventura","minecraft" ,45.35, 10, D3, "+3",1)
v5=  Videojuego("Deportes","fifa" ,62.01, 10, D1, "+7",1)
v6=  Videojuego("Accion","call of duty" ,70.15, 10, D2, "+18",1)
v7=  Videojuego("Familiar","los sims" ,20.45, 10, D3, "+3",1)
v8=  Videojuego("Accion","dark souls" ,50.09, 10, D1, "+16",1)
v9=  Videojuego("Aventura","crash bandicoot" ,39.95, 10, D2, "+12",1)
v10=  Videojuego("Accion","gta v" ,70.45, 10, D1, "+18",1)

D1.getVideojuegos().append(v1)
D1.getVideojuegos().append(v2)
D1.getVideojuegos().append(v5)
D1.getVideojuegos().append(v8)
D1.getVideojuegos().append(v10)
D2.getVideojuegos().append(v9)
D3.getVideojuegos().append(v3)
D3.getVideojuegos().append(v4)
D3.getVideojuegos().append(v6)
D3.getVideojuegos().append(v7)

catalogo=[]
catalogo.append(v1)
catalogo.append(v2)
catalogo.append(v8)
catalogo.append(v5)
catalogo.append(v10)
ci= Catalogo()
Catalogo.setVideojuegos(catalogo)


c1= Cliente("Marco Aurelio Gomez",100,22,tc1,20)
c2= Cliente("Jeronimo Zapata",200,16,tc2,15)
c3= Cliente("Didier Herrera",300,30,tc3,30)
c4= Cliente("Miguel Angel Vera",400,45,tc4,20)
c5= Cliente("Santiago Marulanda",500,27,tc5,50)


Empresa.setListaDesarrolladores([D1])

c1.comprarVideojuego("silent hill")
c1.comprarVideojuego("uncharted")

c2.comprarVideojuego("gta v")


c3.comprarVideojuego("fifa")
c3.comprarVideojuego("dark souls")'''

'''print(e1.getTarjeta().getSaldo())
print(e2.getTarjeta().getSaldo())
print(Empresa.pagarEmpleados())
print(e1.getTarjeta().getSaldo())
print(e2.getTarjeta().getSaldo())
print(Empresa.pagarEmpleados())
print("Se lleva pagado a la Dian un total de "+str(Dian.getTarjeta1().getSaldo()))'''


'''print(Empresa.revisionMensual())
print(Empresa.revisionMensual())'''
###################################################
#####################################################3
#######################################################
###########################################################
import tkinter as tk;
from tkinter import E, Frame,INSERT,Entry,scrolledtext,Label,BOTH
import tkinter.scrolledtext as st
from uiMain.fielfdFrame import FieldFrame
#from uiMain.ventana_inicio.ventana import Ventana
from uiMain.user_exception import UserException
from uiMain.exception_pop import ExceptionPopUp
from uiMain.cash_exception import CashException
from uiMain.value_error import Value_error

def ventana_principal():
  #VEntana principal
  ventana=tk.Tk()
  ventana.title("XGames")
  ventana.geometry("1100x720")
  ventana.option_add("*tearOff",False)



  matar=[]
  def matarlo(frameUtilizado):
    for i in matar:
        i.pack_forget()
    frameUtilizado.pack(fill=BOTH,expand=True)


  #ventana de inicio
  VentanaInicio=Inicio(ventana)
  matarlo(VentanaInicio)
  matar.append(VentanaInicio)


  def aplicacionPop():  ####3
    aplicacion=tk.Toplevel(ventana)
    aplicacion.geometry("580x320")
    aplicacion.title("Aplicacion")
    texto="Xgames es una empresa especialista en venta y distribucion de videojuegos.\nEn los ultimos años la compañia se ha centrado principalmente en vender sus juegos de forma digital.\nPor lo que surge esta aplicacion con el objetivo de una mejor gestion del proceso de ventas de manera digital.\nDentro de esta aplicacion se lleva cuenta de todo el proceso de compra de los videojuegos, \ndesde el cliente que lo compra, hasta el dinero que recibe la empresa y los desarrolladores del juego."
    Label(aplicacion, text= texto , font=('Times 8')).pack(fill=BOTH, expand=True)
    aplicacion.mainloop()
  
  def ayudaPop(): ###4
    ayuda= tk.Toplevel(ventana)
    ayuda.grid_rowconfigure(0, weight=1)
    ayuda.geometry("450x250")
    ayuda.title("Ayuda")
    Label(ayuda, text= "AUTORES\nJean Carlo Montoya Castro \nSimon Henao Angarita\nMichael Steven Ramirez Reyes\nJuan Jose Garcia Vasquez", font=('Times 18 bold')).pack(fill=BOTH, expand=True)
    ayuda.mainloop()
  def exit(): ####5
    from uiMain.ventana import ventanaInicio
    Serializador.serializarTodo()
    matar = []
    ventana.destroy()
    ventana_inicio = ventanaInicio()
    ventana_inicio.mainloop()
  

  def popUp(x,y):
    aplicacion=tk.Toplevel(ventana)
    aplicacion.geometry("580x320")
    aplicacion.title(x)
    Label(aplicacion,text=y)
    aplicacion.mainloop()




##########################################################################
  def creadores():
    frame=Frame(ventana)
    frame.place(relx=0,rely=0, relwidth=1, relheight=1)
    texto = st.ScrolledText(frame,width =40, height = 10, font = ("Times New Roman",15))
    texto.insert(INSERT,"Creadores:"+"\n"+"Jean Carlo Montoya Castro-1000872579"+"\n"+"Juan José García Vásquez-1001237547"+"\n"+"Simon Henao Angarita-1000872910"+"\n"+"Michael Steven Ramirez Reyes-1001139994")
    texto.place(relx=0,rely=0, relwidth=1, relheight=1)
    matarlo(frame)
    matar.append(frame)


############################################################################
  def detalles():
    frame=Frame(ventana)
    frame.place(relx=0,rely=0, relwidth=1, relheight=1)
    texto = st.ScrolledText(frame,width =40, height = 10, font = ("Times New Roman",15))
    texto.insert(INSERT,Empresa.revision())
    texto.place(relx=0,rely=0, relwidth=1, relheight=1)
    matarlo(frame)
    matar.append(frame)
###########################################################################
  def detallesEmpresa():
    c="Empresa XGames"+"\n"+"Saldo global :"+str(Empresa.getTarjeta().getSaldo())+"\n"+"Numero de empleados actuales: "+str(len(Empresa.getListaEmpleados()))+"\n" +"Numero de clientes activos: "+str(len(Empresa.getListaClientes()))+"\n"+"Numero de desarrolladores actuales: "+str(len(Empresa.getListaDesarrolladores()))
    frame=Frame(ventana)
    frame.place(relx=0,rely=0, relwidth=1, relheight=1)
    texto = st.ScrolledText(frame,width =40, height = 10, font = ("Times New Roman",15))
    texto.insert(INSERT,c)
    texto.place(relx=0,rely=0, relwidth=1, relheight=1)
    matarlo(frame)
    matar.append(frame)
##############################################################
  def mostrarCatalogo():
    c=Cliente()
    x=str(c.verCatalogo())
    frame=Frame(ventana)
    frame.place(relx=0,rely=0, relwidth=1, relheight=1)
    texto = st.ScrolledText(frame,width =40, height = 10, font = ("Times New Roman",15))
    texto.insert(INSERT,x)
    texto.place(relx=0,rely=0, relwidth=1, relheight=1)
    matarlo(frame)
    matar.append(frame)
    ######################################################################

  def pagar():

    frame=Frame(ventana)
    frame.place(relx=0,rely=0, relwidth=1, relheight=1)
    texto = st.ScrolledText(frame,width =40, height = 10, font = ("Times New Roman",15))
    texto.insert(INSERT,Empresa.pagarEmpleados())
    texto.place(relx=0,rely=0, relwidth=1, relheight=1)
    matarlo(frame)
    matar.append(frame)
  ############################################################################
  def bonificacion():
    frame=Frame(ventana)
    frame.place(relx=0,rely=0, relwidth=1, relheight=1)
    texto = st.ScrolledText(frame,width =40, height = 10, font = ("Times New Roman",15))
    texto.insert(INSERT,Empresa.revisionMensual())
    texto.place(relx=0,rely=0, relwidth=1, relheight=1)
    matarlo(frame)
    matar.append(frame)
  ########################################################################################
  bonificar=Frame(ventana,bd=10)
  nombre = Label(bonificar, text="Información de cliente específico", bd= 10)
  nombre.pack()
  descripcion = Label(bonificar, text="Diligenciar la cédula del cliente que desea ver la informacion", bd= 20)
  descripcion.pack()
  clienteespecifico=FieldFrame(bonificar,"Criterios",["Cedula Cliente"],"Valor",[None],[],[1])
  clienteespecifico.pack()


  def x():
    try:
      aplicacion=tk.Toplevel(ventana)
      aplicacion.geometry("580x320")
      aplicacion.title("Aplicacion")
      clienteespecifico.validacion()
      texto=int(clienteespecifico._entries[0].get())  
      cc=""
      for cliente in Empresa.getListaClientes():
        if cliente.getDocumento()==texto:
          c="Nombre: "+cliente.getNombre()+"\n"+"Edad:"+ str(cliente.getEdad())+"\n"+"Saldo: "+str(cliente.getTarjeta().getSaldo())+"\n"+"Juegos:" +cliente.juegos()
          y=Label(aplicacion, text= c , font=('Times 12')).pack(fill=BOTH, expand=True)
          aplicacion.mainloop()
          return

    except ErrorAplicacion as e:
            aplicacion.destroy()
            ExceptionPopUp(str(e))
  def clienteespecifico1():
    clienteespecifico.crearBotones(x)
    matarlo(bonificar)
    matar.append(bonificar)
    

####################################################################################
  bonificarv=Frame(ventana,bd=10)
  nombrevid = Label(bonificarv, text="Añadir Videojuego", bd= 10)
  nombrevid.pack()
  descripcionvid = Label(bonificarv, text="Añadir manualmente un nuevo videojuego", bd= 20)
  descripcionvid.pack()
  framev=FieldFrame(bonificarv,"Criterios",["Genero videojuego","Nombre","Precio","Desarrollador","Clasificacion"],"Valor",["","","","",""],[],[0,0,1,0,0])
  framev.pack()

  def y():
    try:
        aplicacion=tk.Toplevel(ventana)
        aplicacion.geometry("580x320")
        aplicacion.title("Aplicacion")
        framev.validacion()
        for videojuego in Catalogo.getVideojuegos():
          if videojuego.getNombre()==str(framev.getValue("Nombre")):
            Label(aplicacion, text= "Videojugo ya existente" , font=('Times 12')).pack(fill=BOTH, expand=True)
            aplicacion.mainloop()
            return
        Catalogo._videojuegos.append(Videojuego(framev.getValue("Genero videojuego"),framev.getValue("Nombre"),framev.getValue("Precio"),10,Desarrollador(framev.getValue("Desarrollador"),None,0),framev.getValue("Clasificacion"),0)) 
        Label(aplicacion, text= "Videojugo agregado" , font=('Times 12')).pack(fill=BOTH, expand=True)
        aplicacion.mainloop()
    except ErrorAplicacion as e:
      ExceptionPopUp(str(e))
      aplicacion.destroy()
  def videojuego():
    matarlo(bonificarv)
    matar.append(bonificarv)
    framev.crearBotones(y)
    
    
    
  ####################################################################################
  emple=Frame(ventana,bd=10)
  nombreem=Label(emple,text="Contratar empleado",bd=10)
  nombreem.pack()
  descripcionem=Label(emple,text="Contratar empelado manualmente",bd=20)
  descripcionem.pack()
  frameem=FieldFrame(emple,"Criterios",["Nombre","Documento","Tarjeta","Sueldo","Cargo","Ventas"],"Valor",["","","","","Vendedor",0],["Cargo","Ventas"],[0,1,1,1,0,1])
  frameem.pack()
  def z():
    try:
      aplicacion=tk.Toplevel(ventana)
      aplicacion.geometry("580x320")
      aplicacion.title("Aplicacion")
      frameem.validacion()
      for empleado in Empresa.getListaEmpleados():
        if empleado.getDocumento()==int(frameem.getValue("Documento")):
          Label(aplicacion, text= "Empleado ya contratado anteriormente" , font=('Times 12')).pack(fill=BOTH, expand=True)
          aplicacion.mainloop()
          return
      v=Tarjeta(frameem.getValue("Tarjeta"),0)
      Empleado(frameem.getValue("Nombre"),int(frameem.getValue("Documento")),18,v,int(frameem.getValue("Sueldo")),"Vendedor",0)
      Label(aplicacion, text= "Empleado contratado" , font=('Times 12')).pack(fill=BOTH, expand=True)
      aplicacion.mainloop()
    except ErrorAplicacion as e:
      ExceptionPopUp(str(e))
      aplicacion.destroy()
  def empleado():
    matarlo(emple)
    matar.append(emple)
    frameem.crearBotones(z)
######################################################################################
  clien=Frame(ventana,bd=10)
  nombrecl=Label(clien,text="Recargar tarjeta de cliente",bd=10)
  nombrecl.pack()
  descripcioncl=Label(clien,text="Recargar manualmente la tarjeta de un cliente, algo parecido a un cajero",bd=20)
  descripcioncl.pack()
  framecl=FieldFrame(clien,"Criterios",["Cedula","Cantidad"],"Valor",["",""],[],[1,1])
  framecl.pack()

  def w():
    try:
      aplicacion3=tk.Toplevel(ventana)
      aplicacion3.geometry("580x320")
      aplicacion3.title("Aplicacion")
      framecl.validacion()
      texto=int(framecl._entries[0].get())
      texto1=math.sqrt(int(framecl._entries[1].get()))
      texto2=int(framecl._entries[1].get())
       
      for cliente in Empresa.getListaClientes():
        if cliente.getDocumento()==texto:
          cliente.getTarjeta().ingresar(texto2)
          s="Dinero ingresado,saldo actual: "+str(cliente.getTarjeta().getSaldo())
          z=Label(aplicacion3, text= str(s) , font=('Times 12')).pack(fill=BOTH, expand=True)
          aplicacion3.mainloop()
          return
      raise ClienteException("Cliente no encontrado")

    except ErrorAplicacion as e:
            aplicacion3.destroy()
            ExceptionPopUp(str(e))
  



  def cli():
    matarlo(clien)
    matar.append(clien)
    framecl.crearBotones(w)

#####################################################################################
  clv=Frame(ventana,bd=10)
  nombreclv=Label(clv,text="Comprar un videojuego",bd=10)
  nombreclv.pack()
  descripcionclv=Label(clv,text="Comprarle manualmente un juego a un cliente",bd=20)
  descripcionclv.pack()
  frameclv=FieldFrame(clv,"Criterios",["Cedula","Videojuego"],"Valor",["",""],[],[1,0])
  frameclv.pack()
  def t():
    try:
      aplicacion3=tk.Toplevel(ventana)
      aplicacion3.geometry("580x320")
      aplicacion3.title("Aplicacion")
      frameclv.validacion()
      texto=int(frameclv._entries[0].get())
      texto1=str(frameclv._entries[1].get())
      
      
      for cliente in Empresa.getListaClientes():
        if cliente.getDocumento()==texto:
          z=Label(aplicacion3, text= cliente.comprarVideojuego(texto1), font=('Times 12')).pack(fill=BOTH, expand=True)
          aplicacion3.mainloop()
          return
      raise ClienteException("Cliente no encontrado")
    except ErrorAplicacion as e:
            aplicacion3.destroy()
            ExceptionPopUp(str(e))
  def clvv():
    matarlo(clv)
    matar.append(clv)
    frameclv.crearBotones(t)
#################################################################################

  cll=Frame(ventana,bd=10)
  nombrecll=Label(cll,text="Calificar",bd=10)
  nombrecll.pack()
  descripcioncll=Label(cll,text="Calificar manualmente un videojuego",bd=20)
  descripcioncll.pack()
  framecll=FieldFrame(cll,"Criterios",["Cedula","Videojuego","Calificacion"],"Valor",["","",""],[],[1,0,1])
  framecll.pack()
  def to():
    try:
      aplicacion3=tk.Toplevel(ventana)
      aplicacion3.geometry("580x320")
      aplicacion3.title("Aplicacion")
      framecll.validacion()
      texto=int(framecll._entries[0].get())
      texto1=str(framecll._entries[1].get())
      texto2=int(framecll._entries[2].get())
      
      
      for cliente in Empresa.getListaClientes():
        if cliente.getDocumento()==texto:
          z=Label(aplicacion3, text= cliente.calificarVideojuego(texto1,texto2), font=('Times 12')).pack(fill=BOTH, expand=True)
          aplicacion3.mainloop()
          return
      raise ClienteException("Cliente no encontrado")


    

    except ErrorAplicacion as e:
            aplicacion3.destroy()
            ExceptionPopUp(str(e))





  def cllo():
    matarlo(cll)
    matar.append(cll)
    framecll.crearBotones(to)


####################################################################################

  clienb=Frame(ventana,bd=10)
  nombreclb=Label(clienb,text="Bonificar a un cliente",bd=10)
  nombreclb.pack()
  descripcionclb=Label(clienb,text="Cambiarle el RANGO a un cliente",bd=20)
  descripcionclb.pack()
  frameclb=FieldFrame(clienb,"Criterios",["Cedula"],"Valor",[""],[],[1])
  frameclb.pack()

  def r():
    try:
      frameclb.validacion()
      texto=int(frameclb._entries[0].get())
      aplicacion3=tk.Toplevel(ventana)
      print(len(Empresa.getListaEmpleados()))
      aplicacion3.geometry("580x320")
      aplicacion3.title("Aplicacion")
      e=Empleado()
      print(len(Empresa.getListaEmpleados()))
      z=Label(aplicacion3, text=e.descuentoEspecial(texto), font=('Times 12')).pack(fill=BOTH, expand=True)
      aplicacion3.mainloop()
    except ErrorAplicacion as e:
            aplicacion3.destroy()
            ExceptionPopUp(str(e)) 

      


  def bonificacionespecial():
    frameclb.crearBotones(r)
    matarlo(clienb)
    matar.append(clienb)


###############################################################################################




  #MENU
  menuBar=tk.Menu(ventana)
  ventana.config(menu=menuBar)
  menu1=tk.Menu(menuBar,activebackground="blue",activeforeground="white")
  menuBar.add_cascade(label="Archivo",menu=menu1)
  menu1.add_command(label="Aplicación",command=aplicacionPop)####7
  menu1.add_command(label="Salir",command=exit)####8
  menu3=tk.Menu(menuBar,activebackground="blue",activeforeground="white")
  menu3.add_command(label="Mostrar detalles empleados",command=detalles)
  menu3.add_command(label="Mostrar detalles empresa",command=detallesEmpresa)
  menu3.add_command(label="Mostrar catálogo",command=mostrarCatalogo)
  menu3.add_command(label="Mostrar cliente específico",command=clienteespecifico1)
  menu4=tk.Menu(menuBar,activebackground="blue",activeforeground="white")
  menu4.add_command(label="Añadir videojuego",command=videojuego)
  menu4.add_command(label="Contratar empleado",command=empleado)
  menu4.add_command(label="Ingresar dinero tarjeta",command=cli)
  menu4.add_command(label="Volver",command="")
  menu2=tk.Menu(menuBar,activebackground="blue",activeforeground="white")
  menuBar.add_cascade(label="Procesos y consultas", menu=menu2)
  menu2.add_command(label="Comprar videojuego",command=clvv)
  menu2.add_command(label="Calificar videojuego",command=cllo)
  menu2.add_command(label="Pagar empleados",command=pagar)
  menu2.add_command(label="Bonificación especial al cliente",command=bonificacionespecial)
  menu2.add_command(label="Realizar bonificación mensual",command=bonificacion)
  menu2.add_cascade(label="Opciones alternativas", menu=menu3)
  menu2.add_cascade(label="Extras",menu=menu4)
  menu5=tk.Menu(menuBar,activebackground="blue",activeforeground="white")
  menuBar.add_cascade(label="Ayuda", menu=menu5)
  menu5.add_command(label="Acerca de",command=ayudaPop)



  ventana.mainloop()