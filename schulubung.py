import os

#convert pdf to html
for root,dirs,files in os.walk("data"):
    for filee in files:
        filee_html = filee.replace(".pdf",".html")
        filee_html = "data\\html\\" + filee_html
        if (not os.path.exists(filee_html)):
            print(filee_html)
            config = "--zoom 1.3 --dest-dir data\\html data\\%s" % filee
            os.system("pdf2htmlEX-win32-0.14.6-with-poppler-data\\pdf2htmlEX.exe "+str(config))

#change all the html files
for filee in os.listdir("data\\html"):
    filee = "data\\html\\" + filee
    print(filee)
