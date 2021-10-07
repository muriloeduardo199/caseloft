from case_loft.file import extract_text
from typing import List
from pathlib import Path


def test_extract_text(pdf_files_list: List[Path]):
    for pdf in pdf_files_list:
        content = extract_text(pdf.absolute().as_posix())
        assert isinstance(content, str)
        assert len(content) >= 1
