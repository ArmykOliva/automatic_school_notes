import os
from bs4 import BeautifulSoup
import random

#init
fonts = ["veranda","arial","Algerian"]


#convert pdf to html
for root,dirs,files in os.walk("data"):
    for filee in files:
        filee_html = filee.replace(".pdf",".html")
        filee_html = "data\\converted\\" + filee_html
        if (not os.path.exists(filee_html)):
            print(filee_html)
            config = "--zoom 1.3 --dest-dir data\\converted data\\%s" % filee
            os.system("pdf2htmlEX-win32-0.14.6-with-poppler-data\\pdf2htmlEX.exe "+str(config))

#change all the html files
for filee in os.listdir("data\\converted"):
    filee = "data\\converted\\" + filee
    #find text and change it
    with open(filee,"r",encoding="utf-8") as f:
        result = f.read()
        whole_file = BeautifulSoup(result,"html.parser")
        schulubung = whole_file.find("div",attrs={"id" : "page-container"})
        #najit pages
        for data in schulubung.children:
            #page cislo
            if (data.name == "div"):
                #najit jenom page
                this_page = False
                for page in data.find("div"):
                    if (this_page): #jenom ten spravnej text
                        #for loop mezi divs
                        for divs in page.children:
                            #loop v divu a randomize fontu
                            line = divs.decode_contents()
                            res = ""
                            i = 0
                            while i < len(line):
                                if (line[i:i + 1] == " "):
                                    res += line[i:i + 1]
                                elif (line[i:i + 5] == "<span" or line[i:i + 6] == "</span"):
                                    while line[i:i + 1] != ">":
                                        res += line[i:i + 1]
                                        i += 1
                                    res += ">"
                                else:
                                    word = ["<font face='{0}'>".format(random.choice(fonts)),"</font>"]
                                    res += word[0] + line[i:i + 1] + word[1]
                                i += 1
                            divs.string = res
                    this_page = not this_page
                print("\n\ngay\n\n")

                

    #write new file
    with open(filee.replace("converted","done"),"w",encoding="utf-8") as f:
        whole_file = str(whole_file).replace("&lt;","<")
        whole_file = whole_file.replace("&gt;",">")
        f.write(str(whole_file))
        print("done")