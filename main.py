from PyPDF2 import PdfWriter
import os


# function to check if there is any pdf on the folder
def pdfChecker():
    folder = os.listdir("PDF to Merge")
    for i in folder:
        if i.endswith("pdf"):
            pdf_list.append(i)  # filtering pdf and adding it to the list
    if pdf_list == []:  # notifying if pdf don't exist
        print("There is no PDF file. Please add pdf you want merge.")
        exit()


# function for checking if the default folder exit if not create one
def folderChecker():
    check_folder = os.listdir()
    folder_list = []
    for i in check_folder:
        folder_list.append(i)
    if "PDF to Merge" not in folder_list:  # create folder if not exist
        os.mkdir("PDF to Merge")


# function to merge the PDF
def pdfMerger():
    os.chdir("PDF to Merge")  # changing working directory to Merge PDF
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("Merged_PDF.pdf")  # merging the PDF
    merger.close()
    print("PDF successfully Merged!!")


# calling required functions
folderChecker()
pdf_list = []
pdfChecker()
pdfMerger()
