from tkinter import*



class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800")


        msg = Message( root, text = "เข้าสู่ระบบ",font=28,width="100")
        msg.place(relx = 0.5, rely = 0.2, anchor = CENTER)

        inputUser = Entry(root,width=50)
        inputUser.place(relx = 0.5, rely = 0.25, anchor = CENTER)


        inputPassword = Entry(root,width=50, show="*")
        inputPassword.place(relx = 0.5, rely = 0.3, anchor = CENTER)


        btnSubmit = Button(root,text="LOGIN",width=40)
        btnSubmit.place(relx = 0.5, rely = 0.35, anchor = CENTER)

         
if __name__=="__main__":
        root=Tk()
        obj=HotelManagementSystem(root)
        root.mainloop()
        #####################################################
#################################################
#################################################
#################################################

print("1212121212122e2e2e2e2e2e2e2e2e2e21212")
        
        
