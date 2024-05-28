import tkinter
import customtkinter
from PIL import ImageTk,Image
from main import LOL

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("green") 


app = customtkinter.CTk()
#creating cutstom tkinter window
app.geometry("1300x750")
app.title('AI App')

ai_answer = ""

def button_function():
    l2.delete("0.0", "end")
    hehe = entry2.get()

    
    entry2.delete(0, len(hehe))
    
    ai_answer = LOL.answerMe(hehe)

    l2.insert("0.0", text=ai_answer)
    


img1=ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()


frame=customtkinter.CTkFrame(master=l1, width=800, height=500, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkTextbox(master=frame,font=('Century Gothic',20), width=700, height= 250, wrap="word")
l2.insert("0.0",text=ai_answer)


l2.place(x=50, y=45)


entry2=customtkinter.CTkEntry(master=frame, width=400, height=50, placeholder_text='Input Question')
entry2.place(x=200, y=330)




button1 = customtkinter.CTkButton(master=frame, width=400, height=50, text="Submit", command=button_function, corner_radius=6)
button1.place(x=200, y=400)





app.mainloop()
