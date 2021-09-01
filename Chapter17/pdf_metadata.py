import PyPDF2
import sys

def print_metadata(filename):
    pdf_file = PyPDF2.PdfFileReader(filename,"rb") 
    doc_info = pdf_file.getDocumentInfo()
    print(f"[*] PDF MetaData For: {filename}")
    for meta_item in doc_info:
        print(f"[+] {meta_item} :: {doc_info[meta_item]}")

print_metadata(r"D:\Downloads\Python Security eCourseware.pdf")