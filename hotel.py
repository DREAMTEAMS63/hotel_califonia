from tkinter import *
from pages.pageInfo import appPage1
class MainPage:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        # DATA TEST
        testuser = "test"
        testpass = "test01"
        # DATA TEST
        # CHACK LOGIN TEST
        def clicksend():
                us = username.get()
                pw = password.get()
                if(us == testuser):
                      if( pw == testpass):
                            self.root.destroy()
                            appPage1()
                            print("OK! รหัสถูกต้อง")
                            
                      else:
                            print('NOT OK! รหัสไม่ถูกต้อง')
                else:
                      print("กรุณาใส่ USERNAME ให้ถูกต้อง")
        # CHACK LOGIN TEST
        username= StringVar()
        password = StringVar()

        msg = Message( root, text = "เข้าสู่ระบบ",font=28,width="100")
        msg.place(relx = 0.5, rely = 0.2, anchor = CENTER)

        inputUser = Entry(root,width=50, textvariable=username)
        inputUser.place(relx = 0.5, rely = 0.25, anchor = CENTER)


        inputPassword = Entry(root,width=50, show="*",textvariable=password)
        inputPassword.place(relx = 0.5, rely = 0.3, anchor = CENTER)

        btnSubmit = Button(root,text="LOGIN",width=40,command=clicksend)
        btnSubmit.place(relx = 0.5, rely = 0.35, anchor = CENTER)

         
if __name__=="__main__":
        root=Tk()
        object = MainPage(root)
        root.wm_geometry("500x500")
        root.mainloop()

        
        
