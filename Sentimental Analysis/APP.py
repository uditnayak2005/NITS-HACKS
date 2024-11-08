import tkinter
import customtkinter
import mysql.connector
x=mysql.connector.connect(user="root",host="localhost",passwd="udit2005",database="SBH")
y=x.cursor()
def loading():
    
    
    sroot=customtkinter.CTk()
    sroot.geometry("500x350")
    sroot.title("Sentimental Analysis")
    frame=customtkinter.CTkFrame(master=sroot)
    frame.pack(padx=20,pady=60,fill="both",expand=True)
    lable=customtkinter.CTkLabel(master=frame,text=".............DONE.............")
    lable.pack(pady=12,padx=10)
    button=customtkinter.CTkButton(master=frame,text="This May take upto 3-5 min")
    button.pack(pady=12,padx=10)
    customtkinter.COMMAND(20,login())
    

    
    sroot.mainloop()
def login():
    ins_usr=entry1.get()
    tw_usr=entry2.get()
    y.execute(f'insert into usernames values("{ins_usr}","{tw_usr}")')
    x.commit()
    stscrape.configure(text="Analysing The Interactions........")
    import main_Prototype
    root.destroy()
    import display
    

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.iconbitmap("video/icon.ico")
root.geometry("500x500")
root.title("Sentimental Analysis")
frame=customtkinter.CTkFrame(master=root)
frame.pack(padx=20,pady=60,fill="both",expand=True)
lable=customtkinter.CTkLabel(master=frame,text="Enter The usernames")
lable.pack(pady=12,padx=10)
entry1=customtkinter.CTkEntry(master=frame,placeholder_text="Instagram Username")
entry1.pack(pady=12,padx=10)
entry2=customtkinter.CTkEntry(master=frame,placeholder_text="Instagarm Username2")
entry2.pack(pady=12,padx=10)
stscrape=customtkinter.CTkLabel(master=frame,text=" ")
stscrape.pack(pady=12,padx=10)
button=customtkinter.CTkButton(master=frame,text="Analyse",command=login)
button.pack(pady=12,padx=10)
root.mainloop()
