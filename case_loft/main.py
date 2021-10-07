from argparse import ArgumentParser
import extractor
import logging
from pathlib import Path


if __name__ == "__main__":
    # TODO - BONUS: Fazer uma log que preste. Olhar o formato.
    # Dica: https://docs.python.org/3/library/logging.html#logrecord-attributes
    # logger = logging.basicConfig(format="???")

    # TODO: Aceitar argumento de entrada da pasta com os arquivos e caminho do arquivo de saída, dica abaixo
    # Dica: https://docs.python.org/3/library/argparse.html#adding-arguments
    parser = ArgumentParser()
    argumentos = parser.parse_known_args()
    parser.add_argument(
        '-i', '--input', help='aceita qualquer argumento de entrada da pasta', type=str)
    parser.add_argument(
        '-o', '--output', help='aceita qualquer argumento de saida da pasta', type=str)

    args = parser.parse_args()

    # TODO: Processar os arquivos e exportar para xlsx
    # Dica: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
    arquivos = list(Path(argumentos.input).glob("*.pdf"))
    dataframe = extractor.extrair_dados_arquivos(arquivos)
    dataframe.to_excel(argumentos.output)
