from tkinter import *
import os

def restart():
    os.system("shutdown -r -t 1")

def restart_time():
    os.system("shutdown -r -t 20")

def shutdown():
    os.system("shutdown -s -t 1")

st = Tk()
st.title("Shut Down App")
st.geometry("500x500")
st.config(bg="blue")
#restart button
r_button = Button(st,text="Restart",font=("arial",20,"bold"),bg="red",cursor="Plus",command=restart)
r_button.place(x=150,y=60,width=200,height=50)
#restart with time
r_button = Button(st,text="Restart Time",font=("arial",20,"bold"),bg="red",cursor="Plus",command=restart_time)
r_button.place(x=150,y=170,width=200,height=50)
#shutdown
r_button = Button(st,text="Shutdown",font=("arial",20,"bold"),bg="red",cursor="Plus",command=shutdown)
r_button.place(x=150,y=270,width=200,height=50)
#closed button
r_button = Button(st,text="Close",font=("arial",20,"bold"),bg="red",cursor="Plus",command=st.destroy)
r_button.place(x=150,y=370,width=200,height=50)


st.mainloop()