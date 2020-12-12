from tkinter import *

# Creamos la ventana principal
app = Tk()

# Ventana principal titulo y dimensiones
app.title("Ahorros por año")
app.geometry('300x400')
app.configure(background = "light green")

# Definimos las funciones
def calcular():
    resultado = int(entry1.get()) * int(entry2.get())
    calcular = resultado * int(entry3.get())
    ingreso.set(calcular)

def limpiar_todo():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)

# Definimos variables
ingreso = StringVar()

headLabel = Label(app, text = "Calcula cuanto pudes ahorrar", bg = "light green")
label1 = Label(app, text = "Salario por hora:", bg = "light green")
label2 = Label(app, text = "Horas por semana:", bg = "light green")
label3 = Label(app, text= "Semanas por año:", bg="light green")
label4 = Label(app, text="Gastos por semana:", bg="light green")

# Posiciones de los lebels
headLabel.grid(row = 0, column = 1, pady=15)
label1.grid(row = 2, column = 0, pady=5)
label2.grid(row=3, column=0, pady=5)
label3.grid(row=4, column=0, pady=5)

# Creamos los Entry
entry1 = Entry(app, bd=2)
entry2 = Entry(app, bd=2)
entry3 = Entry(app, bd=2)

# Posicionamos los Entrys
entry1.grid(row = 2, column = 1, pady=5)
entry2.grid(row=3, column=1, pady=5)
entry3.grid(row=4, column=1, pady=5)

answer_label = Label(app, text = "Salario por año", bg = "light green", textvariable=ingreso)
answer_label.grid(row = 7, column = 0, pady=5)

button1 = Button(app, text = "Calcular", bg = "Blue", fg = "snow", command=calcular)
button1.grid(row = 6, column = 1, pady=5)
button2 = Button(app, text = "Limpiar", bg = "Blue", fg = "snow", command=limpiar_todo)
button2.grid(row=8, column=1, pady=5)


app.mainloop()
