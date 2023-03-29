from tkinter import *
import sqlite3

windowuser = Tk()
windowuser.title('User')

def salvar():
    nome = nomeinput.get()
    telefone = f'+55{telefoneinput.get()}'
    
    connectionall = sqlite3.connect('lista.db')
    c= connectionall.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS clientes(nome text,telefone text)')
    connectionall.commit()
    c.execute('INSERT INTO clientes(nome, telefone) VALUES(?,?)',(nome,telefone))
    connectionall.commit()
    nomeinput.delete(0,END)
    telefoneinput.delete(0,END)


nome = Label(windowuser, text='Nome',
                font=('impact bold', "15 "),
                background='grey',
                foreground='yellow',
                )
nome.place(x=70, y=50)

nomeinput = Entry(windowuser,
                    width=25,
                    bg='powder blue',
                    bd=10,
                    font=('impact bold', '12')
                    )
nomeinput.place(x=230, y=50)


numero = Label(windowuser, text='DDD e Numero',
                font=('impact bold', "15 "),
                background='grey',
                foreground='yellow',
                )
numero.place(x=35, y=100)


telefoneinput = Entry(windowuser,
                        width=25,
                        bg='powder blue',
                        bd=10,
                        font=('impact bold', '12')
                        )
telefoneinput.place(x=230, y=100)
btenter = Button(windowuser, text='salvar',
                    bg='powder blue',
                    bd=10,
                    font=('impact bold', '15'),
                    command=salvar
                    )

btenter.place(x=100, y=150)




windowuser.configure(background='grey')
windowuser.geometry('500x250')
windowuser.mainloop()
