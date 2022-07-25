from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from typing import List,Dict
from _constants import *
PAD_XCOLUMN1=9
PADY_BOTTOM=10

class ManageStudents(Frame):
    def __init__(self,classes:Dict[str,list],*args,**kwargs):
        self.classes=classes
        super().__init__(*args,**kwargs,bg='#B0C4DE',relief='flat')
   
        label=Label(self,text='Manage Student',font=('times new  roman',22,'bold'),
        bg='black',fg='white')
        label.pack(fill=X,expand=YES)
        self.wholeContainer=Frame(self,bg='#B0C4DE',padx=PAD_XCOLUMN1)
        self.wholeContainer.pack(fill=BOTH,expand=YES)
        
        self.wholeContainer.rowconfigure(0,weight=1)
        self.wholeContainer.columnconfigure(0,weight=1)
        
        self.container=Frame(self.wholeContainer,bg='#B0C4DE',padx=PAD_XCOLUMN1)
        self.container.grid(row=0,column=0,sticky=NSEW)
        self.container.columnconfigure(0,weight=1)
        
        self.column1=Frame(self.container,bg='#B0C4DE')
        self.column1.grid(row=0,column=0,sticky=NSEW)
        
        fname=Label(self.column1,text='Name :',font=('times new roman',20,'bold'),
        fg='black',bg='#B0C4DE')
        fname.grid(row=0,column=0,sticky="nsw",padx=PAD_XCOLUMN1)
        self.fentry=Entry(self.column1,font=('times new roman',18,'bold'),relief=RIDGE)
        self.fentry.grid(row=1,column=0,sticky=NSEW,padx=PAD_XCOLUMN1)
        
        
        class_label=Label(self.column1,text='Class :',font=('times new roman',20,'bold'),
        fg='black',bg='#B0C4DE')
        class_label.grid(row=0,column=2,sticky="nsw",padx=PAD_XCOLUMN1)
        
        self.class_combovar=StringVar()
        self.class_combo=ttk.Combobox(self.column1,values=CLASSES,textvariable=self.class_combovar,font=('times new roman',18,'bold'))
        self.class_combo.grid(row=1,column=2,sticky=NSEW,padx=PAD_XCOLUMN1)
        self.class_combo.config(state='readonly')
        self.class_combovar.set(SELECT_CLASS)
        self.class_combovar.trace_add("write",lambda *Args:self._change_section())


        self.column2=Frame(self.container,bg='#B0C4DE')
        self.column2.grid(row=1,column=0,sticky=NSEW,pady=20)
        
        class_label=Label(self.column1,text='SECTION :',font=('times new roman',20,'bold'),
        fg='black',bg='#B0C4DE')
        class_label.grid(row=0,column=3,sticky="nsw",padx=PAD_XCOLUMN1)
        self.section_combo=ttk.Combobox(self.column1,font=('times new roman',18,'bold'))
        self.section_combo.grid(row=1,column=3,sticky=NSEW,padx=PAD_XCOLUMN1)
        self.section_combo.config(state='readonly')
        self.section_combo.set(SELECT_SECTION)
        
        contact=Label(self.column2,text='Contact :',font=('times new roman',20,'bold')
        ,fg='black',bg='#B0C4DE')
        contact.grid(row=0,column=0,sticky="nsw",padx=PAD_XCOLUMN1)
        
        self.contact_entry=Entry(self.column2,font=('times new roman',18,'bold'),relief=RIDGE)
        self.contact_entry.grid(row=1,column=0,sticky=NSEW,padx=PAD_XCOLUMN1)
        
        rollno=Label(self.column2,text='ID No :',font=('times new roman',20,'bold'),
        fg='black',bg='#B0C4DE')
        rollno.grid(row=0,column=1,sticky="nsw")
        self.rollLabel=Label(self.column2,font=('times new roman',18,'bold'),fg='black',bg='#B0C4DE')
        self.rollLabel.grid(row=1,column=1,sticky=NSEW,padx=PAD_XCOLUMN1)

        h_frame=Frame(self.container,bg='#B0C4DE',height=PADY_BOTTOM)
        self.message_data=Label(h_frame,font=('times new roman',18,'bold'),fg='black',bg='#B0C4DE')
        self.message_data.pack()
        h_frame.grid(row=2,column=0,sticky=NSEW,)
        
        self.container2=Frame(self.wholeContainer,bg='#B0C4DE',padx=PAD_XCOLUMN1,pady=20)
        self.container2.grid(row=0,column=1,sticky=NSEW)
        self.container2.columnconfigure(0,weight=1)
        
        button=Button(self.container2,text='ADD' ,font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.add_student())
        button.grid(row=0,column=0,sticky=NSEW)

        sbutton=Button(self.container2,text='UPDATE' ,font=('times new roman',15,'bold')
        ,relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.update_stud())
        sbutton.grid(row=1,column=0,sticky=NSEW)

        sbutton=Button(self.container2,text='DELETE' ,font=('times new roman',15,'bold')
        ,relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.delet_stud())
        sbutton.grid(row=2,column=0,sticky=NSEW)

        button=Button(self.container2,text='CLEAR' ,font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.clear())
        button.grid(row=3,column=0,sticky=NSEW)
        
        button=Button(self.container2,text='QRCode' ,font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4',command=lambda:self.generate_code())
        button.grid(row=4,column=0,sticky=NSEW)
    def delet_stud(self):
        pass
    
    def write_massage(self,message:str):
        self.message_data.text=message
    def update_stud(self,):
        if self.class_combo.get()==SELECT_CLASS:
            return messagebox.showerror("Error",'Please Select Class')
        elif self.section_combo.get()==SELECT_SECTION:
            return messagebox.showerror("Error",'Please Select Section')
        else:return True
        
    def update_classes(self,new_classes):
        self.classes=new_classes
        self.class_combo.values=list(new_classes.keys())
        self.class_combovar.set(SELECT_CLASS)
        self.section_combo.set(SELECT_SECTION)
        self.section_combo.values=[]
    def generate_code(self):
        pass
    def _change_section(self):
        if self.class_combo.get()!=SELECT_CLASS:
            self.section_combo["values"]=self.classes[self.class_combo.get()]
       
    def get_data(self):
        return self.fentry.get(),self.class_combo.get(),self.section_combo.get(),self.contact_entry.get(),\
    
    def clear_allMethdod(self):
        self.fentry.delete(0,END)
        self.rollLabel.text=""
        self.contact_entry.delete(0,END)
        self.write_massage("")
    def add_student(self):
        if len(self.fentry.get().replace(" ",""))==0:
            messagebox.showerror("Error",'All fields are required')
            return 
        elif self.class_combo.get()==SELECT_CLASS:
            messagebox.showerror("Error",'Please Select Class')
            return 
        elif self.section_combo.get()==SELECT_SECTION:
            messagebox.showerror("Error",'Please Select Section')
            return 
        else:
            values=self.get_data()
            self.clear_allMethdod()
            return values
    def add_values(self,**kwargs):
        values1:Dict[str,Entry]={NAME:self.fentry,CONTACT:self.contact_entry}
        
        values2:Dict[str,List[ttk.Combobox,list]]={CLASS:(self.class_combo,list(self.classes.keys()))}
        for (key,value) in kwargs.items():
            if key ==CLASS:
                if value in values2[key][1]:
                    values2[key][0].set(value)
                    class_s=value
            elif key in list(values1.keys()):
                values1[key].delete(0,END)
                values1[key].insert(0,value)
            elif key==ID:
                self.rollLabel["text"]=value
     
        sections= self.classes[class_s]
        if (SECTION in list(kwargs.keys())):
            if kwargs[SECTION] in sections:
                self.section_combo.set(kwargs[SECTION])
                
          
    def clear(self):
        self.fentry.delete(0,END)
        self.contact_entry.delete(0,END)
        self.class_combovar.set(SELECT_CLASS)
        self.section_combo.set(SELECT_SECTION)
        self.rollLabel["text"]=""
    
if __name__=="__main__":
    root=Tk()
    classes={'First Year(CS)':[1,2,3,4],'Second Year(CS)':[1,2,3,4],
                      'Third Year(CS)':['First Year(IT)','Second Year(IT)','Third Year(IT)']}
    var=ManageStudents(classes)
    var.add_values(idNo="ggg")
    var.pack(fill=BOTH)
    
    root.mainloop()