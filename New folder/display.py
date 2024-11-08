import tkinter
import customtkinter
from PIL import Image
import mysql.connector
import pandas as pd
def close():
    desroot.destroy()
rd=pd.read_excel('statistics//all data.xlsx')
noci=rd[0][1]
noct=rd[0][2]
poci=rd[1][1]
poct=rd[1][1]
neoci=rd[2][1]
neoct=rd[2][1]
nuoci=rd[3][1]
nuoct=rd[3][1]
x=mysql.connector.connect(user="root",host="localhost",passwd="udit2005",database="SBH")
y=x.cursor()
y.execute("select * from usernames")
a=y.fetchall()
#ins_usr=a[0][0]
#tw_usr=a[0][1]
ins_usr="iamsrk"
tw_usr="iamsrk"
y.execute("DELETE FROM usernames")
x.commit()
x.close()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
desroot=customtkinter.CTk()
desroot.geometry("2600x1100")
desroot.title("Statistics")
desroot.iconbitmap("video/icon.ico")
frame=customtkinter.CTkFrame(master=desroot)
frame.pack(padx=20,pady=60,fill="both",expand=True)
dm=customtkinter.CTkLabel(master=frame,text=f"Total Comment in instagram={noci}\nPositive={poci}\nNegative={neoci}\nNeutral={nuoci}\nTotal Comment in twitter={noct}\nPositive={poct}\nNegative={neoct}\nNeutral={nuoct}")
dm.pack(pady=10,padx=10)
my_image=customtkinter.CTkImage(light_image=Image.open(f'statistics/{ins_usr} pie chart.png'),dark_image=Image.open(f'statistics/{ins_usr} pie chart.png'),size=(700,500))
my_label=customtkinter.CTkLabel(desroot, text="",image=my_image)
my_label.pack(pady=18,side='left')
my_image=customtkinter.CTkImage(light_image=Image.open(f'statistics/{ins_usr} bar graph.png'),dark_image=Image.open(f'statistics/{ins_usr} bar graph.png'),size=(700,500))
my_label=customtkinter.CTkLabel(desroot, text="",image=my_image)
my_label.pack(pady=18,side='right')
button=customtkinter.CTkButton(master=frame,text="close",command=close)
button.pack(pady=12,padx=10)
desroot.mainloop()
