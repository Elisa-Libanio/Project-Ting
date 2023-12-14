import sys
from .file_management import txt_importer


def process(path_file, instance):
    if len(instance.elements) == 1:
        return

    output = txt_importer(path_file)

    formated_output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(output),
        "linhas_do_arquivo": output
    }

    instance.enqueue(formated_output)
    sys.stdout.write(f"{formated_output}")


def remove(instance):
    if len(instance.elements) == 0:
        return sys.stdout.write("Não há elementos\n")

    output = instance.dequeue()

    if output:
        file_name = output["nome_do_arquivo"]

        sys.stdout.write(f"Arquivo {file_name} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        sys.stdout.write(f"{data}")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
