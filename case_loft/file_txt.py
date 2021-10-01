import sys, fitz


fname = sys.argv[0]  # get document filename
doc = fitz.open("arquivos_pdf/Contrato 1.pdf")  # open document
out = open(fname + ".txt", "wb")  # open text output
for page in doc:  # iterate the document pages
     text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
     out.write(text)  # write text of page#     out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
     areas = page.search_for('R$ 800.000,00')
out.close()

# with open ('file.txt', 'w') as  arquivo:
#     for regex in txt:
#         arquivo.write(str(regex))
