import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, "r") as file:
            imported_file = file.read()
            return imported_file.split("\n")

    except FileNotFoundError:
        return sys.stderr.write("Arquivo " + path_file + " não encontrado\n")
