import os
import json

#load config
configF = open("config.json")
config = json.load(configF)

#combine all markdown files
wholeMarkdown = ""
for kapitel in config["kapitel"]:
    md = open("./Kapitel/"+kapitel+"/text.md").read()
    md = md.replace("Dateien\\","Dateien-"+kapitel+"\\")
    wholeMarkdown += "\n\n\\newpage\n\n"+ str(md)
    #copy dateien
    copyPDF = "xcopy Kapitel\\"+kapitel+"\\Dateien chache\\Dateien-"+kapitel+" /E/H/Y/i"
    print(copyPDF)
    os.system(copyPDF)


#append header information to File
header = open("header.md").read()

header = header.replace("<author-placeholder>",config["author"])
header = header.replace("<title-placeholder>",config["titel"])

wholeMarkdown = header + "\n\n" + wholeMarkdown



out = open("chache/combined.md","w")
out.write(wholeMarkdown)
out.close()

createLatex = "pandoc chache/combined.md -f markdown -t latex -s -o chache/out.tex --listings"

os.system(createLatex)

createPDF = "cd chache & lualatex out.tex"
os.system(createPDF)

createPDF = "cd chache & lualatex out.tex"
os.system(createPDF)

copyPDF = "copy chache\out.pdf ."

os.system(copyPDF)

#clear chache
#os.system("rmdir /s /q .\chache")