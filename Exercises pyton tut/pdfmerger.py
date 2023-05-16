# from PyPDF2 import PdfReader

# reader = PdfReader("pdf1.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text)

# Import required library.
import pdfplumber 
# print(help(pdfplumber))

# # Open the file and create a pdf object.
pdf = pdfplumber.open("result.pdf")

# # Get the number of pages.
# numPages = len(pdf.pages)

# print("Number of Pages:", numPages)

# # Iterate over each page and extract the text of each page.
for number, pageText in enumerate(result.pdf):
    print("Page Number:", number)
    print(pageText.extract_text())


# print(dir(pdfplumber))

# from PyPDF2 import PdfMerger

# pdfs = ['pdf1.pdf', 'pdf2.pdf', 'pdf3.pdf']

# merger = PdfMerger()

# for pdf in pdfs:
#     merger.append(pdf)

# merger.write("result.pdf")
# merger.close()

