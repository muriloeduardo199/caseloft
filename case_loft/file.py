import os
from time import perf_counter
import fitz
from nltk.tokenize import RegexpTokenizer

arqPDF1 = "arquivos_pdf/Contrato 1.pdf"

arqPDF2 = "arquivos_pdf/Contrato 2.pdf"

# arqPDF3 = "arquivos_pdf/Contrato 3.pdf"

# arqPDF4 = "arquivos_pdf/Contrato 4.pdf"

# arqPDF5 = "arquivos_pdf/Contrato 6.pdf"

# arqPDF6 = "arquivos_pdf/Contrato teste.pdf"

# lista de arqs
PDFlist = [arqPDF1, arqPDF2]

def saveText(texto, fileName, nameLib):
     """Save the text in a file
     Arguments:
         texto {str} -- text in str format
         fileName {str} -- filename (without path in this code)
         nameLib {str} -- name of extractor project
     """
     arq = open(fileName + "-" + nameLib + ".txt", "w")
     arq.write(texto)
     arq.close()


def extractPDFwithPyMuPDF(arqs):
     """Using PyMuPDF do extract PDF text - https://pypi.org/project/PyMuPDF/
     Arguments:
         arqs {str} -- A list of filenames with path
     """
     for arq in arqs:
         timeIni = perf_counter()
         doc = fitz.open(arq)
         textoCompleto = ""
         for page in doc:
             texto = page.getText("text")
             textoCompleto = textoCompleto + texto
         fileName = os.path.basename(arq)
         timeEnd = perf_counter()
         timeTotal = timeEnd - timeIni
         printMiniReport(textoCompleto, fileName, "PyMuPDF", timeTotal)
         saveText(textoCompleto, fileName, "PyMuPDF")
         doc.close()
     print("--- PyMuPDF ---" )

def printMiniReport(texto, fileName, nameLib, timeConversion):
    """Shows in the screen, some informations to help compare performance in extract file
    Arguments:
        texto {str} -- text in str format
        fileName {str} -- filename (without path in this code)
        nameLib {str} -- name of extractor project
        timeConversion {float} -- time in seconds
    """    
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(texto)
    print(nameLib, " - ", fileName, " - Total of chars: ", str(len(texto)) )
    print(nameLib, " - ", fileName, " - Total of tokens: ", str(len(tokens)) )
    print(nameLib, " - ", fileName, " - Extract time in seconds: ", str(timeConversion) )


extractPDFwithPyMuPDF(PDFlist)



# text = ""
# with fitz.open("arquivos_pdf/Contrato 1.pdf") as pdf:

#     for page in pdf :
#         text += page.getText()
#     text
# text = re.search(r"3\.1\. R\$\s(?P<valor_venda>[\d.,]+).*?\n", text)

# print(text)


# fname = sys.argv[0]  # get document filename
# doc = fitz.open("arquivos_pdf/Contrato 1.pdf")  # open document
# out = open(fname + ".txt", "wb")  # open text output
# for page in doc:  # iterate the document pages
#      text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
#      out.write(text)  # write text of page#     out.write(bytes((12,)))  # write page delimiter (form feed 0x0C)
#      areas = page.search_for('R$ 800.000,00')
# out.close()









