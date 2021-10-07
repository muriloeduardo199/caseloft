import re
import fitz


def extract_text(filepath: str) -> str:
    """Using PyMuPDF do extract PDF text - https://pypi.org/project/PyMuPDF/
    Arguments:
        filepath {str} -- pdf path to extract 
    Returns:
        str -- Document text
    """

    doc = fitz.open(filepath)
    doc_text = ""
    for page in doc:
        page_text = page.get_text()
        doc_text = doc_text + " " + page_text

    doc_text = re.sub(r" {2,}", " ", doc_text)
    # TODO: Remover todos os espaços excedentes final ou inicio do texto (str.strip)
    return doc_text.strip()
