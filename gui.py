import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import ImageTk
import pygame.mixer as mixer


mixer.init()

#Iniciando GUI Tkinter
root = tk.Tk()
style = ttk.Style('morph')
root.geometry('400x600')
root.title('MaggieP3')
root.resizable(False, False)

#Declarando Path da imagens
path1 = ImageTk.PhotoImage(file=r"C:\Users\samue\MusicPlayer\GUI\backward.png")
path2 = ImageTk.PhotoImage(file=r"C:\Users\samue\MusicPlayer\GUI\forward.png")
path3 = ImageTk.PhotoImage(file=r"C:\Users\samue\MusicPlayer\GUI\pause.png")
path4 = ImageTk.PhotoImage(file=r"C:\Users\samue\MusicPlayer\GUI\play.png")
musicas_pasta = []

def carregar_musica():
   
   selecionar = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Mp3 Files",
                                                        "*.mp3*"),
                                                       ("all files",
                                                        "*.*")))
   
   musicas_pasta.append(selecionar)
   return musicas_pasta

def iniciar_musica():
   for item in musicas_pasta:
       mixer.music.load(item)
       mixer.music.play()
   
  
def pausar_musica():
   if mixer.music.get_busy():
       mixer.music.pause()
   else:
       mixer.music.unpause()





#Criando botões
backwardbutton = ttk.Button(root, image=path1, bootstyle='light-link')
backwardbutton.place(x=60, y=500)

forwardbutton = ttk.Button(root, image=path2, bootstyle='light-link')
forwardbutton.place(x=300, y=500)

pausebutton = ttk.Button(root, image=path3, bootstyle='light-link', command=pausar_musica)
pausebutton.place(x=140, y=500)

playbutton = ttk.Button(root, image=path4, bootstyle='light-link', command=iniciar_musica)
playbutton.place(x=215, y=500)



# Capa do album
capa_album = ImageTk.PhotoImage(file=r"C:\Users\samue\MusicPlayer\GUI\albumcover.jpg")


capa_label = ttk.Label(root, image=capa_album)
capa_label.pack(side=TOP, expand=False)
capa_label.place(x=47 , y=50)

musicas = ttk.Button(root, text='Musicas na pasta: ', bootstyle='primary', command=carregar_musica)
musicas.pack(side=BOTTOM, expand=False)


root.mainloop()