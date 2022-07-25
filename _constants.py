import json
import os
KEYS=["Name","Class","Section","Contact","ID"]
NAME,CLASS,SECTION,CONTACT,ID=KEYS
SEARCHBY=[NAME,CONTACT]
SELECT_CLASS  ="         Select Class        "
SELECT_SECTION="        Select Section       "

DEFAULTTEMLET="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        *,::after,::before{
            margin: 0;
            padding: 0;
        }
        div{
            width: 100%;
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-top: 5vh;
        }
    </style>
</head>
<body>
    
</body>
</html>
"""
__DEFAULSETTING={
    "BARCODE_TYPE": "ean",
    "NUMOFREPEAT": 5,
    "CLASSES": [
        "Frist Class",
        "Second Class",
        "Third CLASS"
    ]
}

    
try:
    with open("settings.json","r") as f:
        settings=json.load(f)
    BARCODE=settings["BARCODE_TYPE"]
    NUMOFREPEAT=settings["NUMOFREPEAT"]
    CLASSES=settings["CLASSES"]
    
    
except:
    with open("settings.json","w") as f:
        json.dump(__DEFAULSETTING,f)
    settings=__DEFAULSETTING
    BARCODE=settings["BARCODE_TYPE"]
    NUMOFREPEAT=settings["NUMOFREPEAT"]
    CLASSES=settings["CLASSES"]
    

    


