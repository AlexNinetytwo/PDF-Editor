import pikepdf
import os

def spilt(folderpath):
    directory = os.fsencode(folderpath)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        foldername = filename[:-4]
        old_pdf = pikepdf.Pdf.open(folderpath + "/" + filename)
        os.mkdir(folderpath + "/" + foldername)
        for n, page_can in enumerate(old_pdf.pages):
            new_pdf = pikepdf.Pdf.new()
            new_pdf.pages.append(page_can)
            name = filename[:-4] + "_" + str(n) + filename[-4:]
            new_pdf.save(folderpath + "/" + foldername + "/" + name)

def merge(folderpath):
    new_pdf = pikepdf.Pdf.new()
    directory = os.fsencode(folderpath)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename[-4:] == ".pdf":
            old_pdf = pikepdf.Pdf.open(folderpath + "/" + filename)
            new_pdf.pages.extend(old_pdf.pages)
    os.mkdir(folderpath + "/" + "bind")
    new_pdf.save(folderpath + "/bind/bind.pdf")

if __name__ == "__main__":
    merge("C:/Users/Schumacher/Desktop/kontoauszüge")