from typing import List
from case_loft.extractor import extrair_dados_arquivos
from pathlib import Path


def test_extrair_dados_arquivos(pdf_file_list: List[Path]):
    df = extrair_dados_arquivos(pdf_file_list)
    assert len(df) == len(pdf_file_list)
    assert df[df.isnull().any(1)].empty
