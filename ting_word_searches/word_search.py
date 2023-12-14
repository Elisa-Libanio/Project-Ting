def exists_word(word, instance):
    word_occurrence = []

    for text in instance.elements:

        list = {
            'arquivo': text['nome_do_arquivo'],
            'palavra': word,
            'ocorrencias': []
        }

        for index, line in enumerate(text["linhas_do_arquivo"]):
            if str.lower(word) in str.lower(line):
                list['ocorrencias'].append({'linha': index + 1})
        word_occurrence.append(list)

        if len(word_occurrence[0]['ocorrencias']) == 0:
            return []

    return word_occurrence


def search_by_word(word, instance):
    search = []

    for text in instance.elements:
        list = {
            'arquivo': text['nome_do_arquivo'],
            'palavra': word,
            'ocorrencias': []
        }

        for index, line in enumerate(text["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                list['ocorrencias'].append({
                    'linha': index + 1,
                    'conteudo': line
                })
        search.append(list)

        if len(search[0]['ocorrencias']) == 0:
            return []

    return search