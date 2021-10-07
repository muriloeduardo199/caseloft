import pytest
from pathlib import Path


@pytest.fixture()
def pdf_files_list():
    dataset_folder = Path(__file__).parent / "arquivos_pdf"
    pdf_list = dataset_folder.glob("*.pdf")
    return list(pdf_list)
