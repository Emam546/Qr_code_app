from tkinter import *
from tkinter import ttk
from manage_students import SELECT_CLASS,SELECT_SECTION
from typing import Dict, Iterable
from _constants import ID,CLASSES
SELECTOPTION="Select Option"

class SearchWidget(Frame):
    def __init__(self,searchby:list,*args,**kwargs):
        super().__init__(relief=FLAT,bg='white',pady=13,padx=15,*args,**kwargs)
        self.searchby=searchby
        # searchby=Label(self,text='Search By',font=('times new roman',20,'bold'),
        # fg='black',bg='white')
        # searchby.grid(row=0,column=0,padx=30)
        # self.scombo=ttk.Combobox(self,values=self.searchby,font=('times new roman',18,'bold'))
        # self.scombo.grid(row=0,column=1,padx=1)
        # self.scombo.set(SELECTOPTION)
        # self.scombo.config(state='readonly')

        self.sentry=Entry(self,font=('times new roman',18,'bold'),relief=RIDGE,bd=2,bg='#F5F5DC')
        self.sentry.grid(row=0,column=2)

        self.search_button=Button(self,text='Search By Name',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4')
        self.search_button.grid(row=0,column=3,padx=30)

        self.show_button=Button(self,text='Show All',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4')
        self.show_button.grid(row=0,column=4,padx=0)
        
        self.selectAllButton=Button(self,text='Select ALL',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4')
        self.selectAllButton.grid(row=0,column=5,padx=0)
        
        self.selectDEAllButton=Button(self,text='Deselect ALL',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4')
        self.selectDEAllButton.grid(row=0,column=6,padx=0)
        
        self.columnconfigure(7,weight=1)
        self.section_button=Button(self,text='Section',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4')
        self.section_button.grid(row=0,column=7,sticky="e")
        
        self.columnconfigure(8,weight=1)
        self.id_scannerbutton=Button(self,text='ID Scanner',font=('times new roman',15,'bold'),
        relief=GROOVE,bd=4,fg='black',bg='#7FFFD4')
        self.id_scannerbutton.grid(row=0,column=8,sticky="e")

class THELISTBOX(Frame):
    def __init__(self,searchby:list,classes:Dict[str,list],keys:list,*args,**kwargs):
        super().__init__(relief=FLAT,bg='#B0C4DE',
                        padx=7,pady=7,
                         *args,**kwargs)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(2,weight=1)
        
        self.searchWidget=SearchWidget(searchby,self,)
        self.searchWidget.grid(row=0,column=0,sticky=NSEW)
        self.searchby=self.searchWidget.searchby
        
        self.selectchoice=SELECT_CHOICE(classes,self)
        self.selectchoice.grid(row=1,column=0,sticky=NSEW,pady=10)
        
        self.listboxframe=LISTBOX_FRAME(keys,self)
        self.listboxframe.grid(row=2,column=0,sticky=NSEW)

        self.searchWidget.selectAllButton["command"]=lambda:self.listboxframe.selectAll(True)
        self.searchWidget.selectDEAllButton["command"]=lambda:self.listboxframe.selectAll(False)
        
class SELECT_CHOICE(Frame):
    def __init__(self,classes:Dict[str,list],*args,**kwargs):
        super().__init__(relief=FLAT,bg='#B0C4DE',*args,**kwargs)
        self.classes=classes
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        
        self.section_combovar=StringVar()
        self.section_combo=ttk.Combobox(self,textvariable=self.section_combovar,font=('times new roman',18,'bold'))
        self.section_combo.grid(row=0,column=1,sticky="nsw")
        self.section_combo.set(SELECT_SECTION)
        self.section_combo.config(state='readonly')
        self.section_combovar.trace_add("write",lambda *Args:self._track_updating())
        
        self.class_combovar=StringVar()
        self.class_combo=ttk.Combobox(self,textvariable=self.class_combovar,values=CLASSES,font=('times new roman',18,'bold'))
        self.class_combo.grid(row=0,column=0,sticky="nse",padx=40)
        self.class_combovar.set(SELECT_CLASS)
        self.class_combo.config(state='readonly')
        self.class_combovar.trace_add("write",lambda *Args:[self._change_section(),self._track_updating()])
    def _change_section(self):
        if self.class_combo.get()!=SELECT_CLASS:
            self.section_combo["values"]=self.classes[self.class_combo.get()]
    def update_classes(self,new_classes:dict):
        self.classes=new_classes
        self.class_combo.values=list(new_classes.keys())
        self.class_combovar.set(SELECT_CLASS)
        self.section_combo.set(SELECT_SECTION)
        self.section_combo.values=[]  
    def _track_updating(self):
        pass 
    @property
    def choices(self):
        return (self.class_combo.get() if self.class_combo.get()!=SELECT_CLASS else None),\
        (self.section_combo.get() if self.section_combo.get()!=SELECT_SECTION else None)
class LISTBOX_FRAME(Frame):
    def __init__(self,KEYS:list,*args,**kwargs):
        super().__init__(relief=FLAT,bg='#B0C4DE',*args,**kwargs)
        
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        
        self.treview = ttk.Treeview(self, columns=[i for i in range(1,len(KEYS)+1)],show='headings',height=11,        )
        self.style=ttk.Style()
        self.style.configure('Treeview',background='lightgray',foreground='black',rowheight=20)
        self.style.map('Treeview',background=[('selected','green')])

        for i,key in enumerate(KEYS,1):
            self.treview.heading(i, text=key)
            self.treview.column(i,anchor=CENTER)

        self.treview.grid(row=0,column=0,sticky=NSEW)
        #self.treview.bind("<ButtonRelease-1>",self.click_insert)
        
        
        self.scroll_y =ttk.Scrollbar(self, orient=VERTICAL,command=self.treview.yview)
        self.scroll_x=ttk.Scrollbar(self,orient=HORIZONTAL,command=self.treview.xview)
        #self.scroll_x.grid(row=1,column=0,sticky=NSEW)
        self.scroll_y.grid(row=0,column=1,sticky=NSEW)
        self.treview.config(yscrollcommand=self.scroll_y.set)
        self.treview.bind('<<TreeviewSelect>>', lambda e:self.click_insert())
    def click_insert(self):
        pass

        
    def tree(self,values:list):
        self.treview.delete(*self.treview.get_children())
        for i in values:
            self.treview.insert('', 'end', values=i)
    def selectAll(self,state):
        if state:
            self.treview.selection_add(*self.treview.get_children())
        else:
            self.treview.selection_remove(*self.treview.selection())
            #self.treview.selection_clear()
    def delet_item(self,id):
        if not isinstance(id,Iterable):
            id=[id]
        for item in self.treview.get_children():
            for item["values"][ID] in id:
                self.treview.delete(item)
    
    def delete_all(self):
        self.treview.get_children(*self.treview.get_children())
if __name__=="__main__":
    root=Tk()
    k=['ID_No','Email','Contact']
    classes={'First Year(CS)':[1,2,3,4],'Second Year(CS)':[1,2,3,4],
                    'Third Year(CS)':['First Year(IT)','Second Year(IT)','Third Year(IT)']}
    listbox=THELISTBOX(k,classes,k)
    listbox.pack()
    

    values=([f"id {i}",f"Email {i}",f"Contact {i}"] for i in range(100) )
    listbox.listboxframe.tree(values)  
    
    root.mainloop()