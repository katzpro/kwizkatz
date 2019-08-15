from nltk.corpus import wordnet


def suggest(keyword, diction, update_list):
    all_syn_anto = []
    for m in range(3):
        synonyms = []
        antonyms = []
        if len(diction[keyword[m]]) != 0:
            for syn in wordnet.synsets(keyword[m]):
                for l in syn.lemmas():
                    synonyms.append(l.name())
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())
            syn_set = sorted(set(synonyms), reverse=False)
            anto_set = sorted(set(antonyms), reverse=False)
            if len(syn_set) != 0:
                import binasearch
                syn = binasearch.binary_search(syn_set, update_list)
                if len(syn) > 1:
                    all_syn_anto = all_syn_anto + syn
                    print("synonyms of [" + keyword[m] + "] in this text: ")
                    print(syn)
            if len(anto_set) != 0:
                import binasearch
                anto = binasearch.binary_search(anto_set, update_list)
                if len(anto) > 1:
                    all_syn_anto = all_syn_anto + anto
                    print("antonyms of [" + keyword[m] + "] in this text: ")
                    print(anto)
    return all_syn_anto
