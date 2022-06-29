from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os




root = Tk()

root.geometry("920x670+290+85")
root.title('Music Player')
root.resizable(0,0)
root.configure(bg= "#0f1a2b")
mixer.init()


global song

def add_music():

	path = filedialog.askdirectory(initialdir ='Music/')

	if path:

		os.chdir(path)

		songs = os.listdir(path)

		for song in songs:
			
			if song.endswith(".mp3"):

				Playlist.insert(END , song)


def Play_Music():

	Music_name = Playlist.get(ACTIVE)

	print(Music_name[0:-4])
	mixer.music.load(Playlist.get(ACTIVE))
	mixer.music.play()


def play_next():

	#select song index
	next_one = Playlist.curselection()
	#to get next song
	next_one = next_one[0]  + 1
	#get next song
	temp = Playlist.get(next_one)
	
	mixer.music.load(temp)
	mixer.music.play()
	Playlist.selection_clear(0 ,END)
	#activating new song 
	Playlist.activate(next_one)
	#playing the newxt song
	Playlist.selection_set(next_one)


def prev():

	per_one = Playlist.curselection()
	per_one = per_one[0] - 1

	temp = Playlist.get(per_one)

	mixer.music.load(temp)
	mixer.music.play()
	Playlist.selection_clear(0,END)
	Playlist.activate(per_one)
	Playlist.selection_set(per_one)

def exi():

	os.exit()





#Buttons
play_icon = PhotoImage(file = r"img/play.png").subsample(9,9)

play_btn = Button(root , image = play_icon, compound = LEFT ,fg = "white" , bg = '#0f1a2b' ,command = Play_Music).place(x=115, y=400)

pause_icon = PhotoImage(file = r"img/pause.png").subsample(9,9)

pause_btn = Button(root ,image = pause_icon, compound = LEFT ,fg= 'white', bg = '#0f1a2b' ,command = mixer.music.pause).place(x=200, y=500)

stop_icon = PhotoImage(file = r"img/stop.png").subsample(9,9)

stop_btn = Button(root , image = stop_icon, compound = LEFT ,fg= 'white', bg = '#0f1a2b' ,command = mixer.music.stop).place(x=30, y=500)

resume_icon = PhotoImage(file = r"img/resume.png").subsample(9,9)

resume_btn = Button(root , image = resume_icon, compound = LEFT ,fg= 'white', bg = '#0f1a2b' ,command = mixer.music.unpause).place(x=115, y=500)

next_icon = PhotoImage(file = r"img/next.png").subsample(3,3)

next_Btn = Button(root, image = next_icon, command= play_next,bg='#0f1a2b', fg='white').place(x=115 , y = 550)

prev_icon = PhotoImage(file = r"img/prev.png").subsample(3,4)
prev_Btn = Button(root, image = prev_icon, command= prev,bg='#0f1a2b', fg='white').place(x=155 , y = 550)

exit_icon = PhotoImage(file = r"img/exit.png").subsample(3,4)
exit_Btn = Button(root, image = exit_icon, command= exit,bg='#0f1a2b', fg='white').place(x=115 , y = 590)

Menu = Label(root,bg="White").pack(padx=10, pady=50, side=RIGHT)


Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=330, y=350, width=560, height=250)
 
Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= add_music).place(x=725, y=350)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="red", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()