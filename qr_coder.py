import webbrowser
import os
import barcode
from bs4 import BeautifulSoup
from _constents import *
from typing import List,Tuple
FILE_NAME="index.html"
FILE_NAME=os.path.join(os.path.dirname(__file__),FILE_NAME)
if not os.path.exists(FILE_NAME):
    with  open(FILE_NAME,"w") as g:
        g.write(DEFAULTTEMLET)
 
CODE = barcode.get_barcode_class(BARCODE)
def ides(*ids:List[Tuple[str,str]],Numof_repeat=5):
    with open(FILE_NAME,"r") as htmlf:
        htmlRead=BeautifulSoup(htmlf.read(),"html.parser")
    htmlRead.body.clear()
    codes=[]
    for id in ids:
        try :
            ean = CODE(id[0])
            text = ean.render()
            container=htmlRead.new_tag("div",)
            for _ in range(Numof_repeat):
                svg= BeautifulSoup(text,"html.parser").find("svg")
                svg.find("text").string=str(id[1])
                container.append(svg)
            htmlRead.body.append(container)
            codes.append(ean)
        except Exception as e:
            print(e)
        #print(container)
    if not (len(codes)):
        return []
    with open(FILE_NAME,"w", encoding="utf-8") as htmlf:
        htmlf.write(htmlRead.prettify())
 
    webbrowser.open(FILE_NAME,1,True)
    return 

if __name__=="__main__":
    code1=CODE(str(10**12))
    code2=CODE(str(code1))
    code3=CODE(str(code2))
    print(code1,code2,code3)
    #ides(("555555555555","محمود امام"),("555555555555","Ahemd"))