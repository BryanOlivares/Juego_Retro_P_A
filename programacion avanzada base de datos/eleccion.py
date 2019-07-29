from tkinter import *
import pymysql
import os
from tkinter import messagebox
import sqlite3
tk=Tk()
tk.title("Menu Principal")
#funciones de ejercicios
def estudiante():
    os.system("leer.py")
def profesor():

    os.system("notas_saew.py")
conn=sqlite3.connect("notas")
cur=conn.cursor()
try:

    cur.execute ('''CREATE TABLE calificaciones1 (ID integer Primary key AUTOINCREMENT , Algoritmos FLOAT(10) NOT NULL , SistemasOp FLOAT(10) NOT NULL , Programacion FLOAT(10) NOT NULL , Comunicaciones FLOAT(10) NOT NULL )''')
    messagebox.showinfo("BD","BD creada con exito!!!")
except:
	messagebox.showwarning("Atencion","la base de datos ya existe")

def Limpiar ():
	nombre.set(" ")
	apellido.set(" ")
	contraseña1.set(" ")

ventana=Frame(height=400,width=700)
ventana.pack(padx=5,pady=5)
ventana.configure(background="sky blue")
tk.title("Eleccion de Usuario")
tema=Label(ventana,font=('Times New Roman',12,'bold'),text="Bienvenido",padx=80,pady=3,bd=5,background="SpringGreen2").place(x=170,y=0)
#ingresando nombre
nom=Label(ventana,font=('Times New Roman',12,'bold'),text="Ingrese su nombre",background="#91F467").place(x=200,y=40)
nombre=StringVar()
nombre1=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=nombre,width=10,bg="powder blue",bd=5).place(x=200,y=80)
#ingresando apellido
apell=Label(ventana,font=('Times New Roman',12,'bold'),text="Ingrese su apellido",background="#91F467").place(x=200,y=120)
apellido=StringVar()
apellido1=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=apellido,width=10,bg="powder blue",bd=5).place(x=200,y=160)
#ngrese contraseña

cont=Label(ventana,font=('Times New Roman',12,'bold'),text="Ingrese su contraseña",background="#91F467").place(x=200,y=200)
contraseña1=StringVar()
contraseña=Entry(ventana,font=('Times New Roman',15,'bold'),textvariable=contraseña1,width=10,bg="powder blue",bd=5,show="*").place(x=200,y=240)

#botones
estudiante=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=estudiante,text="Estudiante",padx=20,pady=5,background="#91F467").place(x=0,y=280)
profesor=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=profesor,text="profesor",padx=20,pady=5,background="#91F467").place(x=200,y=280)
limpiar=Button(ventana,font=('Times New Roman',12,'bold'),bd=15,command=Limpiar,text="Limpiar",padx=50,pady=5,background="#FF60F3").place(x=350,y=280)

canvas = Canvas(tk,width=300, height=300)
canvas.pack()

esfera = PhotoImage(file='buo.png')
canvas.create_image(0, 0, anchor=NW, image=esfera)

tk.mainloop()






