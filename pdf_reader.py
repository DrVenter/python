import PyPDF2

file = open("MT Monthly Despatches - May 2022.pdf", 'rb')
reader = PyPDF2.PdfFileReader(file)


number_of_pages = len(reader.pages)

text = ""
for pg in range(number_of_pages):
    page = reader.getPage(pg)
    text += page.extractText()

#text = set(text.lower().split())
print(text)

file.close()