from tkinter import *
from tkinter import messagebox
import pymysql
import sqlite3


def leer():

    conn=sqlite3.connect("notas")
    

    cur=conn.cursor()
    cur.execute("SELECT * FROM  calificaciones1 WHERE ID=" + ID1.get())

    elUsuario=cur.fetchall()

    for usuario in elUsuario:

        ID1.set(usuario[0])
        AF1.set(usuario[1])
        so1.set(usuario[2])
        PA1.set(usuario[3])
        Comu1.set(usuario[4])
    conn.commit()
  

def Limpiar ():
	ID1.set(" ")
	AF1.set(" ")
	so1.set(" ")
	PA1.set(" ")
	Comu1.set(" ")
def salir():
	valor=messagebox.askquestion("salir","deseas salir de la aplicacion")
	if valor=="yes":
		tk.destroy()
tk=Tk()
tk.title("Ingreso de datos")
ventana=Frame (height=400,width=700)
ventana.pack(padx=5,pady=5)
ventana.configure(background="peach puff")
tema=Label(ventana,font=('Times New Roman',12,'bold'),text="Leer notas de alumnos ",padx=80,pady=3,bd=5,background="gray77").place(x=170,y=0)
#notas1
num_ced=Label(ventana,font=('Times New Roman',12,'bold'),text="Ingrese la ID del alumno que desea averiguar",background="#91F467").place(x=195,y=37)
ID1=StringVar()
txt=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=ID1,width=10,bg="cyan",bd=5).place(x=260,y=70)
#nota2
AF=Label(ventana,font=('Times New Roman',12,'bold'),text="Algoritmos funtamentales",background="#91F467").place(x=0,y=100)
AF1=StringVar()
txt1=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=AF1,width=10,bg="cyan",bd=5).place(x=0,y=150)
#notas3
so=Label(ventana,font=('Times New Roman',12,'bold'),text="Sistemas Operativos ",background="#91F467").place(x=210,y=123)
so1=StringVar()
txt2=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=so1,width=10,bg="cyan",bd=5).place(x=210,y=155)
#notas4
PA=Label(ventana,font=('Times New Roman',12,'bold'),text="Programacion avanzada ",background="#91F467").place(x=0,y=209)
PA1=StringVar()
txt3=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=PA1,width=10,bg="cyan",bd=5).place(x=0,y=250)
#notas5
Comu=Label(ventana,font=('Times New Roman',12,'bold'),text="Comunicaciones",background="#91F467").place(x=210,y=209)
Comu1=StringVar()
txt4=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=Comu1,width=10,bg="cyan",bd=5).place(x=210,y=250)

#botones
#
#conectar=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=conectar,text="conectar",padx=20,pady=5,background="#91F467").place(x=20,y=340)
Leer=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=leer,text="Leer",padx=20,pady=5,background="#91F467").place(x=0,y=300)
limpiar=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=Limpiar,text="Limpiar",padx=50,pady=5,background="#FF60F3").place(x=120,y=300)
salir=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=salir,text="salir",padx=50,pady=5,background="#FF60F3").place(x=350,y=300)

canvas = Canvas(tk,width=300, height=300)
canvas.pack()

esfera = PhotoImage(file='buo.png')
canvas.create_image(0, 0, anchor=NW, image=esfera)

tk.mainloop()