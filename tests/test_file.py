from case_loft.file import extract_text
from pathlib import Path


def test_extract_text(pdf_file: Path):
    content = extract_text(pdf_file.absolute().as_posix())
    assert isinstance(content, str)
    assert len(content) >= 1
