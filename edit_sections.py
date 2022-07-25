from tkinter import *
from tkinter import ttk
from listbox import *
from tkinter import messagebox

class UpdateName(Frame):
    def __init__(self,classes,*args,**kwargs):
        super().__init__(relief=FLAT,bg='#B0C4DE',pady=13,padx=15,*args,**kwargs)
        self.select_option=SELECT_CHOICE(classes,self)
        self.select_option.grid(row=0,column=0)
        self.rowconfigure(0,weight=1)
        
        fname=Label(self,text='New Name :',font=('times new roman',20,'bold'),
        fg='black',bg='#B0C4DE')
        fname.grid(row=0,column=1)
        self.sentry=Entry(self,font=('times new roman',18,'bold'),relief=RIDGE,bd=2,bg='#F5F5DC')
        self.sentry.grid(row=0,column=2,sticky=NS)
        
        
        self.columnconfigure(3,weight=1)
        self.search_button=Button(self,text='Update',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.check_entry())
        self.search_button.grid(row=0,column=3,sticky="nse")
    def check_entry(self):
        class_,section=self.select_option.chioces
        if not class_:
            messagebox.showerror("ERROR","Select a Class")
            return False
        if not section:
            messagebox.showerror("ERROR","Select a Section")
            return False
        if not len(self.sentry.get().replace(" ","")):
            messagebox.showerror("ERROR","Name are required")
            return False
        return list(self.select_option.chioces)+[self.sentry.get()]
    def update_classes(self,classes):
        self.select_option.update_classes(classes)
    def clear(self):
        self.sentry.delete(0,END)
        self.select_option.section_combovar.set(SELECT_SECTION)
class NewName(Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(relief=FLAT,bg='#B0C4DE',pady=13,padx=15,*args,**kwargs)
        self.rowconfigure(0,weight=1)
        self.class_combo=ttk.Combobox(self,values=CLASSES,font=('times new roman',18,'bold'))
        self.class_combo.grid(row=0,column=0,sticky="nsw")
        self.class_combo.set(SELECT_CLASS)
        self.class_combo.config(state='readonly')
        #self.section_combovar.trace_add("write",lambda *Args:self._track_updating())
        fname=Label(self,text='Section Name :',font=('times new roman',20,'bold'),
        fg='black',bg='#B0C4DE')
        fname.grid(row=0,column=1,sticky=NS)
        
        self.sentry=Entry(self,font=('times new roman',18,'bold'),relief=RIDGE,bd=2,bg='#F5F5DC')
        self.sentry.grid(row=0,column=2,sticky=NS)
        
        self.columnconfigure(3,weight=1)
        self.search_button=Button(self,text='ADD',font=('times new roman',15,'bold'),
                                  
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.check_entry())
        self.search_button.grid(row=0,column=3,sticky="nse")
    def check_entry(self):

        if self.class_combo.get()==SELECT_CLASS:
            messagebox.showerror("ERROR","Select a Class")
            return False
        if not len(self.sentry.get().replace(" ","")):
            messagebox.showerror("ERROR","Name are required")
            return False
        return self.class_combo.get(),self.sentry.get()
    def clear(self):
        self.sentry.delete(0,END)
        self.class_combo.set(SELECT_CLASS)
class EDIT_SECTIONLEVEL(Toplevel):
    def __init__(self,classes,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("EDIT SECTIONS")
        self.resizable(FALSE,FALSE)
        
        self.newname=NewName(self)
        self.newname.pack(fill=X)
        
        self.update_name=UpdateName(classes,self)
        self.update_name.pack(fill=X)

if __name__=="__main__":
    from _constents import CLASSES
    root=Tk()
    NewName().pack(fill=BOTH,expand=YES)
    root.mainloop()
        
 
