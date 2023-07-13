import PyPDF2

file = open("Working_Business_Proposal.pdf", "rb")
file1 = PyPDF2.PdfReader(file)
page_one = file1.pages[0]

Pdf_practice = PyPDF2.PdfWriter()
Pdf_practice.add_page(page_one)
pdf_output = open("new_PDF.pdf", "wb")
Pdf_practice.write(pdf_output)
file.close()
