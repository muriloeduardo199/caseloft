import pytest
from pathlib import Path
from case_loft.file import extract_text

DATASET_FOLDER = Path(__file__).parent / "arquivos_pdf"


@pytest.fixture()
def pdf_file_list():
    return list(DATASET_FOLDER.glob("*.pdf"))


@pytest.fixture(params=list(DATASET_FOLDER.glob("*.pdf")))
def pdf_file(request):
    return request.param


@pytest.fixture()
def pdf_file_content(pdf_file: Path):
    return extract_text(pdf_file.absolute().as_posix())
