from tkinter import *
import os
def restart():
	os.system("shutdown /r /t 1")
def restart_time():
	os.system("shutdow /r /t 10")
def logout():
	os.system("shutdown -l")
def shutdown():
	os.system("shutdown /s /t 1")
	



sd=Tk()
sd.title("shutdown app")
sd.geometry("500x500")
sd.config(bg="brown")
r_button=Button(sd,text="Restart",font=("Time new roman",20,"bold"),
	relief=RAISED,cursor="plus",command=restart)
r_button.place(x=20,y=20,height=80,width=160)

rt_button=Button(sd,text="Restart time",font=("Time new roman",20,"bold"),
	relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=20,y=120,height=80,width=160)

lo_button=Button(sd,text="Log out",font=("Time new roman",20,"bold"),
	relief=RAISED,cursor="plus",command=logout)
lo_button.place(x=20,y=220,height=80,width=160)

sd_button=Button(sd,text="Shut down",font=("Time new roman",20,"bold"),
	relief=RAISED,cursor="plus",command=shutdown)
sd_button.place(x=20,y=320,height=80,width=160)

sd.mainloop()