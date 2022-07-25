from email import message
from tkinter import *
from tkinter import ttk
from tokenize import Name
from edit_sections import EDIT_SECTIONLEVEL
from manage_students import *
from listbox import *
import pandas as pd
from tkinter import messagebox
import os
import difflib
from _constents import *
from qr_coder import ides,CODE
import random
from id_scanners import IdScaaner
from playsound import playsound
import numpy as np

DATAFILENAME=os.path.join(os.path.dirname(__file__),"data.json")

class Mainapp(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        try:
            self.DB=pd.read_json(DATAFILENAME,orient="records")
        except:
            open(DATAFILENAME,"w")
            self.DB=pd.DataFrame(columns=KEYS)
            self.save_data()
                
        self.DB=self.DB.reindex(columns=KEYS)
        classes:Dict[str,list]={}
        for c in CLASSES:
            classes[c]=[]
        for section in self.DB[SECTION].unique():
            c=self.DB[self.DB[SECTION]==section][CLASS].unique()
            if len(c) and c[0] in classes:classes[c[0]].append(section)
        self.classes=classes
        self.title("STUDENT MANAGEENT SYSTEM")
        self.bigcontainer=Frame(self,bg='#DC143C',relief='flat')
        self.bigcontainer.pack(fill=BOTH,expand=YES)
        self.bigcontainer.columnconfigure(0,weight=1)
        self.bigcontainer.rowconfigure(1,weight=1)
        
        self.heading_label=Label(self.bigcontainer,text='Student Management System'
       ,fg='black',bg='#DC143C',font=('times new roman',35,'bold'))
        self.heading_label.grid(row=0,column=0,sticky=NSEW)
        self.container=ttk.Panedwindow(self.bigcontainer,)
        self.container.grid(row=1,column=0,sticky=NSEW)
        self.listBox=THELISTBOX(SEARCHBY,classes,KEYS,self.container)
        
        #self.listBox.grid(row=1,column=0,sticky=NSEW)
        self.manageStudents=ManageStudents(classes,self.container)
        
        bottom=Label(self.bigcontainer,text='Created by Emam Ashour to contact 01091907365'
       ,fg='black',bg='#DC143C',font=('times new roman',10,'bold'),anchor="w")
        bottom.grid(row=3,column=0,sticky=NSEW)
        
        self.manageStudents.add_student=self.add_new_student
        self.manageStudents.delet_stud=self.delet_stud
        self.manageStudents.update_stud=self.update_stud
        self.manageStudents.generate_code=self.generate_codes
        self.listBox.serachWidget.search_button["command"]=self._search_in
        self.listBox.serachWidget.show_button["command"]=self.showAll
        self.listBox.listboxframe.click_insert=self.showInfo
        self.listBox.selectchoice._track_updating=self.showAll
        self.listBox.serachWidget.section_button["command"]=self.pop_section_up
        self.listBox.serachWidget.id_scannerbutton["command"]=self.pop_idscanner
        
        #self.manageStudents.grid(row=2,column=0,sticky=NSEW)
        self.container.add(self.listBox)
        self.container.add(self.manageStudents)
        self.showAll()
    def update_classes(self,new_classes):
        self.manageStudents.update_classes(new_classes)
        self.listBox.selectchoice.update_classes(new_classes)
        if hasattr(self,"top_level") and self.toplevel.winfo_exists():
            self.toplevel.update_name.update_classes(new_classes)
    def save_data(self):
        if not os.path.exists(DATAFILENAME):
            #create the file
            open(DATAFILENAME,"w")
        self.DB.to_json(DATAFILENAME,orient="records")
    def _search_in(self):
        searchvalue=self.listBox.serachWidget.sentry.get()
        class_,section=self.listBox.selectchoice.chioces
        thelist=self.DB
        if class_:
            thelist=self.DB[self.DB[CLASS]==class_]
            if section:
                thelist=thelist[self.DB[SECTION]==section]
        mathces=difflib.get_close_matches(searchvalue,list(thelist[NAME]))
        self.tree(
            self.DB[self.DB[NAME].isin(mathces)].to_dict(orient="records")
            )
    def showAll(self):
        class_,section=self.listBox.selectchoice.chioces
        thelist=self.DB
        if class_:
            thelist=self.DB[self.DB[CLASS]==class_]
            if section:
                thelist=thelist[thelist[SECTION]==section]
        self.tree(thelist.to_dict(orient="records"))
    def tree(self,values):
     
        values=[list(val.values()) for val in values]
        self.listBox.listboxframe.tree(values)
    def add_new_student(self):
        values=ManageStudents.add_student(self.manageStudents)
        if not values:
            return
        name,classname,section,contact=values
        id=CODE(random.randint(1e12,1e13-1).__str__()).__str__()
        while id in self.DB[ID].values:
            id=CODE(random.randint(1e12,1e13-1).__str__()).__str__()
        self.DB=self.DB.append({
            NAME:name,
            CLASS:classname,
            SECTION:section,
            CONTACT:contact,
            ID:str(id)
           },ignore_index=True)
        
        self.manageStudents.write_massage("A new student was added")
        self.save_data()
        self.showAll()
    def delet_stud(self):
        ManageStudents.delet_stud(self.manageStudents)
        
        treview=self.listBox.listboxframe.treview
        selections=treview.selection()
        items=[treview.item(select) for select in selections]
        
        values=[select["values"][KEYS.index(ID)] for select in items]
        if len(selections):
            self.DB=self.DB[~self.DB["ID"].isin(values)]
            self.save_data()
            if (len(values)>1):
                self.manageStudents.write_massage(f"{len(values)} Student were deleted")
            else:
                name_stu=items[0]["values"][KEYS.index(NAME)]
                self.manageStudents.write_massage(f"{name_stu} was deleted")
            treview.delete(*selections)
        else:
            messagebox.showerror("Error",'You must select something')
    def update_stud(self,):
        if ManageStudents.update_stud(self.manageStudents)!=True:
            return
        treview=self.listBox.listboxframe.treview
        selections=[treview.item(select) for select in treview.selection()]
        
        if len(selections):
            IDS=[select["values"][KEYS.index(ID)] for select in selections]
            if (len(IDS)>1):
                _,classID,SectionId,_=self.manageStudents.get_data()
            
                self.DB.loc[self.DB["ID"].isin(IDS),[CLASS,SECTION]]=classID,SectionId
                self.manageStudents.write_massage(f"{len(selections)} Student were Updated")
                
            else:
                if self.manageStudents.fentry.get()=="":
                    return messagebox.showerror("ERROR","Name field is required")
                Name,classID,SectionId,contact=self.manageStudents.get_data()
                self.DB.loc[self.DB["ID"].isin(IDS)]=Name,classID,SectionId,contact
                name_stu=selections[0][KEYS.index(NAME)]
                self.manageStudents.write_massage(f"{name_stu} was Updated")
            self.save_data()
            self.tree(self.DB[self.DB["ID"].isin(IDS)].to_dict("records"))
        else:
            messagebox.showerror("Error",'You must select something') 
        
    def showInfo(self):
        treview=self.listBox.listboxframe.treview
        if not len(treview.selection()):
            return
        self.manageStudents.clear()
        start,end=0,len(KEYS)
        if len(treview.selection())>1:
            start,end=1,3
        item=treview.item(treview.selection()[0])
        the_dict={}
        i=start
        for key in KEYS[start:end]:
            the_dict.update({key:item["values"][i]})
            i+=1
        self.manageStudents.add_values(**the_dict)
      
    def generate_codes(self):
        treview=self.listBox.listboxframe.treview
        selections=[treview.item(select) for select in treview.selection()]
        if len(selections):
            IDS=[(select["values"][KEYS.index(ID)].__str__(),select["values"][KEYS.index(NAME)])\
                for select in selections]
            ides(*IDS)
        else:
            messagebox.showerror("Error",'You must select something') 
              
    def check_entry(self):
        value=self.toplevel.newname.__class__.check_entry(self.toplevel.newname)
        if value:
            class_,name=value
    
            self.classes[class_].append(name)
            self.update_classes(self.classes)
            self.toplevel.newname.clear()

    def update_sectionName(self,):
        value=self.toplevel.update_name.__class__.check_entry(self.toplevel.update_name)
        if not value:return
        class_,section,newname=value
        if section not in self.classes[class_]:
            return messagebox.showerror("ERROR","The section has been updated")
        self.classes[class_].remove(section)
        
        self.classes[class_].append(newname)
        self.DB.loc[self.DB[SECTION]==section,[SECTION]]=newname
        self.toplevel.update_name.clear()
        self.update_classes(self.classes)
        self.save_data()
        self.showAll()
        
    def pop_section_up(self):
        if hasattr(self,"top_level") and self.toplevel.winfo_exists():
            self.toplevel.lift()
        self.toplevel=EDIT_SECTIONLEVEL(self.classes,self)
        self.toplevel.newname.check_entry=self.check_entry
        self.toplevel.update_name.check_entry=self.update_sectionName
    def scanId(self,):
        value=self.idscanner.__class__.check(self.idscanner)
        if value:
            results=self.DB[self.DB[ID].astype(np.str)==str(value)].to_dict("records")
            if len(results):
                self.manageStudents.add_values(**results[0])
                playsound("chimes.wav",False)
                self.idscanner.clear()
                return True
            
            return False
                
                
    
    def pop_idscanner(self):
        if hasattr(self,"idscanner") and self.idscanner.winfo_exists():
            self.idscanner.lift()
        self.idscanner=IdScaaner(self)
        self.idscanner.check=self.scanId
        
        
if __name__=="__main__":
    app=Mainapp()

    app.mainloop()
        
        