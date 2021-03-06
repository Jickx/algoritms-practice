def find_top10(text):
    """Find 10 most frequent words in text"""
    words = text.split()
    stripped_words = []
    for word in words:
        stripped_words.append(word.strip(".,"))
    words_dict = {}
    for word in stripped_words:
        if word.lower() in words_dict:
            words_dict[word.lower()] += 1
        else:
            words_dict[word.lower()] = 1
    max_list = []
    while len(max_list) < 10:
        max_v = 0
        max_k = ""
        for k, v in words_dict.items():
            if v > max_v:
                max_k = k
                max_v = v
            else:
                pass
        max_list.append(max_k)
        del(words_dict[max_k])
    return max_list


text = """Вот дом,
Который построил Джек.
А это пшеница,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
А это весёлая птица-синица,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
Вот кот,
Который пугает и ловит синицу,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
Вот пёс без хвоста,
Который за шиворот треплет кота,
Который пугает и ловит синицу,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
А это корова безрогая,
Лягнувшая старого пса без хвоста,
Который за шиворот треплет кота,
Который пугает и ловит синицу,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
А это старушка, седая и строгая,
Которая доит корову безрогую,
Лягнувшую старого пса без хвоста,
Который за шиворот треплет кота,
Который пугает и ловит синицу,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
А это ленивый и толстый пастух,
Который бранится с коровницей строгою,
Которая доит корову безрогую,
Лягнувшую старого пса без хвоста,
Который за шиворот треплет кота,
Который пугает и ловит синицу,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек.
Вот два петуха,
Которые будят того пастуха,
Который бранится с коровницей строгою,
Которая доит корову безрогую,
Лягнувшую старого пса без хвоста,
Который за шиворот треплет кота,
Который пугает и ловит синицу,
Которая часто ворует пшеницу,
Которая в тёмном чулане хранится
В доме,
Который построил Джек."""

print(find_top10(text))
