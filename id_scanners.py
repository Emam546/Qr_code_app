
from tkinter  import *
from tkinter import messagebox
def _vaildiation_digits_number(input):
    if input.isnumeric() or input == "":return True                  
    else:return False
class IdScaaner(Toplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("ID BARCODE SCANNER")
        reg=self.winfo_toplevel().register(_vaildiation_digits_number)
        self.resizable(False,False)
        bgfframe=Frame(self,relief=FLAT,bg='white',pady=15)
        bgfframe.pack(fill=BOTH,expand=YES)
        bgfframe.rowconfigure(0,weight=1)
        bgfframe.columnconfigure(2,weight=1)
        
        fname=Label(bgfframe,text='ID :',font=('times new roman',20,'bold'),
        fg='black')
        fname.grid(row=0,column=0,padx=20,sticky=NS)
        self.idvar=StringVar()
        self.sentry=Entry(bgfframe,font=('times new roman',18,'bold'),relief=RIDGE,bd=2,bg='#F5F5DC'
                          ,textvariable=self.idvar,validatecommand =(reg, '%S'),validate ="key")
        self.sentry.grid(row=0,column=1,sticky=NS)

        self.search_button=Button(bgfframe,text='Scan',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.check())
        self.search_button.grid(row=0,column=2,padx=30)
        
        self.search_button=Button(bgfframe,text='Clear',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.clear())
        self.search_button.grid(row=0,column=3)
        
        self.idvar.trace_add("write",lambda *args:self.track())
    
    
    def track(self):
        if len(self.idvar.get())>=12:
            self.check()
        self.lift()
    def scan(self):
        if (self.check()==True):
            pass
    def check(self):
        if not len(self.idvar.get())>=12:
            #messagebox.showerror("ERROR","ID must be 12 digits")
            return False
        return self.sentry.get()
    def clear(self):
        self.idvar.set("")
        
        
def main():
    root=Tk()
    IdScaaner(root)   
    root.mainloop()
if __name__=="__main__":
    main()