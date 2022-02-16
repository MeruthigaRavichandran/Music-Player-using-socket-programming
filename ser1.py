import socket
from tkinter import *
from pygame import mixer
import threading

def handle_client(conn,addr):
        
    canvas = Tk()
    canvas.title("Available audio files")
    canvas.geometry('600x600')  
    canvas.config(bg = 'cyan')

    top = Frame(canvas, bg='light cyan')
    top.pack(padx=10, pady=5,anchor='center')

    mixer.init()

    def motivation():
        conn.send(bytes("Motivational",'utf-8'))
    def devotion():
        conn.send(bytes("Devotional",'utf-8'))    
    def Happy():
        conn.send(bytes("Happy Mood",'utf-8'))
    def relax():
        conn.send(bytes("Relaxing",'utf-8'))
    def party():
        conn.send(bytes("Party",'utf-8'))    

    DevB = Button(canvas,text= "Devotional",bd=5,command=devotion)
    DevB.place(relwidth=0.4,relheight=0.1,relx=0.3,rely=0.1)

    HapB = Button(canvas,text= "Happy Mood",bd=5,command=Happy)
    HapB.place(relwidth=0.4,relheight=0.1,relx=0.3,rely=0.25)

    MotB = Button(canvas,text= "Motivational",bd=5,command=motivation)
    MotB.place(relwidth=0.4,relheight=0.1,relx=0.3,rely=0.4)

    RelB = Button(canvas,text= "Relaxing",bd=5,command=relax)
    RelB.place(relwidth=0.4,relheight=0.1,relx=0.3,rely=0.55)

    ParB = Button(canvas,text= "Party",bd=5,command=party)
    ParB.place(relwidth=0.4,relheight=0.1,relx=0.3,rely=0.7)

    l = Label(canvas,text="Select the Category",bg='cyan',font=("Comic Sans MS Bold",16))
    l.place(relx=0.25,rely=0.85,relheight=0.1,relwidth=0.5)
    canvas.mainloop()
    conn.close()


print("Server is starting.......")
s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Connected!")
s.bind(('localhost',8090))
s.listen()
print('Waiting for the client connection') 

while True:
    conn,addr = s.accept()
    name = conn.recv(1024).decode()
    print("Got connection from Client: ",name," - ",addr[0]," : ",str(addr[1]))
    thread=threading.Thread(target=handle_client,args=(conn,addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS : {threading.active_count()-1}")