import socket
from tkinter import *
from pygame import mixer

c = socket.socket()

try:
    c.connect(('localhost',8090))
    print("Client says 'Socket Connected'") #Socket Connected
except socket.error as e:
    print(str(e))

name = input("Enter your name : ")
c.send(bytes(name,'utf-8'))

mixer.init()

tk = Tk()
tk.title("Client: "+name+"'s Music Player")
tk.geometry("500x500")
tk.config(bg = 'pink')

sn = c.recv(1024).decode()

label = Label(tk,text="Category : "+sn,fg='red',font =(16))
label.pack(padx=1,pady =5)

lab = Label(tk,text=name+" is listening the music...",font = "Helvetica 12")
lab.pack(padx=1,pady=1)

prev_img = PhotoImage(file='prev_img.png')
pause_img = PhotoImage(file='pause_img.png')
stop_img = PhotoImage(file='stop_img.png')
next_img = PhotoImage(file='next_img.png')
play_img = PhotoImage(file='play_img.png')

listBox = Listbox(tk, fg = 'white', bg = 'black',width = 60 )
listBox.pack(padx=10,pady=10) 

if sn=="Motivational":
    listBox.insert(0,"Believer")
    listBox.insert(1,"Fitness")
    listBox.insert(2,"Stronger")
    listBox.insert(3,"Who Says")
    listBox.insert(4,"Love Yourself")
elif sn=="Devotional":
    listBox.insert(0,"Ayarpadi")
    listBox.insert(1,"KrishnaFlute")
    listBox.insert(2,"Kurai Ondrum Illai")
    listBox.insert(3,"Mukuntha Mukuntha")
    listBox.insert(4,"Paarthene")
elif sn=="Happy Mood":
    listBox.insert(0,"Fantasy")
    listBox.insert(1,"Friendship")
elif sn=="Relaxing":
    listBox.insert(0,"Memories")
    listBox.insert(1,"Radha Krishna")
elif sn=="Party":
    listBox.insert(0,"Happy Birthday")
    listBox.insert(1,"Dynamite")   
    listBox.insert(2,"Lets Party") 
    listBox.insert(3,"Party Freak") 
    listBox.insert(4,"Yello Pullelo")          

rootpath = "C:\\test\my_music"
pattern = ".mp3"

top = Frame(tk, bg='pink')
top.pack(padx=15, pady=13,anchor='center')

def select():
	mixer.music.load(rootpath+"\\"+sn+ "\\" + listBox.get("anchor")+pattern)
	mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def pause_song():
    if pause['text']== 'pause':
        mixer.music.pause()
        pause['text'] = 'play'
    else:
        mixer.music.unpause()
        pause['text'] = 'pause'

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] +1
    next_song_name = listBox.get(next_song)
    label.config(text= next_song_name)

    mixer.music.load(rootpath+"\\"+sn+ "\\" + next_song_name+pattern)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)
    

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text= next_song_name)

    mixer.music.load(rootpath+"\\"+sn+ "\\" +next_song_name+pattern)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

prev = Button(tk,text='Prev', image= prev_img, bg='pink', borderwidth=0,command=play_prev)
prev.pack(pady = 15, in_ = top, side='left')

stopb = Button(tk,text='Stop', image= stop_img,bg='pink', borderwidth=0, command=stop)
stopb.pack(pady = 15, in_ = top, side='left')

play = Button(tk,text='play', image= play_img,bg='pink', borderwidth=0, command= select)
play.pack(pady = 15, in_ = top, side='left')

next = Button(tk,text='next', image= next_img,bg='pink', borderwidth=0, command=play_next)
next.pack(pady = 15, in_ = top, side='left')

pause = Button(tk,text='pause', image= pause_img,bg='pink', borderwidth=0, command= pause_song)
pause.pack(pady = 15, in_ = top, side='left')

qb = Button(tk,text='Quit',font='Android 12',bd=5,bg="#00ffff",command=tk.destroy)
qb.pack(padx=10,pady=20)

tk.mainloop()


c.close()