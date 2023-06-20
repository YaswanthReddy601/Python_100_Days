import PyPDF2

file = open("Working_Business_Proposal.pdf", "rb")
file1 = PyPDF2.PdfWriter(file)
last_page = file1.pages[0]

file2 = PyPDF2.PdfWriter()
file2.add_page(last_page)
final_file = open("new_PDF.pdf", "ab")
file2.write(final_file)
file.close()


